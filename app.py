import streamlit as st
import google.generativeai as genai
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
# un formulario, donde se ingresan las peliculas
# Estas peliculas son guardadas en una variable

st.title("Ingresar 3 películas")

pelicula1 = st.text_input("Nombre película 1")
pelicula2 = st.text_input("Nombre película 2")
pelicula3 = st.text_input("Nombre película 3")

mail = st.text_input("Ingrese correo donde recibira las recomendaciones")


if st.button("enviar"):
    st.write("Películas Ingresadas")

    st.write(pelicula1)
    st.write(pelicula2)
    st.write(pelicula3)

    credentials_dict = st.secrets["gcp_service_account"]


    print(f"Agregando recomendaciones a excel")

    # Configuración para autenticación y acceso a Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", 
            "https://www.googleapis.com/auth/spreadsheets", 
            "https://www.googleapis.com/auth/drive.file", 
            "https://www.googleapis.com/auth/drive"]

    # credentials = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]))

    client = gspread.authorize(credentials_dict)

    # Abrir la hoja de cálculo usando su URL
    spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1T2H33PS-I0g0PhQyYblMrYcc8K3FSLbEkonV0VDYfwI/edit?usp=sharing'

    spreadsheet = client.open_by_url(spreadsheet_url)

    # --------------------------------------------------------- #
    worksheet_entrada = spreadsheet.worksheet("Nuevo Ingreso")

    pelicula_1 = pelicula1
    pelicula_2 = pelicula2
    pelicula_3 = pelicula3


    # Insertar datos en una nueva fila
    new_row = [mail, pelicula_1, pelicula_2, pelicula_3]
    worksheet_entrada.append_row(new_row)