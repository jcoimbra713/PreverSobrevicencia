import pickle
import streamlit as st
import numpy as np

# Carregando a Máquina Preditiva
pickle_in = open('Maquina_PreditivaCancer.pkl', 'rb') 
Maquina_PreditivaCancer = pickle.load(pickle_in)

# Essa função é para criação da página web
def main():  
    # Elementos da página web
    # Nesse ponto, você deve personalizar o sistema com sua marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">PROJETO PARA PREVER SOBREVIVÊNCIA DE CÂNCER</h1> 
    <h2 style ="color:white;text-align:center;">SISTEMA PARA PREVER SOBREVIVÊNCIA DE CÂNCER - by João Coimbra </h2> 
    </div> 
    """
      
    # Função do Streamlit que faz o display da página web
    st.markdown(html_temp, unsafe_allow_html=True) 
      
    # As linhas abaixo criam as caixas nas quais o usuário vai inserir os dados da pessoa que deseja prever o diabetes
    Age = st.number_input("Idade")
    TamanhoTumor = st.number_input("Tamanho Do Tumor")
    StatusEstrogênio = st.selectbox('Estrogênio', ("Sim", "Não "))
    StatusProgesterona = st.selectbox('Progesterona', ("Sim", "Não"))
    NoduloRegionalExaminado = st.number_input("Número Do Nodulo Regional Examinado")
    NoduloReginolPositivo = st.number_input("Número Do Nodulo Reginol Positivo") 
    MesesHospital = st.number_input("Quantidade De Dias Internado")
      
    # Quando o usuário clicar no botão "Verificar", a Máquina Preditiva fará seu trabalho
    if st.button("Verificar"): 
        result, probabilidade = prediction(Age, TamanhoTumor, StatusEstrogênio, StatusProgesterona, NoduloRegionalExaminado, NoduloReginolPositivo, MesesHospital) 
        st.success(f'Resultado: {result}')
        st.write(f'Probabilidade: {probabilidade}')

# Essa função faz a predição usando os dados inseridos pelo usuário
def prediction(Age, TamanhoTumor, StatusEstrogênio, StatusProgesterona, NoduloRegionalExaminado, NoduloReginolPositivo, MesesHospital):   
    # Pre-processando a entrada do Usuário    
    if StatusEstrogênio == "Estrogênio":
        StatusEstrogênio = 0
    else:
        StatusEstrogênio = 1
 
    if StatusProgesterona == "Progesterona":
        StatusProgesterona = 0
    else:
        StatusProgesterona = 1


    # Fazendo a Predição
    parametro = np.array([[Age, TamanhoTumor, StatusEstrogênio, StatusProgesterona, NoduloRegionalExaminado, NoduloReginolPositivo, MesesHospital]])
    fazendo_previsao = Maquina_PreditivaCancer.predict(parametro)
    probabilidade = Maquina_PreditivaCancer.predict_proba(parametro)
   
   
    if (fazendo_previsao == 1).any():
        pred = 'NÃO TEM PROBABILIDADE DE MORRER'

    else:
        pred = 'TEM PROBABILIDADE DE MORRERE'

    
    return pred, probabilidade

if __name__ == '__main__':
    main()