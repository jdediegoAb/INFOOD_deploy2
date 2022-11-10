# INFOOD_deploy
*Ironhack Data Analytics Final Project*
## Your app to look for product´s price in different supermarkets.
If you want to look for a specific price of a product, just use one app, no need to go through every single web page of every supermarket.One place needed for all the information of product´s prices.

Also all the product are storage in a spreadsheet in order to follow the evolution of searchs
### Technology stack 🤓
Python, Pandas,Streamlit

### Core technical concepts and inspiration 📸
 This app is useful for customer care teams when they have to look for prices and solve tickets at the same time. Improves teams efficiency
### Configuration 💻
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

### Usage 🖥
    
### Folder structure 💾
└── INFOOD_DEPLOY2
    ├── __pycache__
    │      └── streamlit.cpython-39.pyc
    ├── README.md
    ├── streamlit.py
    ├── .ipynb_checkpoints
    │      └── Untitled-checkpoint.ipynb 
    ├── Infood
    │      ├── infood.ai
    │      ├── infood.png
    │      ├── infood.svg
    │      ├── butanist-a-playful-yummy-font-with-extra-2021-08-27-12-16-38-utc.zip       
    ├── Data
    │      ├── products_clean.csv 
    ├── input_infood.csv
    ├── requirements.txt
    ├── .gitignore
    ├── secrets.toml

## ToDo 👨🏻‍💻
web scraping of more webs
improve the browser to obtain better results
SQL statement in the google sheet deploy in order to improve the velocity
timestamp +1 in spreadsheet


## Contact info
    j.dediego.abad@gmail.com

