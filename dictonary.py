import pandas as pd
data={
"qmarks":[10,20,30],"duration":[50,40,45]
}
myvar=pd.Series(data)
print(myvar)
print(myvar.tolist())
print(myvar.loc(0))
data_set={
    'A':[1,2,3],
    'B':[10,20,30],
    'C':[4,5,8]
}
df=pd.DataFrame(data_set)
#df.index=["day1","day2","day3"]
print(df)
print(pd.Series(data_set))
print(df.loc(0))
print(df.loc[0:1,])
#print(df.loc("A"))
df.index=[100,200,300]
print(df)
result=df.columns
print(result)
df.columns=["col1","col2","col3"]
print(df)
print(df.iloc[0:1])
#print(df.loc['col1'])
print(df.iloc[0:2])
#print(df.loc[:,100])
#df.iloc[0:2,0]=['x','y']
df.drop(200)
print(df)
#result = df[df[300] != 0]
print(result)

