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
df=pd.DataFrame(data1,index=["gsyiSiken1","gsyiSiken2","gsyiSiken3"])
print(df)
df["Job"]=["Uzaktan Siken","Coconut Siken","Mental Siken"]#add a column
new_row=pd.DataFrame([{"Name":"Hayatbitti","Age":20,"Job":"Boş Takılma"}],index=["yokolduk"])
df=pd.concat([df,new_row])
print(df)
