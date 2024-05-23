import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

country_coordinates = {
    'Algeria': {'lat': 36.7372, 'lon': 3.0860},
    'Argentina': {'lat': -34.6118, 'lon': -58.4173},
    'Australia': {'lat': -35.2820, 'lon': 149.1286},
    'Austria': {'lat': 48.2082, 'lon': 16.3738},
    'Azerbaijan': {'lat': 40.4093, 'lon': 49.8671},
    'Bangladesh': {'lat': 23.8103, 'lon': 90.4125},
    'Belarus': {'lat': 53.9045, 'lon': 27.5615},
    'Belgium': {'lat': 50.8503, 'lon': 4.3517},
    'Bhutan': {'lat': 27.4728, 'lon': 89.6393},
    'Bolivia': {'lat': -16.5000, 'lon': -68.1500},
    'Bosnia and Herzegovina': {'lat': 43.8563, 'lon': 18.4131},
    'Brazil': {'lat': -15.7939, 'lon': -47.8828},
    'Bulgaria': {'lat': 42.6977, 'lon': 23.3219},
    'Cameroon': {'lat': 3.8480, 'lon': 11.5021},
    'Canada': {'lat': 45.4215, 'lon': -75.6972},
    'Chile': {'lat': -33.4489, 'lon': -70.6693},
    'China': {'lat': 39.9042, 'lon': 116.4074},
    'Colombia': {'lat': 4.7110, 'lon': -74.0721},
    'Costa Rica': {'lat': 9.9281, 'lon': -84.0907},
    'Croatia': {'lat': 45.8150, 'lon': 15.9819},
    'Cuba': {'lat': 23.1136, 'lon': -82.3666},
    'Cyprus': {'lat': 35.1856, 'lon': 33.3823},
    'Czech Republic': {'lat': 50.0755, 'lon': 14.4378},
    'Denmark': {'lat': 55.6761, 'lon': 12.5683},
    'Dominican Republic': {'lat': 18.4861, 'lon': -69.9312},
    'Ecuador': {'lat': -0.1807, 'lon': -78.4678},
    'Egypt': {'lat': 30.0444, 'lon': 31.2357},
    'Estonia': {'lat': 59.4370, 'lon': 24.7535},
    'Ethiopia': {'lat': 9.0300, 'lon': 38.7400},
    'Finland': {'lat': 60.1695, 'lon': 24.9354},
    'France': {'lat': 48.8566, 'lon': 2.3522},
    'Germany': {'lat': 52.5200, 'lon': 13.4050},
    'Greece': {'lat': 37.9838, 'lon': 23.7275},
    'Hungary': {'lat': 47.4979, 'lon': 19.0402},
    'Iceland': {'lat': 64.1355, 'lon': -21.8954},
    'India': {'lat': 28.6139, 'lon': 77.2090},
    'Indonesia': {'lat': -6.2088, 'lon': 106.8456},
    'Iran': {'lat': 35.6892, 'lon': 51.3890},
    'Iraq': {'lat': 33.3152, 'lon': 44.3661},
    'Ireland': {'lat': 53.3498, 'lon': -6.2603},
    'Israel': {'lat': 31.7683, 'lon': 35.2137},
    'Italy': {'lat': 41.9028, 'lon': 12.4964},
    'Jamaica': {'lat': 18.1096, 'lon': -77.2975},
    'Japan': {'lat': 35.6895, 'lon': 139.6917},
    'Jordan': {'lat': 31.9539, 'lon': 35.9106},
    'Kazakhstan': {'lat': 51.1694, 'lon': 71.4491},
    'Kenya': {'lat': -1.2921, 'lon': 36.8219},
    'Korea, North': {'lat': 39.0392, 'lon': 125.7625},
    'Korea, South': {'lat': 37.5665, 'lon': 126.9780},
    'Kosovo': {'lat': 42.6026, 'lon': 20.9030},
    'Kuwait': {'lat': 29.3759, 'lon': 47.9774},
    'Kyrgyzstan': {'lat': 42.8746, 'lon': 74.5698},
    'Lebanon': {'lat': 33.8938, 'lon': 35.5018},
    'Libya': {'lat': 32.8872, 'lon': 13.1913},
    'Malaysia': {'lat': 3.1390, 'lon': 101.6869},
    'Malta': {'lat': 35.8989, 'lon': 14.5146},
    'Mexico': {'lat': 19.4326, 'lon': -99.1332},
    'Moldova': {'lat': 47.0104, 'lon': 28.8638},
    'Monaco': {'lat': 43.7384, 'lon': 7.4246},
    'Montenegro': {'lat': 42.7087, 'lon': 19.3744},
    'Morocco': {'lat': 31.7917, 'lon': -7.0926},
    'Myanmar': {'lat': 19.7608, 'lon': 96.0785},
    'Nepal': {'lat': 27.7172, 'lon': 85.3240},
    'Netherlands': {'lat': 52.3676, 'lon': 4.9041},
    'New Zealand': {'lat': -41.2865, 'lon': 174.7762},
    'North Macedonia': {'lat': 41.9973, 'lon': 21.4280},
    'Norway': {'lat': 59.9139, 'lon': 10.7522},
    'Oman': {'lat': 23.6140, 'lon': 58.5922},
    'Pakistan': {'lat': 33.6844, 'lon': 73.0479},
    'Palestine': {'lat': 31.9522, 'lon': 35.2332},
    'Panama': {'lat': 8.9824, 'lon': -79.5199},
    'Paraguay': {'lat': -25.2637, 'lon': -57.5759},
    'Peru': {'lat': -12.0464, 'lon': -77.0428},
    'Philippines': {'lat': 14.5995, 'lon': 120.9842},
    'Poland': {'lat': 52.2297, 'lon': 21.0122},
    'Portugal': {'lat': 38.7223, 'lon': -9.1393},
    'Qatar': {'lat': 25.2854, 'lon': 51.5310},
    'Romania': {'lat': 44.4268, 'lon': 26.1025},
    'Russia': {'lat': 55.7558, 'lon': 37.6176},
    'Saudi Arabia': {'lat': 24.7136, 'lon': 46.6753},
    'Senegal': {'lat': 14.7167, 'lon': -17.4677},
    'Serbia': {'lat': 44.7866, 'lon': 20.4489},
    'Singapore': {'lat': 1.3521, 'lon': 103.8198},
    'Slovakia': {'lat': 48.1486, 'lon': 17.1077},
    'Slovenia': {'lat': 46.0569, 'lon': 14.5058},
    'South Africa': {'lat': -25.7460, 'lon': 28.1881},
    'Spain': {'lat': 40.4168, 'lon': -3.7038},
    'Sri Lanka': {'lat': 6.9271, 'lon': 79.8612},
    'Sweden': {'lat': 59.3293, 'lon': 18.0686},
    'Switzerland': {'lat': 46.9480, 'lon': 7.4481},
    'Tajikistan': {'lat': 38.5517, 'lon': 68.7738},
    'Thailand': {'lat': 13.7563, 'lon': 100.5018},
    'Tunisia': {'lat': 36.8065, 'lon': 10.1815},
    'Turkey': {'lat': 39.9334, 'lon': 32.8597},
    'Turkmenistan': {'lat': 37.9601, 'lon': 58.3261},
    'Uganda': {'lat': 0.3476, 'lon': 32.5825},
    'Ukraine': {'lat': 50.4501, 'lon': 30.5234},
    'United Arab Emirates': {'lat': 24.4539, 'lon': 54.3773},
    'United Kingdom': {'lat': 51.5074, 'lon': -0.1278},
    'United States': {'lat': 38.8951, 'lon': -77.0364},
    'Uruguay': {'lat': -34.9011, 'lon': -56.1645},
    'Uzbekistan': {'lat': 41.3775, 'lon': 64.5853},
    'Vatican City': {'lat': 41.9029, 'lon': 12.4534},
    'Venezuela': {'lat': 10.4806, 'lon': -66.9036},
    'Vietnam': {'lat': 21.0285, 'lon': 105.8544},
    'Yemen': {'lat': 15.5527, 'lon': 48.5164},
              
}


def veri_isle(ucus_df):
    kolon_adi = ['id', 'icao24', 'Çağrı İşareti', 'Kaynak Ülke', 'Zaman Pozisyonu', 'Son Temas', 'Long', 'Lat', 'Baro İrtifası',
                'Yerde', 'Hız', 'Gerçek İz', 'Dikey Hız', 'Sensörler', 'Geo Yükseklik', 'Squawk', 'Spi',
                'Konum Kaynağı']
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


# Uçak rotalarını çizme
def ucak_rotalarini_ciz(ucus_df, country_coordinates):
    fig = go.Figure()

    for index, row in ucus_df.iterrows():
        # Uçağın kaynak ülke ve mevcut konumunu al
        kaynak_ulke = row['Kaynak Ülke']
        mevcut_konum = (row['Lat'], row['Long'])

        # Kaynak ülkenin koordinatlarını al
        if kaynak_ulke in country_coordinates:
            kaynak_koordinatlar = (country_coordinates[kaynak_ulke]['lat'], country_coordinates[kaynak_ulke]['lon'])

            # Rotayı çiz
            fig.add_trace(go.Scattergeo(
                locationmode = 'country names',
                lon = [kaynak_koordinatlar[1], mevcut_konum[1]],
                lat = [kaynak_koordinatlar[0], mevcut_konum[0]],
                mode = 'lines',
                line = dict(width = 1, color = 'red'),  # Çizgi kalınlığı ve renk
                opacity = 0.5,
                hoverinfo = 'none'
            ))

            # Uçak simülasyonunu ekle
            fig.add_trace(go.Scattergeo(
                locationmode = 'country names',
                lon = [mevcut_konum[1]],
                lat = [mevcut_konum[0]],
                mode = 'markers',
                marker = dict(
                    size = 3,
                    color = 'black',
                    opacity = 0.7
                ),
                hoverinfo = 'text',
                text = f'Uçak ID: {row["id"]} <br> Çağrı İşareti: {row["Çağrı İşareti"]} <br> Hız: {row["Hız"]} km/s'
            ))

    # Harita stilini ve boyutunu ayarla
    fig.update_geos(
        projection_type="orthographic",
        showland=True, landcolor="rgb(243, 243, 243)",
        showocean=True, oceancolor="LightBlue",
        showcountries=True,
        showframe=False,
        showcoastlines=True,
        showlakes=True,
        lakecolor="LightBlue",
        showrivers=True,
        rivercolor="Blue",
        showsubunits=True,
        subunitcolor="rgb(217, 217, 217)",
        lonaxis=dict(
            showgrid=True,
            gridcolor='rgb(102, 102, 102)',
            gridwidth=0.5
        ),
        lataxis=dict(
            showgrid=True,
            gridcolor='rgb(102, 102, 102)',
            gridwidth=0.5
        )
    )

    # Harita düzenini ayarla
    fig.update_layout(
        title = 'Uçak Rotaları',
        geo = dict(
            scope='world',
            showland = True,
            landcolor = "rgb(212, 212, 212)",
            showcountries=True,
            showframe=False,
            showcoastlines=True,
            coastlinecolor="RebeccaPurple",
            projection_type='orthographic'
        ),
        width=800, height=600
    )

    return fig


@st.cache
def get_data(csv_file_path):
    ucus_df = pd.read_csv(csv_file_path)
    ucus_df = veri_isle(ucus_df)
    return ucus_df

def main():
    st.title("Uçuş Verileri Görselleştirme")

    csv_file_path = st.sidebar.text_input("CSV Dosya Yolu", value="tum_dunya.csv")

    if csv_file_path:
        ucus_df = get_data(csv_file_path)
        st.write(ucus_df)

        fig1 = ucus_verilerini_gorsellestir(ucus_df)
        st.plotly_chart(fig1)

        fig2 = ucak_rotalarini_ciz(ucus_df, country_coordinates)
        st.plotly_chart(fig2)

if __name__ == "__main__":
    main()



# streamlit run app.py