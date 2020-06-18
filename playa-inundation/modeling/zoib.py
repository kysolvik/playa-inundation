import torch
from torch.distributions import Beta
from torch.distributions import constraints
from torch.distributions.exp_family import ExponentialFamily
from torch.distributions.utils import broadcast_all
from torch.distributions.dirichlet import Dirichlet
from numbers import Number


class ZOIBeta(ExponentialFamily):
    """ Zero one inflated Beta distribution
    
    Args: 
        p (float or Tensor): Pr(y = 0)
        q (float or Tensor): Pr(y = 1 | y != 0)
        concentration1 (float or Tensor): 1st Beta dist. parameter 
            (often referred to as alpha)
        concentration0 (float or Tensor): 2nd Beta dist. parameter
            (often referred to as beta)
    """
    
    arg_constraints = {
        'p': constraints.unit_interval, 
        'q': constraints.unit_interval, 
        'concentration1': constraints.positive, 
        'concentration0': constraints.positive
    }
    support = constraints.unit_interval # does this include 0 and 1?
    has_rsample = False
    
    def __init__(self, p, q, concentration1, concentration0, validate_args=None):
        if isinstance(concentration1, Number) and isinstance(concentration0, Number):
            self.concentration1_concentration0 = torch.tensor([float(concentration1), float(concentration0)])
        else:
            concentration1, concentration0 = broadcast_all(concentration1, concentration0)
            self.concentration1_concentration0 = torch.stack([concentration1, concentration0], -1)
        self._dirichlet = Dirichlet(self.concentration1_concentration0)
        self.log_p = torch.log(p)
        self.log1m_p = torch.log(1 - p)
        self.log_q = torch.log(q)
        self.log1m_q = torch.log(1 - q)
        super(ZOIBeta, self).__init__(self._dirichlet._batch_shape, validate_args=validate_args)
    
    def beta_lp(self, value):
        if self._validate_args:
            self._validate_sample(value)
        heads_tails = torch.stack([value, 1.0 - value], -1)
        return self._dirichlet.log_prob(heads_tails)
    
    def log_prob(self, value):
        lp = torch.zeros_like(value, dtype = torch.float)
        if torch.mul(value>0., value<1.).any():
            beta_idx = torch.where(torch.mul(value>0., value<1.))
            self._dirichlet = Dirichlet(self.concentration1_concentration0[beta_idx])
            lp[beta_idx] = self.log1m_p[beta_idx] + self.log1m_q[beta_idx] + self.beta_lp(value[beta_idx])
        lp[torch.where(value == 0.)] = self.log_p[torch.where(value==0.)]
        lp[torch.where(value == 1.)] = self.log1m_p[torch.where(value==1.)] + self.log_q[torch.where(value==1.)]
        return lp


def zoib_loss(t, y_true, pad=0.0001):
    neg_log_probs = -1*ZOIBeta(
        p=t[:,0]+pad,
        q=t[:,1]+pad,
        concentration1=t[:,2]+pad,
        concentration0=t[:,3]+pad
    ).log_prob(torch.tensor(y_true).float())
    
    return torch.mean(log_probs)
