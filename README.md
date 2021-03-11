
![Alt text](Banner-2.png?raw=true "Title")

Interactive website to calculate the power consumption in a power plant based on distinct variables such as Ambient Temperature , Relative Humidity, Exhaust Vacuum  and Ambient Pressure. Numerical values of these features can be entered in a website deployed using Heroku to compute the electrical energy per hour (MW). This project is presented as an upgraded version of what originally was a Master's degree course assignment.

## Table of Contents 

- [Project Website](#project-website)
- [Project Workflow](#project-workflow)
- [Project Description](#project-description)
- [Requirements](#requirements)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [App Deployment using Heroku](#app-deployment-using-heroku)
- [Dataset Information](#dataset-information)
- [Acknowledgements](#acknowledgements)
- [License](#license)


## Project Website 

[(Back to top)](#table-of-contents)

[Project Website](https://pycaret-power.herokuapp.com/predict). The user can enter values for different features such as Ambient Temperature, Relative Humidity, Exhaust Vacuum and Ambient Pressure *within the ranges specified* to obtain a prediction for the electrical energy output in MW.  


## Project Workflow 

[(Back to top)](#table-of-contents)

  - Training machine learning models using Pycaret
  - Simple web application using Flask
  - Deployment of the web application using Heroku 

## Project Description 

[(Back to top)](#table-of-contents)

This project focuses on training several machine learning models on a dataset based on sensor readings in a power plant to predict the net hourly energy output. This problem can be formulated as a regression model as the feature being predicted is a quantitative element. Further, a web application is built using Flask and  deployed using Heroku and the application built using Python can be accessed using an URL. The source code needed for the app deployment is hosted on Github.

## Requirements 

[(Back to top)](#table-of-contents)

- Flask 
- Heroku account
- Git
- Pycaret
- Pandas

## Installation

[(Back to top)](#table-of-contents)

- pip install pycaret
- pip install flask
- pip install pandas

## Model Training 

[(Back to top)](#table-of-contents)

Models were trained using [Pycaret](https://pycaret.org/guide/), which is an open source machine learning library that can be used to perform simple classification and regression tasks. This dataset consists of quantitative values and hence a regression task is suitable to make predictions. The Pycaret library can be used to build several machine learning models and the optimal model is chosen based on several performance metrics such as R2, MSE, MAPE, etc. In this project, the metric used to determine the best model is R2. The best model used in making the predictions is XGBoost, although any of the top three models maybe utilised for the same. 20% of the dataset is preserved as the test set. 
The models are created and tuned (10 fold cross validation) and compared using different metrics.

## Model Performance

[(Back to top)](#table-of-contents)

![Alt text](ResPlot.png?raw=true "Title")

The graph above indicates a residual plot for the XgBoost model. In the plot, each point represents hourly average sensor outputs and the x and y axes represent the predicted values and residuals respectively. The distance of a point from the line at '0' represents how far the predicted value is from the actual value. Consequently, points scattered around zero indicate a good model. 

## Web Application

[(Back to top)](#table-of-contents)

[Flask](https://flask.palletsprojects.com/en/1.1.x/) has been utilised to build the web application. 

## App Deployment using Heroku

[(Back to top)](#table-of-contents)

The app deployed locally using Flask is deployed as a website using [Heroku](https://www.heroku.com).

## Dataset Information

[(Back to top)](#table-of-contents)

The [dataset](https://archive.ics.uci.edu/ml/datasets/Combined+Cycle+Power+Plant#) is available on the UCI Machine Learning Repository.

## Acknowledgements

[(Back to top)](#table-of-contents)

 https://github.com/pycaret/deployment-heroku

## License

[(Back to top)](#table-of-contents)

Released under MIT License.

## Citation 

[(Back to top)](#table-of-contents)

1. Pınar Tüfekci, Prediction of full load electrical power output of a base load operated combined cycle power plant using machine learning methods, International Journal of Electrical Power & Energy Systems, Volume 60, September 2014, Pages 126-140, ISSN 0142-0615, [Web Link].
([Web Link])

2. Heysem Kaya, Pınar Tüfekci , Sadık Fikret Gürgen: Local and Global Learning Methods for Predicting Power of a Combined Gas & Steam Turbine, Proceedings of the International Conference on Emerging Trends in Computer and Electronics Engineering ICETCEE 2012, pp. 13-18 (Mar. 2012, Dubai)

