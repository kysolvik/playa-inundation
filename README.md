# playa-inundation
Exploring and modeling Playa Lake inundation

## Overview
This repo hosts only the code. The data is available on s3, instructions below. For the code itself, there are 3 directories containing jupyter notebooks:

- **exploration**: Exploring the data, but ALSO some preprocessing.
- **modeling**: Code for modeling inundation. The important notebook is "lstm.ipynb". 
- **analysis**: Analysing the model results and the network weights

## Data
The data is all on s3, both in raw and preprocessed formats. The data is all in: s3://earthlab-ksolvik/playa/data/

*Note:* The intermediate data (merged water and weather data split by county) is not on s3, but can be recreated using exploration/preprocess_split_data.ipynb

#### Raw(ish) inputs
You don't need to use any of these for the modeling itself, but if you would like to alter/recreate the preprocessing these are the base inputs:
- s3://earthlab-ksolvik/playa/data/jrc-water_1984-2019.csv: Inundation data for all playas, all months
- s3://earthlab-ksolvik/playa/data/prism.csv: Weather data for same time span (monthly precip, temp, and vpd)
- s3://earthlab-ksolvik/playa/data/fraster_landcover_allyears_bigger.csv: Landcover fractions within 1km of playa centerpoints

#### Preprocessed model-ready data:
The only input to the actual modeling notebook is this hdf:
s3://earthlab-ksolvik/playa/data/all_prepped_data.h5

*After downloading, be sure to update the paths in the lstm.ipynb notebook.*


## Recreating the analysis

### 1. Exploration

### 2. Modeling

### 3. Analysis

