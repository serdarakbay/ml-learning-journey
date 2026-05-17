import pandas as pd
data=[100,102,104]
series  =pd.Series(data,index=["A","B","C"])
print(series)
series.loc["A"]=200
print(series)
data1={
    "Name":["Asensio","Skriniar","Kerem"],
        "Age":[30,31,27]
}
df=pd.DataFrame(data1,index=["row1","row2","row3"])
print(df)
df["Job"]=["Forward","Defender","Midfielder"]#add a column
new_row=pd.DataFrame([{"Name":"Newplayer","Age":20,"Job":"Reserve"}],index=["row4"])
df=pd.concat([df,new_row])
print(df)