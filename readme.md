<p align="center">
  <img src="https://github.com/GoyalParas/Project_Pics/blob/main/new%20logo.jpg" alt="Profile_Pic"/>
</p>

<div align="center">
  <center><h1>GradeXGuru🧑‍🎓</h1></center>
</div>

<p align="center">
  <img src="https://github.com/GoyalParas/Project_Pics/blob/main/Preview.png" alt="Profile_Pic"/>
</p>

 
## About The Project 
Recently, a friend of mine in the last semester, failed in just one subject due to serious health issues, despite having a remarkable academic record since the inception of the course, which resulted in his exemption from the campus placements, thus ruining his entire 4 year diligent hardwork. This is not just his problem; it’s common to observe in many educational institutes, putting a stained mark on the meritorious students’ future. Therefore, “Grade Guru” has come up with a unique solution for rescuing such students' by helping the educators to assess and evaluate such unfortunate students based on their previously established records within the institute.Now,let’s FLY✈️to see how?


<p align="center">
  <img src="https://github.com/GoyalParas/Project_Pics/blob/main/Approach.png" alt="Approach"/>
</p>

## Approach⭐
Focusing an end-to-end approach:
- Building a modular flask web application.
- Data Ingestion: Extract the dataset from an RDBMS,here it’s done using MYSQL🐬workbench.
- Data Transformation:Separating out the score column of the subject whose score needs to be evaluated from the raw data.
- Data Tracking: Tracking the transformed data using DVC(data version control) 📑
- Model Training: Using an ensemble of machine learning algorithms ranging from Random Forest to AdaBoost Regressor under the hood to train the model. 
- Model Evaluation: Evaluating the model using different evaluation metrics such as RMSE,MAE and R2 score.
- ML Lifecyle Tracking: We will track the whole machine learning lifecycle of this project using mlflow🌊and dagshub 🐶
- CI/CD: Automating build & test by creating code pipelines and using github actions.
- Deployment: Finally, deploying🌱 it on aws elastic beanstalk using EC2 instances or may also try Microsoft Azure, GCP.


## Project Structure
```bash
├── .ebextensions           # Elastic Beanstalk configuration files
├── .github/workflows 
├── app.py
├── setup.py
├── requirements.txt
├── data
│   ├── data-s.csv
├── notebook
│   ├── EDA.ipynb
│   └── train.ipynb
├── src
│   ├── __init__.py
│   ├── logger.py
│   ├── exception.py
│   ├── utils.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline
│   │   ├── __init__.py
│   │   ├── predit_pipeline.py
├── templates
│   ├── home.html
│   ├── index.html
├── logs
│   ├── daily-wise.log
├── test_app.py
├── .gitignore              # Git ignore file
├── README.md               # Readme file
```
  Reference form [Cookie Cutter](https://www.cookiecutter.io/)🍪🥠
## Built With
- numpy
- pandas
- mysql-connector-python
- pymysql
- scikit-learn
- sqlalchemy
- seaborn
- catboost
- xgboost
- mlflow
- dagshub
- dill
- python-dotenv
## Dataset 


- The dataset used for this project is the [Evaluation Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) from Kaggle. Which indeed is the data generated from [Royce Kimmons: Understanding digital participation divides](http://roycekimmons.com/tools/generated_data/exams)
- Though in the Kaggle a sample of 1000 rows is provided, here a 9000 rows dataset is used, by the data generator provided by Royce Kimmons with duplicates removed.


## Exploratory Data Analysis
- Check out the sleek performance metrics and graphs for each student, paired with the overall batch stats. Plus, dive into a dynamic scatter plot comparing individual and batch performance using different variables.

<p align="center">
  <img src="https://github.com/GoyalParas/Project_Pics/blob/main/EDA.png" alt="Analysis_1"/>
</p>

<p align="center">
  <img src="https://github.com/GoyalParas/Project_Pics/blob/main/EDA%202.png" alt="Analysis_2"/>
</p>

- More Description can be found in the [EDA](https://github.com/GoyalParas/GradeXGuru/blob/main/notebook/1%20.%20EDA%20STUDENT%20PERFORMANCE%20%20(1).ipynb) and [Modal Training](https://github.com/GoyalParas/GradeXGuru/blob/main/notebook/2.%20MODEL%20TRAINING.ipynb) folders.



## Models Used For Training Purpose
- CatBoosting Regressor
- Linear Regression
- Lasso
- K-Neighbours Regressor
- Ridge
- Decision Tree
- Random Forest Regressor
- XGB Regressor
- AdaBoost Regressor
## CI/CD Github Actions 
This project utilizes GitHub Actions for continuous integration and continuous deployment (CI/CD). The included workflows in the .github/workflows directory automate the build, test, and deployment processes.

The CI/CD workflow performs the following tasks:

- On each push or pull request to the main branch, it triggers the workflow.
- The workflow checks out the source code using the actions/checkout action.
- It sets up the Python environment using the actions/setup-python action and installs the required dependencies.
- The code is linted using flake8 and tested using pytest.
- If all the tests pass, the workflow proceeds to deploy the application.
The deployment workflow can be customized based on deployment target. For example, it can be configured to deploy to AWS Elastic Beanstalk or Microsoft Azure. Updating the workflow configuration file (deploy.yml) according to deployment requirements.

Link to [dagshub](https://dagshub.com/GoyalParas/GradeXGuru/experiments/#/) experiments
