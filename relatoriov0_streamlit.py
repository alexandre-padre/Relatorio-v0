#!/usr/bin/env python
# coding: utf-8

# In[46]:


# imports e definições
import pandas as pd
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta
import streamlit as st
import math
from PIL import Image
import plotly.express as px


# In[47]:


st.image('[LOGO] Eduqo.png')

st.title('Relatório de uso da plataforma QMágico')

image = Image.open('[LOGO] Eduqo.png')
st.sidebar.image(image,caption='Eduqo - Plataforma QMágico',use_column_width=True)

st.sidebar.markdown('Feito por : Alexandre Fernandes (Padre)')


# In[48]:


st.subheader('**Capítulo 1**')


# In[49]:


st.subheader('**Capítulo 2: Dados brutos acerca do tempo gasto pelos usuários ativos na plataforma**')


# In[50]:


st.markdown('**Tópico 2.1: Alunos**')

alunos_tempo_uniao2 = pd.read_excel('alunos_tempo_uniao2.xlsx')

fig1 = px.bar(alunos_tempo_uniao2, x='Dia', y='Horas por aluno')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de alunos por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por aluno')
st.plotly_chart(fig1)


# In[51]:


st.markdown('**Tópico 2.2: Professores**')

professores_tempo_uniao2 = pd.read_excel('professores_tempo_uniao2.xlsx')

fig1 = px.bar(professores_tempo_uniao2, x='Dia', y='Horas por professor')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de professores por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por professores')
st.plotly_chart(fig1)


# In[52]:


st.markdown('**Tópico 2.3: Administradores**')

admin_tempo_uniao2 = pd.read_excel('admin_tempo_uniao2.xlsx')

fig1 = px.bar(admin_tempo_uniao2, x='Dia', y='Horas por administrador')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de administradores por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por administradores')
st.plotly_chart(fig1)


# In[53]:


st.subheader('**Capítulo 3: Dados brutos acerca do Banco de Questões Eduqo (Produto Banqo)**')


# In[54]:


st.markdown('**Tópico 3.1: Número de questões**')

questoes_estante_n_questoes2 = pd.read_excel('questoes_estante_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[55]:


st.markdown('**Tópico 3.2: Número de questões EM**')

questoes_estante_em_n_questoes2 = pd.read_excel('questoes_estante_em_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_em_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Médio no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[56]:


st.markdown('**Tópico 3.3: Número de questões EF2**')

questoes_estante_ef2_n_questoes2 = pd.read_excel('questoes_estante_ef2_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_ef2_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Fundamental II no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[57]:


st.markdown('**Tópico 3.4: Número de questões EF1**')

questoes_estante_ef1_n_questoes2 = pd.read_excel('questoes_estante_ef1_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_ef1_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Fundamental I no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[58]:


st.markdown('**Tópico 3.5: Número de questões BNCC**')

questoes_estante_bncc_n_questoes2 = pd.read_excel('questoes_estante_bncc_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_ef1_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões da BNCC no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[59]:


st.markdown('**Tópico 3.6: Número de questões por disciplina**')

questoes_estante_disciplina_n_questoes2_ordenado = pd.read_excel('questoes_estante_disciplina_n_questoes2_ordenado.xlsx')

fig1 = px.bar(questoes_estante_disciplina_n_questoes2_ordenado, x='Nº de questões', y='Disciplina')
fig1.update_layout(showlegend=False,
                    title="Número de questões por disciplina",
                    title_x=0.5,
                    xaxis_title='Nº de questões',
                    yaxis_title='Disciplina')
st.plotly_chart(fig1)


# In[60]:


st.markdown('**Tópico 3.7: Número de questões por fonte**')

questoes_estante_fonte_n_questoes2_ordenado_filt = pd.read_excel('questoes_estante_fonte_n_questoes2_ordenado_filt.xlsx')

fig1 = px.bar(questoes_estante_fonte_n_questoes2_ordenado_filt, x='Nº de questões', y='Fonte')
fig1.update_layout(showlegend=False,
                    title="Número de questões por fonte",
                    title_x=0.5,
                    xaxis_title='Nº de questões',
                    yaxis_title='Fonte')
st.plotly_chart(fig1)


# In[61]:


st.markdown('**Tópico 3.8: Número de tags por questão**')

questoes_estante_ntags3 = pd.read_excel('questoes_estante_ntags3.xlsx')

fig1 = px.bar(questoes_estante_ntags3, x='Número de tags', y='Número de questões')
fig1.update_layout(showlegend=False,
                    title="Número de tags por questão",
                    title_x=0.5,
                    xaxis_title='Número de tags',
                    yaxis_title='Número de questões')
st.plotly_chart(fig1)


# In[62]:


st.subheader('**Capítulo 4: Dados brutos acerca das Avaliações (Produto Diagnóstiqo)**')


# In[63]:


st.markdown('**Tópico 4.1: Números de avaliações criadas**')

numero_avaliacoes3 = pd.read_excel('numero_avaliacoes3.xlsx')

fig1 = px.bar(numero_avaliacoes3, x='Data', y='Número de avaliações')
fig1.update_layout(showlegend=False,
                    title="Número de AAs criadas por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Número de avaliações')
st.plotly_chart(fig1)


# In[64]:


st.markdown('**Tópico 4.2: Números de questões**')

numero_questoes_tipo3 = pd.read_excel('numero_questoes_tipo3.xlsx')

fig1 = px.bar(numero_questoes_tipo3, x='Mês', y=['Múltipla Escolha','Discursiva','Resposta Curta'])
fig1.update_layout(showlegend=True,
                    title="Número de questões por tipo",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Número de questões')
st.plotly_chart(fig1)


# In[65]:


st.markdown('**Tópico 4.3: Engajamento médio dos alunos**')

engajamento_medio_aa4 = pd.read_excel('engajamento_medio_aa4.xlsx')

fig1 = px.bar(engajamento_medio_aa4, x='Mês', y='Engajamento')
fig1.update_layout(showlegend=False,
                    title="Engajamento médio dos alunos",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Engajamento')
st.plotly_chart(fig1)


# In[66]:


st.markdown('**Tópico 4.4: Tempo médio dos alunos**')

tempo_aa3 = pd.read_excel('tempo_aa3.xlsx')

fig1 = px.bar(tempo_aa3, x='Mês', y='Tempo em AA')
fig1.update_layout(showlegend=False,
                    title="Tempo dos alunos em AA",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Horas')
st.plotly_chart(fig1)


# In[67]:


st.subheader('**Capítulo 5: Dados brutos acerca dos cadernos (Produto Pedagógiqo)**')


# In[68]:


st.markdown('**Tópico 5.1: Número de cadernos criados**')

numero_cadernos3 = pd.read_excel('numero_cadernos3.xlsx')

fig1 = px.bar(numero_cadernos3, x='Mês', y='Número de cadernos')
fig1.update_layout(showlegend=False,
                    title="Criação de cadernos",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Número de cadernos')
st.plotly_chart(fig1)


# In[69]:


st.markdown('**Tópico 5.2: Número de materiais nos cadernos**')

numero_materiais_cadernos10 = pd.read_excel('numero_materiais_cadernos10.xlsx')

fig1 = px.bar(numero_materiais_cadernos10, x='Tipo de material', y='Número de materiais', color="Tipo de material", color_discrete_sequence=["turquoise","red", "green", "blue", "orange", "yellow", "brown", "violet", "black","gray"])
fig1.update_layout(showlegend=False,
                    title="Número de materiais por tipo",
                    title_x=0.5,
                    xaxis_title='Tipo de material',
                    yaxis_title='Número de materiais',
                 )

st.plotly_chart(fig1)

numero_materiais_cadernos8 = pd.read_excel('numero_materiais_cadernos8.xlsx')

fig2 = px.bar(numero_materiais_cadernos8, x='Mês', y='Número de materiais', color="Tipo de material", color_discrete_sequence=["turquoise","red", "green", "blue", "orange", "yellow", "brown", "violet", "black","gray"])
fig2.update_layout(showlegend=True,
                    title="Número de materiais por tipo",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Número de materiais',
                 )

st.plotly_chart(fig2)

numero_materiais_cadernos9 = pd.read_excel('numero_materiais_cadernos9.xlsx')

fig1 = px.bar(numero_materiais_cadernos9, x='Mês', y='Porcentagem', color="Tipo de material", color_discrete_sequence=["turquoise","red", "green", "blue", "orange", "yellow", "brown", "violet", "black","gray"])
fig1.update_layout(showlegend=True,
                    title="Número de materiais por tipo normalizado",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Porcentagem',
                 )

st.plotly_chart(fig1)


# In[70]:


st.markdown('**Tópico 5.3: Engajamento nos cadernos**')

engajamento_cadernos_disciplina5 = pd.read_excel('engajamento_cadernos_disciplina5.xlsx')

fig1 = px.bar(engajamento_cadernos_disciplina5, x='Engajamento', y='Disciplina')
fig1.update_layout(showlegend=False,
                    title="Engajamento no cadernos por disciplina",
                    title_x=0.5,
                    xaxis_title='Engajamento',
                    yaxis_title='Disciplina')
fig1.update_xaxes(range=[0, 1])

st.plotly_chart(fig1)

engajamento_cadernos_segmento5 = pd.read_excel('engajamento_cadernos_segmento5.xlsx')

fig1 = px.bar(engajamento_cadernos_segmento5, x='Engajamento', y='Segmento')
fig1.update_layout(showlegend=False,
                    title="Engajamento no cadernos por segmento",
                    title_x=0.5,
                    xaxis_title='Engajamento',
                    yaxis_title='Disciplina')
fig1.update_xaxes(range=[0, 1])

st.plotly_chart(fig1)

engajamento_cadernos_tipomaterial5 = pd.read_excel('engajamento_cadernos_tipomaterial5.xlsx')

fig1 = px.bar(engajamento_cadernos_tipomaterial5, x='Tipo de material', y='Engajamento', color="Tipo de material", color_discrete_sequence=["turquoise","red", "green", "blue", "orange", "yellow", "brown", "violet", "black","gray"])
fig1.update_layout(showlegend=False,
                    title="Engajamento no cadernos por tipo de material",
                    title_x=0.5,
                    xaxis_title='Tipo de material',
                    yaxis_title='Engajamento')
fig1.update_yaxes(range=[0, 1])

st.plotly_chart(fig1)


# In[71]:


st.subheader('**Capítulo 6: Benefícios QBR por namespace**')


# In[72]:


st.markdown('**Tópico 6.1: Benefício 1: Alunos engajados, no seu próprio ritmo e recebendo feedback em tempo real**')
st.markdown('Item 6.1.1: Porcentagem de alunos ativos no período analisado')


# In[73]:


st.markdown('Item 6.1.2: Média de exercícios realizados por aluno por mês')


# In[74]:


st.markdown('Item 6.1.3: Média de conteúdos estudados por aluno por mês')


# In[75]:


st.markdown('**Tópico 6.2: Benefício 2: Professores que estão personalizando a aprendizagem**')
st.markdown('Item 6.2.1: Porcentagem de professores ativos no período analisado')


# In[76]:


st.markdown('Item 6.2.2: Média de exercícios selecionados, curados ou criados por professor por mês')


# In[77]:


st.markdown('Item 6.2.3: Média de conteudos selecionados, curados ou criados por professor por mês')


# In[78]:


st.markdown('**Tópico 6.3: Benefício 3: Escola que analisa dados para personalização da aprendizagem**')
st.markdown('Item 6.3.1: Porcentagem dos professores ativos que analisaram relatórios')


# In[79]:


st.markdown('Item 6.3.2: Média de relatórios analisados por professor por mês')


# In[80]:


st.markdown('**Tópico 6.4: Benefício 4: Escola que economiza tempo para dedicar ao mais importante: o aprendizado e crescimento dos seus alunos**')
st.markdown('Item 6.4.1: Número de questões corrigidas automaticamente')


# In[81]:


st.markdown('Item 6.4.2: Número de folhas que deixaram de existir, dando menos trabalho para a sua escola')


# In[82]:


st.markdown('Item 6.4.3: Horas que foram economizados desde a troca de arquivos para impressão até o recolhimento de atividades e correção pelos professores')


# In[83]:


st.markdown('Item 6.4.4: Valor economizado com impressão e papel considerando 10 centavos por folha não impressa')


# In[85]:


beneficios_qbr2 = pd.read_excel('beneficios_qbr2.xlsx')

beneficios_qbr3 = beneficios_qbr2.style.format({"Média":"{:,.2f}","Porcentagem de alunos ativos":"{:,.2f}","Média de exercícios realizados":"{:,.2f}","Média de conteúdos estudados":"{:,.2f}","Porcentagem de professores ativos":"{:,.2f}","Média de exercícios criados":"{:,.2f}","Média de conteúdos criados":"{:,.2f}","Porcentagem de professores que viram relatórios":"{:,.2f}","Média de relatórios vistos por professor":"{:,.2f}","Número de questões corrigidas automaticamente":"{:,.0f}","Número de folhas que deixaram de existir":"{:,.0f}","Horas que foram economizados":"{:,.2f}","Valor economizado com impressão e papel":"R$ {:,.2f}"}).background_gradient(cmap='Greens')

st.dataframe(beneficios_qbr3)

beneficios_qbr_normalizado3 = pd.read_excel('beneficios_qbr_normalizado3.xlsx')

beneficios_qbr_normalizado4 = beneficios_qbr_normalizado3.style.format({"Média":"{:,.2f}","Porcentagem de alunos ativos":"{:,.2f}","Média de exercícios realizados":"{:,.2f}","Média de conteúdos estudados":"{:,.2f}","Porcentagem de professores ativos":"{:,.2f}","Média de exercícios criados":"{:,.2f}","Média de conteúdos criados":"{:,.2f}","Porcentagem de professores que viram relatórios":"{:,.2f}","Média de relatórios vistos por professor":"{:,.2f}","Número de questões corrigidas automaticamente":"{:,.0f}","Número de folhas que deixaram de existir":"{:,.0f}","Horas que foram economizados":"{:,.2f}","Valor economizado com impressão e papel":"R$ {:,.2f}"}).background_gradient(cmap='Greens')

st.dataframe(beneficios_qbr_normalizado4)


# In[87]:


st.subheader('**Capítulo 7: Benefícios QBR por grupo em Redes**')


# In[99]:


st.markdown('**Tópico 7.1: Rede Inspira**')
st.markdown('Item 7.1.1: Total')

beneficios_rede = pd.read_excel('beneficios_rede.xlsx')
beneficios_rede2 = beneficios_rede.drop(columns = ['Unnamed: 0'])

select = st.sidebar.selectbox('Selecione uma rede',beneficios_rede2['Rede'].unique())

beneficios_rede_filt1 = beneficios_rede2[beneficios_rede2['Rede'] == select]

select2 = st.sidebar.selectbox('Selecione um grupo',beneficios_rede_filt1['grupo'].unique())

beneficios_rede_filt2 = beneficios_rede_filt1[beneficios_rede_filt1['grupo'] == select2]

st.dataframe(beneficios_rede_filt2)

#select

