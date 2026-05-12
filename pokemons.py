import pandas as pd
df=pd.read_csv("data.csv")
print(df.to_string())#everything in file
print(df["Name"])#just the name column
print(df.loc[0])#you find the row
print(df.loc[df["Name"]=="Pikachu"])#gets the row about pikachu in name column
print(df.iloc[0:10:2,0:2])#get the rows starting from 0 to 10 and skip 1. after the , take the first 2 column
tall=df[df["Height"]>=2]
print(tall)
print(df.mean(numeric_only=True))#takes the avarege of the stats
print(df.sum(numeric_only=True))#takes the sum of the stats
print(df.min(numeric_only=True))#takes the min of the stats
print(df.max(numeric_only=True))#takes the max of the stats
print(df.count())#takes the max of the stats
group=df.groupby("Type1")
print(group["Height"].mean())