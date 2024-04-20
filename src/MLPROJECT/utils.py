import os
import sys
from src.MLPROJECT.exception import CustomException
from src.MLPROJECT.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
from sqlalchemy import create_engine

#import mysql.connector

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')


def read_sql_data():
    logging.info("Reading SQL Database Started")
    try:
        mydb=pymysql.connect(
        #mydb=mysql.connector.connect(  
            host=host,
            user=user,
            password=password,
            database=db
        )
        engine=create_engine('mysql+pymysql://root:12345@localhost/college')
        logging.info("connection established") 
        df=pd.read_sql('select * from students',engine)
        print(df.head())

        return df
    
    except Exception as ex:
        raise CustomException(ex)
