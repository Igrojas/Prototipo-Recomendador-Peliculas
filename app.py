import streamlit as st
import google.generativeai as genai


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





