# Yield-Prediction-Model
This repository is part of my Predictive Analytics project

### Statement
Crop Yield Prediction is predicting the yield of a crop in future based on the dependent factors. Crop yield is dependent on factors like rainfall, pressure, temperature, pesticide use etc. This is achieved by Designing a system to predict crop yield.

### Motivation
This project is based on the curbing the problem faced by the farmers as well as providing the accurate level of the harvest they
can expect from the crop they have growth depending on the dependent factors like temperature, rainfall, etc. This project is
mainly developed to help farmers so that this may help them in analysis of the yield of their crop. Farmers are facing loses in the
crop yield due to  improper knowledge of the crop and the natural factor that are effecting them. In this project we analysis the
factors that shows the crop’s yield well before the harvest

### Dataset
- The chosen dataset was taken from Kaggle Repository.
- Contains the crop yield production of 10 crops from all states and union territories from India. Records start from 1990 to 2013.
- 20,847 Rows with 7 attributes : Area, Item, Year, Yield (hg/ha), Average Rainfall (mm), Pesticides, Average Temperature. 

### Models USed
- Machine Learning
- Ensemble supervised Learning
- Extra Trees Regressor

### Tech Stack
- This project uses Flask to build a RESTful Server, which can be accessed by the UI and as a RESTFUL API endpoint

### Model Implmentation Limitations
- To use the trained model for all requests, without training it individually each time, a .plk file for the trined model is used.
- Due to the large size of this file, it has been compressed into model.zip
- Uncompress this file and then call the endpoint.