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


st.set_page_config(layout="centered")
Title=st.container()
searcher=st.container()
results_=st.container()
header=st.container()
info=st.container()
columns=st.columns((1,50,1))

st.markdown("""<style>.main {background-color: #fcf8f2;text-align: center;image-align: center} <style>""",unsafe_allow_html=True)
st.markdown( """<style>.row_heading.level0 {display:none}.blank {display:none}</style>""",unsafe_allow_html=True)
#st.markdown("""<style>thead tr th:first-child {display:none}tbody th {display:none}</style>""",unsafe_allow_html=True)
original_title = '<p style="font-family:Arial Black; color:#008A89; font-size: 32px;">Insert the product you are looking for</p>'
image_title='<p style="font-family:Verdana; color:#1C5D70; font-size: 15px;">The app to look for food info</p>'
second_title = '<p style="font-family:Arial Black; color:#008A89; font-size: 32px;">List of products</p>'

#letter color
#008A89 
#1C5D70
#2F4858


@st.cache(allow_output_mutation=True) 
def get_data(filename):
    df_products=pd.read_csv(filename)
    return df_products

df_products=get_data ('./Data/products_clean.csv') 

with columns[1]:
    image = st.image("./Infood/infood.png")
    
with columns[1]:
   
    st.markdown(image_title, unsafe_allow_html=True)
    st.markdown(original_title, unsafe_allow_html=True)
    user_input=st.text_input("Enter a product👇🏽")
    #user_input3=st.number_input('Enter number of products to display 🛒',min_value=0)
    match_product = process.extract(user_input,df_products['name'],limit=5,scorer=fuzz.partial_token_sort_ratio)
    list1=[(i[0]) for i in match_product]

with columns[1]:
    st.markdown(second_title, unsafe_allow_html=True)
    if user_input!= "":
        table1=df_products.loc[df_products['name'].isin(list1)].drop(columns=['insert_date','product_id','category'])
        st.write(df_show=st.table((table1).style.format({"price": "{:.2f}","reference_price":"{:.2f}"})))#,width=40000))
        table1.to_csv('input_infood.csv', mode='a', index=False, header=False)
        #a=table1.to_csv(mode='a', index=False, header=False).encode('utf-8')    
    else:
        st.write("no insert 🫤")
        st.stop()

        
        
        
scope= ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']   
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)
     
sheet_url = st.secrets["public_gsheets_url"]       
client = Client(scope=scope,creds=credentials)
spreadsheetname = 'infood2'
spread = Spread(spreadsheetname,client = client)

with columns[1]:
    st.write(spread.url)

sh = client.open(spreadsheetname)
worksheet_list = sh.worksheets()

def worksheet_names():
    sheet_names = []   
    for sheet in worksheet_list:
        sheet_names.append(sheet.title)  
    return sheet_names
def load_the_spreadsheet(spreadsheetname):
    worksheet = sh.worksheet(spreadsheetname)
    df = DataFrame(worksheet.get_all_records())
    return df
def update_the_spreadsheet(spreadsheetname,dataframe):
        col = ['input','Time_stamp']
        spread.df_to_sheet(dataframe[col],sheet = spreadsheetname,index = False)

now = datetime.now()
opt = {'input':[user_input],
         'Time_stamp' :  [now]} 
opt_df = DataFrame(opt)
df = load_the_spreadsheet('sheet1')
new_df = df.append(opt_df,ignore_index=True)
update_the_spreadsheet('sheet1',new_df)   

with columns[1]:
    conn = connect(credentials=credentials)               
    @st.cache(ttl=600)
    def run_query(query):
        rows = conn.execute(query, headers=1)
        rows = rows.fetchall()
        return rows
    query= f'SELECT input COUNT(input) AS input_count FROM "{sheet_url}" GROUP BY "input" ORDER by "input_count" LIMIT 3'
    SELECT my_column COUNT(my_column)


    
    rows = run_query(query)
    # Print results.
    st.table(rows)
