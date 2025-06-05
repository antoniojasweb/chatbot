import os
import streamlit as st
from PIL import Image
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langdetect import detect

# Configuración de Streamlit
st.set_page_config(
    page_title="CHATBOT: Tu asistente Académico",
    page_icon="📄",
    initial_sidebar_state='collapsed',
    menu_items={
        'Get Help': 'https://www.noexiste.com',
        'Report a bug': None,
        'About': "CHATBOT es una herramienta para asistir sobre las información pública de un centro educativo. Permite realizar preguntas y obtener respuestas específicas de documentos pdf."
    }
)

# Carga y muestra el logo de la aplicación
logo = Image.open('logo.jpg')
st.image(logo, width=250)

# Título y descripción de la aplicación
st.title("CHATBOT: Tu asistente Académico")
st.write("""
    Con CHATBOT, puedes consultar tus dudas sin esperas.
    No más llamada telefónicas, ni visitas al centro, ni más lecturas aburridas o búsquedas tediosas.
    Haz preguntas directamente y obtén respuestas inmediatas gracias a la IA.
    """)

# Cargar PDF
pdf_obj = st.file_uploader(
    "Carga tu documento", type="pdf")

# Si no se ha cargado un PDF, no permitas que el usuario haga nada más
if not pdf_obj:
    st.stop()


# Principal
if pdf_obj:

    # Opciones de usuario
    st.sidebar.header('Opciones')
    options = [
        'Extraer texto',
        'Resumir texto',
        'Traducir texto',
    ]
    selected_option = st.sidebar.selectbox("¿Qué deseas hacer con el PDF?", options)

    # Preguntar
    if selected_option == ('Realizar preguntas'):
        st.header("Realizar preguntas")

        # Definir los prompts y sus descripciones
        prompts = [
            ("""Realiza un control de una consulta administrativa recibida por un posible alumno y/o tutor educativo en Extremadura (España).
Evalúa la peticíon basándote en los documentos oficiales del D.O.E, incluyendo competencia territorial, legitimidad del interesado, completitud y claridad de la solicitud, y su conformidad con los procedimientos y requisitos establecidos en el acuerdo. Presenta tu análisis en una tabla con las columnas 'Criterio', 'Descripción', 'Aplicación al Caso Hipotético', considerando si cada aspecto cumple o no con los requisitos, e incluye observaciones o recomendaciones pertinentes.
Asegúrate de verificar si la solicitud es jurídicamente correcta, si el solicitante tiene un interés legítimo, y si la solicitud es completa y clara.
            """,)
        ]

        # Crear botones para los prompts con descripciones emergentes
        for index, (prompt, label, description) in enumerate(prompts):
            # Decide en qué columna colocar el botón basándose en su índice
            col = st.columns(2)[index % 1]
            with col:
                if st.button(label, help=description):
                    st.session_state['selected_prompt'] = prompt

        # Mostrar el área de texto con el prompt seleccionado o el ingresado por el usuario
        user_question = st.text_area(
            "Haz una pregunta sobre tu PDF:",
            value=st.session_state.get('selected_prompt', ''),
            height=150
        )

        if user_question:
            #....
            st.write(respuesta)
    else:
        st.info("Esta opción se implementará próximamente")

    # Footer / Pie de página
    st.sidebar.markdown('---')
    st.sidebar.subheader('Creado por:')
    st.sidebar.markdown('Antonio Jesús Abasolo Sierra')
    st.sidebar.markdown('Jose David Honrado García')
    )
