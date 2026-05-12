import pandas as pd
df=pd.read_csv("data.csv")
df=df[df["Legendary"]==1] 
group=df.groupby("Type1")  
print(group["Weight"].mean())
print(df.sort_values("Weight",ascending=False))
