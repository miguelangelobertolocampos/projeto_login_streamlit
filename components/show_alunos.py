import streamlit as st
from controllers.alunos_controllers import load_alunos
from utils.cpf_utils import cpf_utils
from components.modal_visualizar import visualizar_aluno

def show_alunos():
    st.subheader("Lista de Alunos Cadastrados")

    alunos = load_alunos()

    if not alunos:
        return st.error("Nenhum aluno cadastrado! Clique no botão acima ")
    
    tabs = st.tabs(["Alunos", "Pesquisa"])

    with tabs[0]:
        colunas = st.columns([3, 2, 3, 2, 2])

        colunas[0].subheader("Nome")
        colunas[1].subheader("Email")
        colunas[2].subheader("CPF")
        colunas[3].subheader("Visualizar")
        colunas[4].subheader("Deletar")

        for aluno in alunos:
            colunas_aluno = st.columns([3, 3, 2, 2, 2])

            cpf_formatado = cpf_utils(aluno["cpf_aluno"])

            colunas_aluno[0].write(aluno["nome_aluno"])
            colunas_aluno[1].write(aluno["email_aluno"])
            colunas_aluno[2].write(cpf_utils)

            if colunas_aluno[3].button("Visualizar", key=f"view_{aluno["id_aluno"]}", use_container_width=True):
                visualizar_aluno(aluno) 

            if colunas_aluno[4].button("Deletar", key=f"deletar_{aluno["id_aluno"]}", use_container_width=True):
                pass 