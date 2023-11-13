import streamlit as st
import requests

st.title("Cadastro de Produtos")

# Formulário para adicionar um novo produto
with st.form("new_product"):
    st.write("Adicionar um novo produto")
    name = st.text_input("Nome do Produto")
    description = st.text_area("Descrição do Produto")
    price = st.number_input("Preço", min_value=0.00, format="%f")
    submit_button = st.form_submit_button("Adicionar Produto")

    if submit_button:
        response = requests.post(
            "http://localhost:8000/products/",
            json={"name": name, "description": description, "price": price},
        )
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o produto")

# Exibir produtos existentes
st.write("Produtos Existentes")
response = requests.get("http://localhost:8000/products/")
if response.status_code == 200:
    products = response.json()
    for product in products:
        st.write(
            f"ID: {product['id']}, Nome: {product['name']}, Descrição: {product['description']}, Preço: {product['price']}"
        )
