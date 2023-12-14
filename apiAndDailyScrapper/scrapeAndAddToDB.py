

import pandas as pd
import os
from sqlalchemy import create_engine

from dailyScrapper import DailyScrapper
import joblib

import yfinance as yf

#this function will scrape the openinsider website and add the new data to the database, whihc is today's data
def lambda_handler(event, context):
    #url for latest day of trading
    url = "http://openinsider.com/screener?s=&o=&pl=&ph=&ll=&lh=&fd=1&fdr=&td=0&tdr=&fdlyl=&fdlyh=&daysago=&xp=1&vl=&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&grp=2&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1"
    scrapper = DailyScrapper(url)

    df = scrapper.data

    # Set up RDS database connection using environment variables
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')

    # Construct the connection string
    connection_string = f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    #add the data to the database
    engine = create_engine('postgresql://username:password@host:port/database_name')

    # Write DataFrame to the RDS database
    table_name = 'insider-tradingdata'
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

    #runs ML model on the data
    naive_bayes_model = joblib.load('naive_bayes_model.joblib')

    DataForML = pd.DataFrame({
        'Insider_Amount': df["Insider_Amount"], 
        'ΔOwn': df["ΔOwn"],  
    })

    predictions = naive_bayes_model.predict(DataForML)

    #adds the predictions to the stock to buy database       
    df['predictions'] = predictions

    stockToBuy = df[df['prediction'] == 1]

    #gets the price of that row from YFinance
    for index, row in stockToBuy.iterrows():
        symbol = row['Ticker']
        price = get_latest_price(symbol)

        #if yf doesnt have stock data, drop it from the dataframe
        if(price == 0):
            stockToBuy.drop(index, inplace=True)

        stockToBuy.at[index, 'Price'] = price

    stockToBuy.to_sql('trades', con=engine, if_exists='replace', index=False)

    return {
        'statusCode': 200,
        'body': 'Successfully scrapped, processed with ML and then added to database'
    }

def get_latest_price(symbol):
    stock = yf.Ticker(symbol)
    latest_price = stock.history(period='1d')['Close'].iloc[-1]
    return latest_price or 0

