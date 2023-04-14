# -*- coding: utf-8 -*- 位于头部,表示文件中带有中文,需要使用UTF8编码,同时注意保存UTF-8格式.
import sys
import pandas as pd
from src import get_price as gp
from src import get_prediction_model as gm
sys.path.append("./src/")

if __name__ == '__main__':
    fileName = './dataset/data_stocks.csv'
    data = pd.read_csv(fileName)
    df = data[['DATE', 'SP500', 'NASDAQ.AAL', 'NASDAQ.GOOGL', 'NASDAQ.FB', 'NASDAQ.AMZN', 'NASDAQ.MSFT']]

    gp.get_stock_price(df)
    gp.get_Compared_price(df)
    gp.get_df_income(df)
    gp.get_df_change(df)
    gp.get_df_mean(df)

    gm.build_predictive_model1(df)
    gm.build_predictive_model2(df)