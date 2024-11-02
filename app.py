import streamlit as st
import google.generativeai as genai


# un formulario, donde se ingresan las peliculas
# Estas peliculas son guardadas en una variable

st.title("Ingresar 3 películas")

pelicula1 = st.text_input("Nombre película 1")
pelicula2 = st.text_input("Nombre película 2")
pelicula3 = st.text_input("Nombre película 3")

mail = st.text_input("Ingrese correo donde recibira las recomendaciones")


# ------------------------------------------------ #

# API_KEY = "AIzaSyCLc0Gi3m6U-JgxTtu3dNgDB4N8NQ2XkPU"

# genai.configure(api_key=API_KEY)
# model = genai.GenerativeModel('gemini-1.5-flash')

# def corrector(pelicula):
#     response = model.generate_content(f"""Estrictamente, quiero que si {pelicula} esta mal escrita, solo me devuelvas el nombre de la película corregido""")
#     # st.write(response.text)
#     return response.text



if st.button("enviar"):
    st.write("Películas Ingresadas")

    # pelicula_1_corr = corrector(pelicula1)
    # pelicula_2_corr = corrector(pelicula2)
    # pelicula_3_corr = corrector(pelicula3)

    # st.write(corrector(pelicula_1_corr))
    # st.write(corrector(pelicula_2_corr))
    # st.write(corrector(pelicula_3_corr))

    st.write(pelicula1)
    st.write(pelicula2)
    st.write(pelicula3)





