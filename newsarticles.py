# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:01:48 2022

@author: theresa.fenech
"""

from GoogleNews import GoogleNews
import pandas as pd
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
onemonthago = (date.today() - relativedelta( months = +1 ))


df1 = pd.read_excel(r'file:///C:\Users\therese.fenech\OneDrive%20-%20Malta%20Enterprise\Desktop\Tracked_companies.xlsx' , header=0)
companies = df1.values.tolist()

results = {}

googlenews = GoogleNews()


for company in companies:
     googlenews.search(str(company))
     results = googlenews.result()
     df = pd.DataFrame.from_dict(results)
     df['keyword'] = company

df['check_date'] = pd.to_datetime(df['date'], errors='coerce', )





df.to_excel(r'C:\Users\therese.fenech\OneDrive - Malta Enterprise\Desktop\NewsArticles.xlsx', index = False)

