import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv("MyData.csv", sep=",")



df["SRX_query"] = df["relation.1"].str.replace("SRA: ","")
# Get query and get srr numbers from beautiful soup
def query(q, df):
    print("querying... ", q)
    SRX = q.split("=")[1]
    df2 = pd.DataFrame(columns=["SRX","SRR"])
    page = requests.get(q)
    soup = BeautifulSoup(page.content, 'html.parser')
    t = soup.find_all('table')[0]
    t = t.find_all('a', href=True)
    srr = []
    for x in t:
        for s in x:
            df2 = df2.append({"SRX": SRX, "SRR": s, "SRX_query": q}, ignore_index=True)
    df_merge = pd.merge(df2,df, on="SRX_query", how="inner")

    return df_merge





#  Append all of the samples to a final dataframe
df_final = pd.DataFrame()
for x in range(len(df)):
    q = df["SRX_query"].iloc[x]
    if "SRX" in q:
        # print("q is ", q)
        df_merge = query(q, df)
        df_final = df_final.append(df_merge)

#Write out final dataframe
df_final.to_csv("MyData_with_SRR.csv", index=None, sep=",")


df = df_final[["SRR","title"]]
df.to_csv("MyData_SRR_title.csv", index=None, sep="\t")
print("done ")

