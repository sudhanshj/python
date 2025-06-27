from operator import index

import pandas as pd
import numpy as np
data = {'Name': ['ABC', 'XYZ', 'PQR'], 'Age': [28, 22, 34],index:[
    4,6,5]}
df=pd.DataFrame(data)
print(df)
res=df.sort_values(by=['Age','Name'],ascending=[False,True],inplace=True)
res1=df.sort_index(ascending=False)
print(res)
print(pd.date_range('24-06-25',periods=5))
