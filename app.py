import streamlit as st

st.title("Meu Primeiro App no Streamlit 🎉")
st.write("Este app foi criado no GitHub Codespaces!")

nome = st.text_input("Qual é o seu nome?")
if nome:
    st.success(f"Prazer em conhecer você, {nome}!")
