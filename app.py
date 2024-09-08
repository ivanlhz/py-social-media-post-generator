"""Hugging face and LL POst generation"""

import streamlit as st
from ai_application import title_chain,post_chain,keywords_chain

st.header('Asistente IA de contenido para Threads...🤖🫣')
st.subheader('Crea contenido para Threads sin romperte la cabeza')

# Title generation
st.subheader('Título del post')
topic_header = st.expander('A partir de un tema crearemos 10 titulos')

with topic_header:
    topic_name = st.text_input('Escribe el tema', key='topic_name')
    button_topic = st.button('Generar titulos')

    if button_topic:
        st.write(title_chain.invoke({topic_name}))


# Blog generation
st.subheader('Contenido de los posts')
post_header = st.expander('Rellena los siguientes campos para generar un artículo adaptado a tus necesidades')

keywords = ''
with post_header:
    title_name = st.text_input('Pega aqui el titulo que quieras para tu post', key='title_name')
    num_of_posts = st.slider('Numero post a generar', min_value=1, max_value=10, step=1)
    button_keywords = st.button('Generar palabras clave')
    button_generate = st.button('Generar articulo')

if button_keywords:
    keywords = keywords_chain.invoke({'topic': title_name, 'num_of_keywords': 5})
    st.write(keywords)

if button_generate:
    st.write(post_chain.invoke({'title': title_name, 'keywords': keywords, 'number_of_posts': num_of_posts}))
