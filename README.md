[![DOI](https://zenodo.org/badge/265002033.svg)](https://zenodo.org/badge/latestdoi/265002033)

# playa-inundation
Exploring and modeling Playa Lake inundation

## Overview
This repo hosts only the code. The data is available on s3, instructions below. For the code itself, there are 3 directories containing jupyter notebooks:

- **exploration**: Exploring the data, but ALSO some preprocessing.
- **modeling**: Code for modeling inundation. The important notebook is "lstm.ipynb". 
- **analysis**: Analysing the model results and the network weights

## Data
The pre-processed data is publicly available on figshare (see below for details). This is all the data needed to recreate the modeling and analysis. We suggest creating a directory called "data" in the main code directory (i.e. playa-inundation/playa-inundation/data/, same level as exploration, modeling, and analysis directories) and saving the data there. 

#### Preprocessed model-ready data:
The only input to the actual modeling code is an hdf5 file available on figshare:
https://doi.org/10.6084/m9.figshare.13017650.v1

#### Raw(ish) inputs
The raw data are available on AWS s3. You don't need to use any of these for the modeling itself, but if you would like to alter/recreate the preprocessing these are the base inputs:
- s3://earthlab-ksolvik/playa/data/jrc-water_1984-2019.csv: Inundation data for all playas, all months
- s3://earthlab-ksolvik/playa/data/prism.csv: Weather data for same time span (monthly precip, temp, and vpd)
- s3://earthlab-ksolvik/playa/data/fraster_landcover_allyears_bigger.csv: Landcover fractions within 1km of playa centerpoints

*Note:* The intermediate data (merged water and weather data split by county) is not on s3, but can be recreated using exploration/preprocess_split_data.ipynb

*After downloading, be sure to update the paths in the lstm.ipynb notebook.*


## Recreating the analysis

### 1. Exploration

### 2. Modeling

### 3. Analysis

