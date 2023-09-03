# -*- coding: utf-8 -*-
"""vix_Izra Noor Zahara Aliya.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18NSStrn1cyrZ1c_PF0Am1h97T_n3mRwr
"""

import numpy as np
import pandas as pd


# for operation 2
dfc = pd.read_csv('/content/Case Study - Customer.csv',sep=';')
dfp = pd.read_csv('/content/Case Study - Product.csv',sep=';')
dfs = pd.read_csv('/content/Case Study - Store.csv',sep=';')
dft = pd.read_csv('/content/Case Study - Transaction.csv',sep=';')

dfc.describe()

print(dfc)

print(dfp)

print(dfs)

print(dft)

dfp.describe()

# Mengubah tipe data kolom 'date' menjadi datetime
dft['Date'] = pd.to_datetime(dft['Date'])0

# Menampilkan DataFrame setelah mengubah tipe data kolom 'date'
print(dft)

dfc.to_csv('Customer.csv', index=False)
dfp.to_csv('Produck.csv', index=False)
dfs.to_csv('Store.csv', index=False)
dft.to_csv('Transaction.csv', index=False)

dfc.to_csv('Customer.csv', index=False)

dfp.to_csv('/content/Case Study - Product', index=False)

# Melihat kolom-kolom yang memiliki missing value (nilai null)
kolom_dengan_missing_value = dfc.columns[dfc.isna().any()].tolist()

# Menampilkan nama kolom yang memiliki missing value
print("Kolom dengan missing value:")
print(kolom_dengan_missing_value)

mode_marital_status = dfc['Marital Status'].mode().iloc[0]

# Mengganti nilai-nilai yang hilang di kolom 'Marital Status' dengan mode
dfc['Marital Status'].fillna(mode_marital_status, inplace=True)

# Menampilkan DataFrame setelah mengganti nilai-nilai yang hilang
print(dfc)

# Melihat kolom-kolom yang memiliki missing value (nilai null)
kolom_dengan_missing_value = dfp.columns[dfp.isna().any()].tolist()

# Menampilkan nama kolom yang memiliki missing value
print("Kolom dengan missing value:")
print(kolom_dengan_missing_value)



null_count_dfc = dfc.isnull().sum()
print(null_count_dfc)

null_count_dfs = dfs.isnull().sum()
print(null_count_dfs)

null_count_dfp = dfp.isnull().sum()
print(null_count_dfp)

null_count_dft = dft.isnull().sum()
print(null_count_dft)

dfc.info()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


# Menggabungkan DataFrame dfp dan dft berdasarkan 'ProductID'
merged_data = dfp.merge(dft, on='ProductID')

# Mengagregasi data dengan mengelompokkan berdasarkan tanggal dan menjumlahkan kuantitas produk
daily_qty = merged_data.groupby('Date')['Qty'].sum()

# Membuat time series data yang memuat total kuantitas harian
ts_data = daily_qty.resample('D').sum()

# Mengisi nilai-nilai yang hilang dengan 0 jika diperlukan
ts_data = ts_data.fillna(0)

# Memisahkan data menjadi data pelatihan dan data uji
train_data = ts_data.iloc[:-7]  # Menggunakan data historis untuk pelatihan
test_data = ts_data.iloc[-7:]   # Menggunakan data terakhir sebagai data uji

# Memodelkan data dengan ARIMA
model = ARIMA(train_data, order=(1, 1, 1))
model_fit = model.fit()

# Membuat prediksi untuk 7 hari ke depan
forecast_steps = 7
forecast = model_fit.forecast(steps=forecast_steps)

# Menampilkan hasil prediksi
print("Prediksi 7 Hari ke Depan:")
print(forecast)

# Plot hasil prediksi
plt.figure(figsize=(12, 6))
plt.plot(train_data.index, train_data.values, label='Data Pelatihan')
plt.plot(test_data.index, test_data.values, label='Data Uji')
plt.plot(test_data.index, forecast, label='Prediksi')
plt.title('Prediksi Total Kuantitas Harian Produk yang Terjual')
plt.xlabel('Tanggal')
plt.ylabel('Total Kuantitas')
plt.legend()
plt.grid(True)
plt.show()

from sklearn.cluster import KMeans
merged_data = pd.merge(dfc[['CustomerID', 'Marital Status']], dft[['CustomerID', 'TransactionID', 'Qty', 'TotalAmount']], on='CustomerID')

# Melakukan agregasi
agg_data = merged_data.groupby('CustomerID').agg({
    'TransactionID': 'count',
    'Qty': 'sum',
    'TotalAmount': 'sum'
}).reset_index()


kmeans = KMeans(n_clusters=3)
agg_data['Cluster'] = kmeans.fit_predict(agg_data[['TransactionID', 'Qty', 'TotalAmount']])

# Menampilkan hasil clustering
print(agg_data)

