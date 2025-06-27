import pandas as pd
import numpy as np
data={"col1":[3,np.nan,np.nan,2],"col2":[1.0,pd.NA,pd.NA,2.0]}
#df=pd.DataFrame(data)
#print(df)
#f=df.fillna(21)
#print(f)
df = pd.DataFrame([[9, -3, -2], [-5, 1, 8], [6, 4, -8]],
                  index=['a', 'c', 'd'],
                  columns=['one', 'two', 'three'])
df=df.reindex(['a','b','c','d','e'])
print(df)
print(df.ffill())
print(df.bfill())
print(df)
print(df.ffill(limit=1))
print(df.replace({-3:300,-5:500}))
df1= pd.DataFrame(['$40,000*','$40000 conditions attached'], columns=['P'])
print(df1)
df1['P']=df1['P'].str.replace(r'\D+',"",regex=True).astype(int)
print(df1)
data1 = {'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A'],'Value': [10, 15, 12, 8, 20, 5, 18]}
print(data1)
df2=pd.DataFrame(data1)
print(df2)
group_data = df2.groupby('Category')['Value'].sum()
print(group_data)
print(df2.groupby('Category')['Value'].mean())
print(df2.groupby('Category')['Value'].count())
print(df2.groupby('Category')['Value'].min())
print(df2.groupby('Category')['Value'].max())
print(df2.groupby('Category')['Value'].agg(['min','max']))
