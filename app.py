import streamlit as st

# Definir titulo
st.title('Evento | Dashboard com Python')

# Cabeçalho
st.header('Conhecendo os elementos do Streamlit')

# Subtitulo
st.subheader('Aula 2 [2/5]')

# Texto Simples
st.text('Nesta aula vamos entender os elementos do Streamlit')

# Texto formatado
st.markdown('# Streamlit')

# Texto
st.write('Streamlit é um frameworl de alto nível do python!')

# Botão com validação - Combinando Streamlit com Python
if st.button('Clique aqui'):
    
    for Loop in range(5):
        st.write(f'Botão selecionado! {Loop}')

# Radio - Selecionar
Escolha = st.radio('Qual linguagem de programação você mais utiliza', ('Python', 'R', 'Java', 'Outro'))

# Seleção de caixa
Lista_Frameworks = ['Matplotlib', 'Seaborn', 'Plotly']
Opcao = st.selectbox('Escolha seu framework favorito de Data Vizualization: ', Lista_Frameworks)

# Seleção de multiplas caixas
Lista_Estudo = ['Pandas', 'Numpy', 'Matplotlib', 'Seaborn', 'Plotly', 'Scipy', 'TensorFlow']
Selecoes = st.multiselect('Escolha as opções:', Lista_Estudo)

# Seletor deslizante , Começa no 0, Termina no 30, Anda de 1 em 1
Valor = st.slider('Quantos anos trabalha com Data Science? ', 0, 30, 1)

# Upload de arquivos
Arquivo = st.file_uploader('Escolha um arquivo', type=['csv', 'txt'])

# Imagem
st.image('foto_perfil.jpg', caption='Descrição da imagem', use_column_width=True)

import pandas as pd
import numpy as np

# Tabela
# Dataframe 
df = pd.DataFrame(
    {
        'Dias':[loop for loop in range(31)]
    }
)

# Adicionando novas colunas com dados fictícios
df['Valor de Venda'] = np.random.randint(100, 1000, size=31)
df['Custo'] = df['Valor de Venda'] * 0.8
df['Lucro'] = df['Valor de Venda'] - df['Custo']
df['Quantidade Vendida'] = np.random.randint(10, 50, size=31)
df['Cliente'] = ['Cliente' + str(i) for i in range(1, 32)]

# Incluir tabela
st.dataframe( df )

import altair as alt

# Gráfico com altair - linha
chart = alt.Chart(df).mark_line().encode(
    x='Dias',
    y='Valor de Venda'
)

# Exibir 
st.altair_chart(chart)