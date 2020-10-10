[![DOI](https://zenodo.org/badge/265002033.svg)](https://zenodo.org/badge/latestdoi/265002033)

# playa-inundation
Exploring and modeling Playa Lake inundation

## Overview
This repo hosts only the code. The data is available on figshare and s3, instructions below. For the code itself, there are 4 directories containing jupyter notebooks:

- **exploration**: Exploring the data
- **preprocessing**: Prep the data for modeling
- **modeling**: Code for modeling inundation. The important notebook is "lstm.ipynb". 
- **analysis**: Analysing the model results and the network weights


## Preparing the Python Environment
The python environments can be recreated via conda using the two yaml files:
- *base_environment.yml*: A lighter weight environment for exploration, preprocessing, and analysis.
- *lstm_environment.yml*: A bulkier environment with pytorch and cuda, used for training the model and prediction. 

## Data
The pre-processed data is publicly available on figshare (see below for details). This is all the data needed to recreate the modeling and analysis. We suggest creating a directory called "data" in the main code directory (i.e. playa-inundation/playa-inundation/data/, same level as exploration, modeling, and analysis directories) and saving the data there. 

#### Preprocessed model-ready data:
The only input to the actual modeling code is an hdf5 file available on figshare:
https://doi.org/10.6084/m9.figshare.13017650.v1

#### Raw(ish) inputs
The raw data are available on AWS s3. You don't need to use any of these for the modeling itself, but if you would like to alter/recreate the preprocessing these are the base inputs:
- s3://earthlab-ksolvik/playa/data/jrc-water_1984-2019.csv: Inundation data for all playas, all months
- s3://earthlab-ksolvik/playa/data/prism.csv: Weather data for same time span (monthly precip, temp, and vpd)
- s3://earthlab-ksolvik/playa/data/fraster_landcover_allyears_bigger.csv: Landcover fractions within 200m of playa centerpoints

*Note:* The intermediate data (merged water and weather data split by county) is not on s3, but can be recreated using exploration/preprocess_split_data.ipynb

## Recreating the analysis

### 0. Exploration (Optional)
playa-inundation/exploration contains several notebooks that may be useful for getting an overview of the inundation and weather data. *NOTE:* you must run the preprocess_split_data.ipynb notebook from the preprocessing directory before using the exploration notebooks (see below).

### 1. Preprocessing
playa-inundation/preprocessing contains notebooks, scripts, and modules used to prepare the data for modeling, . If you downloaded the hdf file, you don't need to run any of these preprocessing steps. 

- *preprocess_split_data.ipynb*: Run first. Preprocesses the weather and inundation data and splits it by county and state csvs, which are more manageable.
- *prep_dataloader.ipynb*: Run after. 
- *raster_extract_wrapper.py*: You can skip this script. Extracts the Sohl et al. land cover around each playa. The output is already available on s3 (fraster_landcover_allyears_bigger.csv).
- *fraster_extract.py*: Python mmodule for performing the buffered extraction. Used by raster_extract_wrapper.py.

### 2. Modeling
playa-inundation/modeling contains notebooks for training the CNN and saving the weights and predictions.

- *lstm.ipynb*: Train CNN and save model weights. There are many parameters that can be set within the notebook, but the values in the notebook currently are the final ones used after performance tuning. 
- *predict_save_results.ipynb*: Loads saved model weights, performs inference throughout the entire time series, and saves the results as '../data/all_preds.csv'.

There are two other notebooks as well for running basic linear and logistic regression models. These were used as baseline models to compare against the CNN.

### 3. Analysis
playa-inundation/analysis contains notebooks for analyzing the modeling results. 

- *model_analysis.ipynb*: Calculate basic performance metrics (e.g. F1, AUC, etc.) and visualize predicted inundation probability vs. true inundation for individual playas.
- *simulate_inundation.ipynb*: Simulate inundation trajectories based on the predicted inundation probabilities. Creates a figure of monthly estimated inundation fraction. 
- *mapping.ipynb*: Create maps of playa inundation and model performance.
- *visualize_embeddings.ipynb*: Visualize embedding spaces using tensorboard. Not very useful for drawing insights, but potentially interesting.
