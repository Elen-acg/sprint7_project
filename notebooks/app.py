import pandas as pd
import plotly.express as px
import streamlit as st

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# header primera sección
st.header('Mostrar Histograma')

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón

    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

# header segunda sección
st.header('Mostrar gráfico de dispersión')

build_dispersion = st.checkbox('Construir gráfico de dispersión')

if build_dispersion: # si la casilla de verificación está seleccionada

    #escribir un mensaje
    st.write('Construir un gráfico de dispersión para la columna precio')
    
    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price") 

    #mostrar gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)
