import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


dataset = "Talent_Academy_Case_DT_2025.xlsx"
df = pd.read_excel(dataset, sheet_name="Sheet1")


df["Yas"] = df["Yas"].astype(str).str.extract(r"(\d+)").astype(float)
df["UygulamaSuresi"] = df["UygulamaSuresi"].astype(str).str.extract(r"(\d+)").astype(float)
df["TedaviSuresi"] = df["TedaviSuresi"].astype(str).str.extract(r"(\d+)").astype(float)


num_cols = ["Yas", "UygulamaSuresi", "TedaviSuresi"]
imputer = SimpleImputer(strategy="mean")
df[num_cols] = imputer.fit_transform(df[num_cols])

cat_cols = ["Cinsiyet", "KanGrubu", "Uyruk", "Bolum", 
            "TedaviAdi", "UygulamaYerleri", "KronikHastalik", "Alerji", "Tanilar"]

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])


ct = ColumnTransformer(transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)],remainder="passthrough")

X = df.drop(columns=["TedaviSuresi"]) 
y = df["TedaviSuresi"]  

X_encoded = ct.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split( X_encoded, y,test_size=0.2,random_state=42)


plt.hist(df["Yas"], bins=15, color="skyblue", edgecolor="black")
plt.title("Yaş Dağılımı")
plt.xlabel("Yaş")
plt.ylabel("Hasta Sayısı")
plt.show()


plt.hist(df["TedaviSuresi"], bins=15, color="orange", edgecolor="black")
plt.title("Tedavi Süresi Dağılımı")
plt.xlabel("Dakika")
plt.ylabel("Hasta Sayısı")
plt.show()
