import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Gráficos de Base de Datos de vehiculos de Estados Unidos') #Encabezado

st.write('Esta aplicación es un ejercicio académico')   #Texto

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
        
disp_button = st.button('Construir Diagrama de dispersión') # crear un botón

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un Diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)