import streamlit as st
import google.generativeai as genai
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
# un formulario, donde se ingresan las peliculas
# Estas peliculas son guardadas en una variable


st.image("Imagenes/WEEKLUXE.jpg", width=300)

st.write("""
        Somos WeekLuxe, tu guía para exploradores del cine alternativo.
         Cada semana te ofrecemos una selección curada de películas que probablemente no encontrarás fácilmente en las plataformas comunes.""")

st.title("Ingresar 3 películas")

with st.form("formulario", clear_on_submit = True):
    pelicula1 = st.text_input("Nombre película 1", key="p1")
    pelicula2 = st.text_input("Nombre película 2", key="p2")
    pelicula3 = st.text_input("Nombre película 3", key="p3")
    mail = st.text_input("Ingrese correo", key="email")
    
    enviado = st.form_submit_button("Enviar")

if enviado:
    st.write("Solicitud enviada: GRACIAS POR CONFIAR EN WEEKLUXE, BUEN DIA")

credentials_dict = st.secrets["gcp_service_account"]

scope = ["https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)

client = gspread.authorize(credentials)

spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1T2H33PS-I0g0PhQyYblMrYcc8K3FSLbEkonV0VDYfwI/edit?usp=sharing'

spreadsheet = client.open_by_url(spreadsheet_url)

# --------------------------------------------------------- #
worksheet_entrada = spreadsheet.worksheet("Entradas - ST")

pelicula_1 = pelicula1
pelicula_2 = pelicula2
pelicula_3 = pelicula3

new_row = [pelicula_1, pelicula_2, pelicula_3, mail]
worksheet_entrada.append_row(new_row)