import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Memuat dataset
bike_df = pd.read_csv('day.csv')
bike_df.season.replace((1, 2, 3, 4), ('spring', 'summer', 'fall', 'winter'), inplace=True)

# Judul utama
st.title('Bike Sharing Dashboard')

# Kolom untuk metrik
col1, col2 = st.columns(2)

with col1:
    total_rides = bike_df['cnt'].sum()
    st.metric('Jumlah pengguna sepeda', total_rides)

with col2:
    average_rides = bike_df['cnt'].mean()
    st.metric('Rata-rata pengguna sepeda', average_rides)

# Rata-rata pengguna sepeda per musim
bySeason_df = bike_df.groupby('season')['cnt'].mean().sort_values(ascending=False)
st.title('Bike Sharing Demand by Season')

plt.figure(figsize=(8, 6))
sns.barplot(
    x=bySeason_df.index,
    y=bySeason_df,
    palette='pastel'
)
plt.title("Rata-rata pengguna sepeda per musim", loc="center")
plt.ylabel("Rata-rata pengguna")
plt.xlabel("Musim")
st.pyplot(plt.gcf())
plt.clf()  # Membersihkan plot

# Rata-rata pengguna sepeda per bulan
byMonth_df = bike_df.groupby('mnth')['cnt'].mean().sort_values(ascending=False)
st.title('Bike Sharing Demand by Month')

plt.figure(figsize=(8, 6))
sns.barplot(
    x=byMonth_df.index,
    y=byMonth_df,
    palette='pastel'
)
plt.title("Rata-rata pengguna sepeda per bulan", loc="center")
plt.ylabel("Rata-rata pengguna")
plt.xlabel("Bulan")
st.pyplot(plt.gcf())
plt.clf()  # Membersihkan plot

# Rata-rata pengguna sepeda berdasarkan kecepatan angin
byWindspeed_df = bike_df.groupby('windspeed')['cnt'].mean().sort_values(ascending=False)
st.title('Bike Sharing Demand by Windspeed')

plt.figure(figsize=(8, 6))
plt.hist(byWindspeed_df, bins=10)
plt.title("Rata-rata pengguna sepeda berdasarkan kecepatan angin", loc="center")
plt.ylabel("Rata-rata pengguna")
plt.xlabel("Kecepatan angin")
st.pyplot(plt.gcf())
plt.clf()  # Membersihkan plot

# Sidebar
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

    # Menambahkan judul
    st.title("Bike Sharing Dashboard")

    # Menambahkan deskripsi
    st.write("Dashboard ini menampilkan rata-rata pengguna sepeda per musim.")
