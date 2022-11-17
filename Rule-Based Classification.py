# -*- coding: utf-8 -*-

# -- Sheet --

##GÖREV1
#######soru1
##persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("persona.csv")
df.head()
df.shape
df.info()

###soru2
###Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].unique()

df["SOURCE"].value_counts()


#### Soru 3: Kaç unique PRICE vardır?

df["PRICE"].unique()

### Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

#▪ Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()

### Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY")["PRICE"].sum()

#### Soru 7: SOURCE türlerine göre göre satış sayıları nedir?

df["SOURCE"].value_counts()

##### Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY")["PRICE"].mean()

### Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE")["PRICE"].mean()

###Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

print(df.groupby(["COUNTRY","SOURCE"])["PRICE"].mean())

### GÖREV 2
###############################################

#COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

print(df.groupby(["COUNTRY","SOURCE","SEX","AGE"])["PRICE"].mean())

###GÖREV3
###Çıktıyı PRICE’agöre sıralayınız.
### Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
###Çıktıyı agg_df olarak kaydediniz.

      
df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).sum("PRICE").sort_values("PRICE",ascending=False)
agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).sum("PRICE").sort_values("PRICE",ascending=False)

# GÖREV 4
###############################################

#Index’te yer alan isimleri değişken ismine çeviriniz.


agg_df = agg_df.reset_index()
agg_df.head()

# GÖREV 5
###############################################

#age değişkenini kategorik değişkene çeviriniz ve  agg_df’e ekleyiniz.
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'


bins=[0,18,23,30,40,70]
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [0,18,23,30,40,70],labels=["0_18","19_23","24_30","31_40","41_70"])

agg_df["AGE_CAT"].dtype

#### GÖREV 6
###############################################

#Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.



agg_df["customers_level_based"] = [(row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_"+row[5].upper()) for row in agg_df.values]
agg_df.head()
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE":"mean"})
agg_df.reset_index(inplace=True)
agg_df.sort_values("customers_level_based",ascending=False)

# GÖREV 7
###############################################

#Yeni müşterileri (personaları) segmentlere ayırınız.
#Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
#• Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
#• Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız)

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"],4,["D","C","B","A"])
agg_df.head()

agg_df.groupby("SEGMENT")["PRICE"].agg("max")
agg_df.groupby("SEGMENT")["PRICE"].agg("sum")
agg_df.groupby("SEGMENT")["PRICE"].agg("mean")

##Görev 8:Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
#35 yaşında IOS kullanan bir Fransız kadnı hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]



new_user1 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user1]



