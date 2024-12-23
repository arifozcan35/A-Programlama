# Flight Data Visualization Project

This project is a web application that visualizes flight data dynamically and statically using the OpenSky Network API and static data files. It aims to interactively display the speed, routes, and positions of aircraft on a world map.

![Ekran Görüntüsü (2195)](https://github.com/user-attachments/assets/e63c6540-bcf8-4975-a162-68c80c02d238)


![Ekran Görüntüsü (2196)](https://github.com/user-attachments/assets/21386c97-2f44-426c-9604-ca0b4e06cbdb)


![Ekran Görüntüsü (2198)](https://github.com/user-attachments/assets/7ea417c3-fab2-45a8-bef6-01d723450ad8)


## Features

- *Dynamic Data Usage:*
  - Real-time flight data is retrieved from the OpenSky Network API.
  - Aircraft position and speed information are visualized within user-defined geographic boundaries.

- *Static Data Usage:*
  - A data file containing 4500 flight records in CSV format is utilized.
  - Flight speeds are displayed on a world map with a colored scale.
  - Routes between the source country and the current positions of aircraft are drawn.

- *Interactive Maps:*
  - Colored and sized markers representing aircraft speeds.
  - Lines showing the source country and flight routes.
  - Hover functionality to display additional information such as aircraft ID, speed, and source country.

- *User-Friendly Interface:*
  - A simple web application built with Streamlit.
  - Features include API username and password input and geographic boundary adjustments.

---

## Technologies and Libraries Used

### Programming Language:
- *Python*

### Framework and Libraries:
1. **[Streamlit](https://streamlit.io/):**
   - For building the user interface and web application.
2. **[Requests](https://pypi.org/project/requests/):**
   - To fetch flight data via HTTP requests.
3. **[Pandas](https://pandas.pydata.org/):**
   - For data processing and manipulation.
4. **[Plotly](https://plotly.com/):**
   - For interactive maps and visualizations.
   - Using plotly.express and plotly.graph_objects modules.
5. **[OpenSky Network API](https://opensky-network.org/):**
   - For providing real-time flight data.

### Other:
- *Orthographic Map Projection:*
  - To display the world map with a global view.
- *CSV Data Processing:*
  - For processing static flight data.

---

## Installation and Use

### 1. Requirements
- Python version 3.8+.
- `pip` package manager.

### 2. Installation of Required Libraries
Install the necessary libraries with the following command:
```bash
pip install streamlit pandas plotly requests
```

### 3. Running the Project
1. **`app.py` File (Dynamic Data):**
   - Enter your OpenSky Network API username and password.
   - Start the application with the following command:
     ```bash
     streamlit run app.py
     ```

2. **`app2.py` File (Static Data):**
   - Visualises flight data using a static data file (`tum_dunya.csv`).
   - Start the application with the following command:
     ```bash
     streamlit run app2.py
     ```

---


## Project Structure

```
.
├── app.py              # Application using dynamic data (API)
├── app2.py             # Application using static data (CSV)
├─── tum_dunya.csv      # Static data file
└── README.md           # Project description file
```

---


## Example Data

### **`tum_dunya.csv` Example of Content:**
```csv
,id,icao24,Çağrı İşareti,Kaynak Ülke,Zaman Pozisyonu,Son Temas,Long,Lat,Baro İrtifası,Yerde,Hız,Gerçek İz,Dikey Hız,Sensörler,Geo Yükseklik,Squawk,Spi,Konum Kaynağı
0,7c35e7,KXL     ,Australia,1714025360,1714025360,150.8523,-31.0833,396.24,false,53.5,313.05,-0.98,Veri Yok,441.96,4405,false,0
1,88044a,AIQ377  ,Thailand,1714025411,1714025411,102.2897,2.7496,9966.96,false,240.47,321.34,3.25,Veri Yok,10668.0,Veri Yok,false,0
2,88044f,AIQ3230 ,Thailand,1714025383,1714025383,100.6092,13.9266,Veri Yok,true,0,118.12,Veri Yok,Veri Yok,Veri Yok,Veri Yok,false,0
```

---


## Images

1. **Map of Aircraft Speeds:**
   - Colour scale representation of speeds on the world map.
2. **Map of Aircraft Routes:**
   - Routes between the source country and the current positions of the aircraft.

---

## Contribution
If you would like to contribute to the project, please send a **pull request** or contact us by opening a **issue**.

---

**Developers:**  

- **[Arif Özcan](https://github.com/arifozcan35)**
- **[Furkan Tasan](https://github.com/Furkantsnb)** 
