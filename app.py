import streamlit as st
import google.generativeai as genai
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
# un formulario, donde se ingresan las peliculas
# Estas peliculas son guardadas en una variable


st.image("Imagenes/WEEKLUXE.jpg", width=400)
st.title("Ingresar 3 películas")

pelicula1 = st.text_input("Nombre película 1")
pelicula2 = st.text_input("Nombre película 2")
pelicula3 = st.text_input("Nombre película 3")

mail = st.text_input("Ingrese correo donde recibirá las recomendaciones")


if st.button("enviar"):
    st.write("Películas Ingresadas")

    st.write(pelicula1)
    st.write(pelicula2)
    st.write(pelicula3)

    # Obtén el diccionario de credenciales desde Streamlit secrets
    credentials_dict = st.secrets["gcp_service_account"]

    # Define el alcance
    scope = ["https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"]

    # Crea las credenciales utilizando el diccionario y el alcance
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)

    # Autenticación con gspread usando las credenciales
    client = gspread.authorize(credentials)

    # Abrir la hoja de cálculo usando su URL
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1T2H33PS-I0g0PhQyYblMrYcc8K3FSLbEkonV0VDYfwI/edit?usp=sharing'

    spreadsheet = client.open_by_url(spreadsheet_url)

    # --------------------------------------------------------- #
    worksheet_entrada = spreadsheet.worksheet("Entradas - ST")

    pelicula_1 = pelicula1
    pelicula_2 = pelicula2
    pelicula_3 = pelicula3


    # Insertar datos en una nueva fila
    new_row = [pelicula_1, pelicula_2, pelicula_3, mail]
    worksheet_entrada.append_row(new_row)