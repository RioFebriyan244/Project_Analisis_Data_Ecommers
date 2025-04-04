# -*- coding: utf-8 -*-
"""dashboard_visualisasi_analisis_ecommers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-PR0e30FUbeL8IXgMRLy8P9z95c5VXDD
"""

import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

all_df = pd.read_csv('https://raw.githubusercontent.com/RioFebriyan244/Project_Analisis_Data_Ecommers/refs/heads/main/dashboard/all_data_ecommers.csv')
order_df = pd.read_csv("https://raw.githubusercontent.com/RioFebriyan244/Project_Analisis_Data_Ecommers/refs/heads/main/data/orders.csv")
all_df["order_date"] = pd.to_datetime(all_df["order_date"])

monthly_orders_df = all_df.resample(rule='M', on='order_date').agg({
    "order_id": "nunique",
    "total_price": "sum"
})
monthly_orders_df.index = monthly_orders_df.index.strftime('%B')
monthly_orders_df = monthly_orders_df.reset_index()
monthly_orders_df.rename(columns={
    "order_id": "order_count",
    "total_price": "revenue"
}, inplace=True)
monthly_orders_df.head()


# Judul halaman
st.title("Number of Orders per Month (2021)")
# Buat plot-nya
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    monthly_orders_df["order_date"],
    monthly_orders_df["order_count"],
    marker='o',
    linewidth=2,
    color="#72BCD4"
)
ax.set_title("Number of Orders per Month (2021)", loc="center", fontsize=20)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

# Tampilkan di Streamlit
st.pyplot(fig)

# Judul halaman
st.title("Total Revenue per Month in 2021 (AUD)")

# Misalnya monthly_orders_df sudah tersedia dan memiliki kolom 'order_date' & 'revenue'

# Buat figure dan axis
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    monthly_orders_df["order_date"],
    monthly_orders_df["revenue"],
    marker='o',
    linewidth=2,
    color="#72BCD4"
)
ax.set_title("Total Revenue per Month in 2021 (AUD)", loc="center", fontsize=20)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)

# Tampilkan chart di Streamlit
st.pyplot(fig)

sum_order_items_df = all_df.groupby("product_name").quantity_x.sum().sort_values(ascending=False).reset_index()


# Judul halaman
st.title("Best and Worst Performing Product by Number of Sales")

# Buat figure dan axes
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

# Warna: satu biru, sisanya abu-abu
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

# Grafik produk terlaris
sns.barplot(
    x="quantity_x",
    y="product_name",
    data=sum_order_items_df.head(5),
    palette=colors,
    ax=ax[0]
)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Performing Product", loc="center", fontsize=18)
ax[0].tick_params(axis='y', labelsize=15)

# Grafik produk penjualan terendah
sns.barplot(
    x="quantity_x",
    y="product_name",
    data=sum_order_items_df.sort_values(by="quantity_x", ascending=True).head(5),
    palette=colors,
    ax=ax[1]
)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=18)
ax[1].tick_params(axis='y', labelsize=15)

# Tambahkan judul utama
fig.suptitle("Best and Worst Performing Product by Number of Sales", fontsize=20)

# Tampilkan di Streamlit
st.pyplot(fig)