import streamlit as st
import requests

st.title("Cadastro de Produtos")

with st.form("new_product"):
    st.write("Adicionar um novo produto")
    name = st.text_input("Nome do Produto")
    description = st.text_area("Descrição do Produto")
    price = st.number_input("Preço", min_value=0.00, format="%f")
    categoria = st.selectbox(
        "Categoria", ["Eletrônico", "Eletrodoméstico", "Móveis", "Roupas", "Calçados"]
    )
    email_fornecedor = st.text_input("Email do Fornecedor")
    submit_button = st.form_submit_button("Adicionar Produto")

    if submit_button:
        response = requests.post(
            "http://localhost:8000/products/",
            json={
                "name": name,
                "description": description,
                "price": price,
                "categoria": categoria,
                "email_fornecedor": email_fornecedor,
            },
        )
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o produto")

# Botão para exibir produtos existentes
if st.button("Exibir Todos os Produtos"):
    response = requests.get("http://localhost:8000/products/")
    if response.status_code == 200:
        products = response.json()
        for product in products:
            st.write(
                f"ID: {product['id']}, Nome: {product['name']}, Descrição: {product['description']}, Preço: {product['price']}, Categoria: {product['categoria']}, Email do Fornecedor: {product['email_fornecedor']}, Criado em: {product['created_at']}"
            )
    else:
        st.error("Erro ao buscar os produtos")

# Botão para obter um produto específico
get_button = st.button("Obter Detalhes de um Produto")
if get_button:
    get_id = st.number_input("ID do Produto para Obter", min_value=1, format="%d")
    response = requests.get(f"http://localhost:8000/products/{get_id}")
    if response.status_code == 200:
        product = response.json()
        st.write(f"Detalhes do Produto: {product}")
    else:
        st.error("Produto não encontrado")

# Botão para deletar um produto
delete_button = st.button("Deletar um Produto")
if delete_button:
    delete_id = st.number_input("ID do Produto para Deletar", min_value=1, format="%d")
    response = requests.delete(f"http://localhost:8000/products/{delete_id}")
    if response.status_code == 200:
        st.success("Produto deletado com sucesso!")
    else:
        st.error("Erro ao deletar o produto")

with st.form("update_product"):
    st.write("Atualizar um produto existente")
    update_id = st.number_input("ID do Produto", min_value=1, format="%d")
    new_name = st.text_input("Novo Nome do Produto")
    new_description = st.text_area("Nova Descrição do Produto")
    new_price = st.number_input("Novo Preço", min_value=0.00, format="%f")
    new_email = st.text_input("Novo Email do Fornecedor")
    update_button = st.form_submit_button("Atualizar Produto")

    if update_button:
        update_data = {}
        if new_name:  # Verifica se o campo não está vazio
            update_data["name"] = new_name
        if new_description:  # Verifica se o campo não está vazio
            update_data["description"] = new_description
        if new_price > 0:  # Verifica se o preço é maior que 0
            update_data["price"] = new_price
        if new_email:  # Verifica se o campo não está vazio
            update_data["email_fornecedor"] = new_email

        if update_data:  # Se houver dados para atualizar
            response = requests.put(
                f"http://localhost:8000/products/{update_id}", json=update_data
            )
            if response.status_code == 200:
                st.success("Produto atualizado com sucesso!")
            else:
                st.error("Erro ao atualizar o produto")
        else:
            st.error("Nenhuma informação fornecida para atualização")
