import streamlit as st
import google.generativeai as genai


# un formulario, donde se ingresan las peliculas
# Estas peliculas son guardadas en una variable

peliculas_populares = [
    "El Padrino",
    "El Señor de los Anillos",
    "La Lista de Schindler",
    "El Resplandor",
    "Pulp Fiction",
    "La Vida es Bella",
    "El Club de la Lucha",
    "Forrest Gump",
    "La Paradoja del Viajero",
    "12 Hombres en Pugna"
]

# Crear el formulario para seleccionar las películas
with st.form("formulario_peliculas"):
    st.write("Seleccione 3 películas")
    pelicula1 = st.selectbox("Pelicula 1", peliculas_populares)
    pelicula2 = st.selectbox("Pelicula 2", peliculas_populares)
    pelicula3 = st.selectbox("Pelicula 3", peliculas_populares)
    # Botón para enviar el formulario
    submitted = st.form_submit_button("Enviar")

if submitted:
    st.write(f'''
            El usuario ingreso estas 3 peliculas \n
            Pelicula 1: {pelicula1} \n
            Pelicula 2: {pelicula2} \n
            Pelicula 3: {pelicula3}        ''')


    # La parte de gimini

    API_KEY = "AIzaSyCLc0Gi3m6U-JgxTtu3dNgDB4N8NQ2XkPU"

    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(f"Quiero hasta 3 recomendaciones de pelicula en base a estas 3 peliculas {pelicula1},{pelicula2},{pelicula3}")
    st.write(response.text)