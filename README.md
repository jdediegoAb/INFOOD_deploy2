# INFOOD_deploy
*Ironhack Data Analytics Final Project*
## Your app to look for productΒ΄s price in different supermarkets.
If you want to look for a specific price of a product, just use one app, no need to go through every single web page of every supermarket.One place needed for all the information of productΒ΄s prices.

Also all the product are storage in a spreadsheet in order to follow the evolution of searchs
### Technology stack π€
Python, Pandas,Streamlit

### Core technical concepts and inspiration πΈ
 This app is useful for customer care teams when they have to look for prices and solve tickets at the same time. Improves teams efficiency
### Configuration π»
import streamlit as st
import pandas as pd
import numpy as np
import fuzzywuzzy
from fuzzywuzzy import fuzz,process
from datetime import datetime
from gsheetsdb import connect
from google.oauth2 import service_account
from gspread_pandas import Spread,Client
from pandas import DataFrame

Is neccesary to make the conection to google cloud API: both google sheets and google drive

The root information is from datamarket- web page with supermarket scraped information.

### Usage π₯
    
### Folder structure πΎ
βββ INFOOD_DEPLOY2
    βββ __pycache__
    β      βββ streamlit.cpython-39.pyc
    βββ README.md
    βββ streamlit.py
    βββ .ipynb_checkpoints
    β      βββ Untitled-checkpoint.ipynb 
    βββ Infood
    β      βββ infood.ai
    β      βββ infood.png
    β      βββ infood.svg
    β      βββ butanist-a-playful-yummy-font-with-extra-2021-08-27-12-16-38-utc.zip       
    βββ Data
    β      βββ products_clean.csv 
    βββ input_infood.csv
    βββ requirements.txt
    βββ .gitignore
    βββ secrets.toml

## ToDo π¨π»βπ»
web scraping of more webs
improve the browser to obtain better results
SQL statement in the google sheet deploy in order to improve the velocity
timestamp +1 in spreadsheet


## Contact info
    j.dediego.abad@gmail.com

