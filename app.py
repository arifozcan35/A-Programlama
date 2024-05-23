import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px

def ucus_verilerini_al(kullanici_adi, sifre, lat_min, lon_min, lat_max, lon_max):
    url_veri = 'https://' + kullanici_adi + ':' + sifre + '@opensky-network.org/api/states/all?' \
               'lamin=' + str(lat_min) + '&lomin=' + str(lon_min) + '&lamax=' + str(lat_max) + '&lomax=' + str(lon_max)
    yanit = requests.get(url_veri).json()
    return yanit

def veri_isle(yanit):
    kolon_adi = ['icao24', 'Çağrı İşareti', 'Kaynak Ülke', 'Zaman Pozisyonu', 'Son Temas', 'Long', 'Lat', 'Baro İrtifası',
                'Yerde', 'Hız', 'Gerçek İz', 'Dikey Hız', 'Sensörler', 'Geo Yükseklik', 'Squawk', 'Spi',
                'Konum Kaynağı']
    ucus_df = pd.DataFrame(yanit['states'])
    ucus_df = ucus_df.loc[:, 0:16]
    ucus_df.columns = kolon_adi
    ucus_df = ucus_df.fillna('Veri Yok')
    
    # Hız sütununu sayısal formata dönüştür
    ucus_df['Hız'] = pd.to_numeric(ucus_df['Hız'], errors='coerce')
    
    # Eksik veya bozuk değerleri filtrele
    ucus_df = ucus_df.dropna(subset=['Hız'])
    
    return ucus_df

def ucus_verilerini_gorsellestir(ucus_df):
    fig = px.scatter_geo(ucus_df, lat='Lat', lon='Long', hover_name='Çağrı İşareti', 
                          color='Hız', size='Hız', 
                          color_continuous_scale='Rainbow',
                          # projection='natural earth', 
                          projection='orthographic', 
                          title='Uçuş Verileri',
                          opacity=0.7,
                          range_color=[0, 275],  # Hız aralığı
                          size_max=15,
                          labels={'Kaynak Ülke': 'Kaynak Ülke'},
                          custom_data=['Kaynak Ülke'],
                          animation_frame=None)     # Animasyonu devre dışı bırakmak
                          
                        
    fig.update_geos(showcountries=True)
    fig.update_layout(coloraxis_colorbar=dict(title="Hız (km/s)"),  # Renk skalası etiketi
                      geo=dict(
                          showframe=True,
                          framecolor="gray",
                          showcoastlines=True,
                          coastlinecolor="RebeccaPurple",
                          showland=True,
                          landcolor="rgb(217, 217, 217)",
                          showocean=True,
                          oceancolor="LightBlue",
                          showlakes=True,
                          lakecolor="Blue",
                          showcountries=True,
                          countrycolor="black",
                          showsubunits=True,
                          subunitcolor="red"
                      ),
                      width=800,  # Genişlik
                      height=600,  # Yükseklik
                      margin=dict(l=0, r=0, t=0, b=0))  # Kenar boşlukları
    
    fig.update_traces(hovertemplate='<b>Çağrı İşareti:</b> %{hovertext}<br><b>Hız:</b> %{marker.size} km/s<br><b>Kaynak Ülke:</b> %{customdata[0]}')
    return fig

@st.cache
def get_data(kullanici_adi, sifre, lat_min, lon_min, lat_max, lon_max):
    yanit = ucus_verilerini_al(kullanici_adi, sifre, lat_min, lon_min, lat_max, lon_max)
    ucus_df = veri_isle(yanit)
    return ucus_df

def main():
    st.title("Uçuş Verileri Görselleştirme")

    kullanici_adi = st.sidebar.text_input("Kullanıcı Adı")
    sifre = st.sidebar.text_input("Şifre", type="password")

    lat_min = st.sidebar.number_input("Minimum Latitude", value=-90.0)
    lon_min = st.sidebar.number_input("Minimum Longitude", value=-180.0)
    lat_max = st.sidebar.number_input("Maximum Latitude", value=90.0)
    lon_max = st.sidebar.number_input("Maximum Longitude", value=180.0)

    if kullanici_adi and sifre:
        ucus_df = get_data(kullanici_adi, sifre, lat_min, lon_min, lat_max, lon_max)
        st.write(ucus_df)

        fig = ucus_verilerini_gorsellestir(ucus_df)
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()




# streamlit run app.py