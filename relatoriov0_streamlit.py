#!/usr/bin/env python
# coding: utf-8

# In[450]:


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


# In[451]:


st.image('[LOGO] Eduqo.png')

st.title('Relatório de uso da plataforma QMágico')

image = Image.open('[LOGO] Eduqo.png')
st.sidebar.image(image,caption='Eduqo - Plataforma QMágico',use_column_width=True)

st.sidebar.markdown('Feito por : Alexandre Fernandes (Padre)')

#st.sidebar.write('[Capítulo 1](https://share.streamlit.io/alexandre-padre/relatorio-v0/main/relatoriov0_streamlit.py#cap-tulo-1)')


# In[452]:


st.subheader('**Capítulo 1**')


# In[453]:


st.subheader('**Capítulo 2: Dados brutos acerca do tempo gasto pelos usuários ativos na plataforma**')


# In[454]:


st.markdown('**Tópico 2.1: Alunos**')

alunos_tempo_uniao2 = pd.read_excel('alunos_tempo_uniao2.xlsx')

fig1 = px.bar(alunos_tempo_uniao2, x='Dia', y='Horas por aluno')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de alunos por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por aluno')
st.plotly_chart(fig1)


# In[455]:


st.markdown('**Tópico 2.2: Professores**')

professores_tempo_uniao2 = pd.read_excel('professores_tempo_uniao2.xlsx')

fig1 = px.bar(professores_tempo_uniao2, x='Dia', y='Horas por professor')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de professores por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por professores')
st.plotly_chart(fig1)


# In[456]:


st.markdown('**Tópico 2.3: Administradores**')

admin_tempo_uniao2 = pd.read_excel('admin_tempo_uniao2.xlsx')

fig1 = px.bar(admin_tempo_uniao2, x='Dia', y='Horas por administrador')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de administradores por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por administradores')
st.plotly_chart(fig1)


# In[457]:


st.subheader('**Capítulo 3: Dados brutos acerca do Banco de Questões Eduqo (Produto Banqo)**')


# In[458]:


st.markdown('**Tópico 3.1: Número de questões**')

questoes_estante_n_questoes2 = pd.read_excel('questoes_estante_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[459]:


st.markdown('**Tópico 3.2: Número de questões EM**')

questoes_estante_em_n_questoes2 = pd.read_excel('questoes_estante_em_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_em_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Médio no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[460]:


st.markdown('**Tópico 3.3: Número de questões EF2**')

questoes_estante_ef2_n_questoes2 = pd.read_excel('questoes_estante_ef2_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_ef2_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Fundamental II no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[461]:


st.markdown('**Tópico 3.4: Número de questões EF1**')

questoes_estante_ef1_n_questoes2 = pd.read_excel('questoes_estante_ef1_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_ef1_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Fundamental I no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[462]:


st.markdown('**Tópico 3.5: Número de questões BNCC**')

questoes_estante_bncc_n_questoes2 = pd.read_excel('questoes_estante_bncc_n_questoes2.xlsx')

fig1 = px.area(questoes_estante_ef1_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões da BNCC no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[463]:


st.markdown('**Tópico 3.6: Número de questões por disciplina**')

questoes_estante_disciplina_n_questoes2_ordenado = pd.read_excel('questoes_estante_disciplina_n_questoes2_ordenado.xlsx')

fig1 = px.bar(questoes_estante_disciplina_n_questoes2_ordenado, x='Nº de questões', y='Disciplina')
fig1.update_layout(showlegend=False,
                    title="Número de questões por disciplina",
                    title_x=0.5,
                    xaxis_title='Nº de questões',
                    yaxis_title='Disciplina')
st.plotly_chart(fig1)


# In[464]:


st.markdown('**Tópico 3.7: Número de questões por fonte**')

questoes_estante_fonte_n_questoes2_ordenado_filt = pd.read_excel('questoes_estante_fonte_n_questoes2_ordenado_filt.xlsx')

fig1 = px.bar(questoes_estante_fonte_n_questoes2_ordenado_filt, x='Nº de questões', y='Fonte')
fig1.update_layout(showlegend=False,
                    title="Número de questões por fonte",
                    title_x=0.5,
                    xaxis_title='Nº de questões',
                    yaxis_title='Fonte')
st.plotly_chart(fig1)


# In[465]:


st.markdown('**Tópico 3.8: Número de tags por questão**')

questoes_estante_ntags3 = pd.read_excel('questoes_estante_ntags3.xlsx')

fig1 = px.bar(questoes_estante_ntags3, x='Número de tags', y='Número de questões')
fig1.update_layout(showlegend=False,
                    title="Número de tags por questão",
                    title_x=0.5,
                    xaxis_title='Número de tags',
                    yaxis_title='Número de questões')
st.plotly_chart(fig1)


# In[466]:


st.subheader('**Capítulo 4: Dados brutos acerca das Avaliações (Produto Diagnóstiqo)**')


# In[467]:


st.markdown('**Tópico 4.1: Números de avaliações criadas**')

numero_avaliacoes3 = pd.read_excel('numero_avaliacoes3.xlsx')

fig1 = px.bar(numero_avaliacoes3, x='Data', y='Número de avaliações')
fig1.update_layout(showlegend=False,
                    title="Número de AAs criadas por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Número de avaliações')
st.plotly_chart(fig1)


# In[468]:


st.markdown('**Tópico 4.2: Números de questões**')

numero_questoes_tipo3 = pd.read_excel('numero_questoes_tipo3.xlsx')

fig1 = px.bar(numero_questoes_tipo3, x='Mês', y=['Múltipla Escolha','Discursiva','Resposta Curta'])
fig1.update_layout(showlegend=True,
                    title="Número de questões por tipo",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Número de questões')
st.plotly_chart(fig1)


# In[469]:


st.markdown('**Tópico 4.3: Engajamento médio dos alunos**')

engajamento_medio_aa4 = pd.read_excel('engajamento_medio_aa4.xlsx')

fig1 = px.bar(engajamento_medio_aa4, x='Mês', y='Engajamento')
fig1.update_layout(showlegend=False,
                    title="Engajamento médio dos alunos",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Engajamento')
st.plotly_chart(fig1)


# In[470]:


st.markdown('**Tópico 4.4: Tempo médio dos alunos**')

tempo_aa3 = pd.read_excel('tempo_aa3.xlsx')

fig1 = px.bar(tempo_aa3, x='Mês', y='Tempo em AA')
fig1.update_layout(showlegend=False,
                    title="Tempo dos alunos em AA",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Horas')
st.plotly_chart(fig1)


# In[471]:


st.subheader('**Capítulo 5: Dados brutos acerca dos cadernos (Produto Pedagógiqo)**')


# In[472]:


st.markdown('**Tópico 5.1: Número de cadernos criados**')

numero_cadernos3 = pd.read_excel('numero_cadernos3.xlsx')

fig1 = px.bar(numero_cadernos3, x='Mês', y='Número de cadernos')
fig1.update_layout(showlegend=False,
                    title="Criação de cadernos",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Número de cadernos')
st.plotly_chart(fig1)


# In[473]:


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


# In[474]:


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


# In[475]:


st.subheader('**Capítulo 6: Benefícios QBR por namespace**')


# In[476]:


st.markdown('**Tópico 6.1: Benefício 1: Alunos engajados, no seu próprio ritmo e recebendo feedback em tempo real**')
st.markdown('Item 6.1.1: Porcentagem de alunos ativos no período analisado')


# In[477]:


st.markdown('Item 6.1.2: Média de exercícios realizados por aluno por mês')


# In[478]:


st.markdown('Item 6.1.3: Média de conteúdos estudados por aluno por mês')


# In[479]:


st.markdown('**Tópico 6.2: Benefício 2: Professores que estão personalizando a aprendizagem**')
st.markdown('Item 6.2.1: Porcentagem de professores ativos no período analisado')


# In[480]:


st.markdown('Item 6.2.2: Média de exercícios selecionados, curados ou criados por professor por mês')


# In[481]:


st.markdown('Item 6.2.3: Média de conteudos selecionados, curados ou criados por professor por mês')


# In[482]:


st.markdown('**Tópico 6.3: Benefício 3: Escola que analisa dados para personalização da aprendizagem**')
st.markdown('Item 6.3.1: Porcentagem dos professores ativos que analisaram relatórios')


# In[483]:


st.markdown('Item 6.3.2: Média de relatórios analisados por professor por mês')


# In[484]:


st.markdown('**Tópico 6.4: Benefício 4: Escola que economiza tempo para dedicar ao mais importante: o aprendizado e crescimento dos seus alunos**')
st.markdown('Item 6.4.1: Número de questões corrigidas automaticamente')


# In[485]:


st.markdown('Item 6.4.2: Número de folhas que deixaram de existir, dando menos trabalho para a sua escola')


# In[486]:


st.markdown('Item 6.4.3: Horas que foram economizados desde a troca de arquivos para impressão até o recolhimento de atividades e correção pelos professores')


# In[487]:


st.markdown('Item 6.4.4: Valor economizado com impressão e papel considerando 10 centavos por folha não impressa')


# In[488]:


st.markdown('**Benefícios QBR: Resultados**')

beneficios_rede = pd.read_excel('beneficios_rede.xlsx')
beneficios_rede2 = beneficios_rede.drop(columns = ['Unnamed: 0'])

# Filtro de redes

rede = pd.Series(['Rede'])
lista_redes = pd.Series(beneficios_rede2['Rede'].unique()).sort_values()
rede = rede.append(lista_redes).reset_index()
rede2 = rede.drop(columns = ['index'])

select = st.sidebar.selectbox('Selecione uma rede',rede2)

if select == 'Rede':
    beneficios_rede_filt1 = beneficios_rede2
else:
    beneficios_rede_filt1 = beneficios_rede2[beneficios_rede2['Rede'] == select]
 
# Filtro de grupos

grupo = pd.Series(['Grupo'])
lista_grupos = pd.Series(beneficios_rede_filt1['grupo'].unique()).sort_values()
grupo = grupo.append(lista_grupos).reset_index()
grupo2 = grupo.drop(columns = ['index'])    
    
select2 = st.sidebar.selectbox('Selecione um grupo',grupo2)

if select2 == 'Grupo':
    beneficios_rede_filt2 = beneficios_rede_filt1
else:
    beneficios_rede_filt2 = beneficios_rede_filt1[beneficios_rede_filt1['grupo'] == select2]
 
# Filtro de namespaces

namespace = pd.Series(['Namespace'])
lista_namespaces = pd.Series(beneficios_rede_filt2['namespace'].unique()).sort_values()
namespace = namespace.append(lista_namespaces).reset_index()
namespace2 = namespace.drop(columns = ['index'])    
    
select3 = st.sidebar.selectbox('Selecione um namespace',namespace2)

if select3 == 'Namespace':
    beneficios_rede_filt3 = beneficios_rede_filt2
else:
    beneficios_rede_filt3 = beneficios_rede_filt2[beneficios_rede_filt2['namespace'] == select3]
    

beneficios_rede_filt4 = beneficios_rede_filt3.replace(np.nan,'').reset_index()   
beneficios_rede_filt4.rename(columns = {'Porcentagem de alunos ativos':'6.1.1','Média de exercícios realizados':'6.1.2','Média de conteúdos estudados':'6.1.3','Porcentagem de professores ativos':'6.2.1','Média de exercícios criados':'6.2.2','Média de conteúdos criados':'6.2.3','Porcentagem de professores que viram relatórios':'6.3.1','Média de relatórios vistos por professor':'6.3.2','Número de questões corrigidas automaticamente':'6.4.1','Número de folhas que deixaram de existir':'6.4.2','Horas que foram economizados':'6.4.3','Valor economizado com impressão e papel':'6.4.4'},inplace = True)
beneficios_rede_filt5 = beneficios_rede_filt4.drop(columns = ['index']).sort_values(by = ['namespace']).reset_index()  
beneficios_rede_filt6 = beneficios_rede_filt5.drop(columns = ['index'])
numeric_col_mask = beneficios_rede_filt6.dtypes.apply(lambda d: issubclass(np.dtype(d).type, np.number))

d = dict(selector="th", props=[('text-align', 'center')])

beneficios_rede_filt7 = beneficios_rede_filt6.style.format({"Média":"{:,.2f}","6.1.1":"{:,.2f}","6.1.2":"{:,.2f}","6.1.3":"{:,.2f}","6.2.1":"{:,.2f}","6.2.2":"{:,.2f}","6.2.3":"{:,.2f}","6.3.1":"{:,.2f}","6.3.2":"{:,.2f}","6.4.1":"{:,.0f}","6.4.2":"{:,.0f}","6.4.3":"{:,.2f}","6.4.4":"R$ {:,.2f}"}).background_gradient(cmap='Blues')                                                    .set_properties(subset=beneficios_rede_filt6.columns[~numeric_col_mask], # right-align the numeric columns and set their width
                                                    **{'width':'10em', 'text-align':'left'})\
                                                    #.set_properties(subset=beneficios_rede_filt6.columns[numeric_col_mask], # right-align the numeric columns and set their width
                                                    #**{'width':'10em', 'text-align':'center'})
                                                    

st.dataframe(beneficios_rede_filt7)
             
#beneficios_rede_filt7


# In[489]:


st.markdown('**Benefícios QBR: Resultados normalizados pela média**')

beneficios_rede = pd.read_excel('beneficios_rede_normalizado.xlsx')
beneficios_rede2 = beneficios_rede.drop(columns = ['Unnamed: 0'])

# Filtro de redes

rede = pd.Series(['Rede'])
lista_redes = pd.Series(beneficios_rede2['Rede'].unique()).sort_values()
rede = rede.append(lista_redes).reset_index()
rede2 = rede.drop(columns = ['index'])

if select == 'Rede':
    beneficios_rede_filt1 = beneficios_rede2
else:
    beneficios_rede_filt1 = beneficios_rede2[beneficios_rede2['Rede'] == select]
 
# Filtro de grupos

grupo = pd.Series(['Grupo'])
lista_grupos = pd.Series(beneficios_rede_filt1['grupo'].unique()).sort_values()
grupo = grupo.append(lista_grupos).reset_index()
grupo2 = grupo.drop(columns = ['index'])    

if select2 == 'Grupo':
    beneficios_rede_filt2 = beneficios_rede_filt1
else:
    beneficios_rede_filt2 = beneficios_rede_filt1[beneficios_rede_filt1['grupo'] == select2]
 
# Filtro de namespaces

namespace = pd.Series(['Namespace'])
lista_namespaces = pd.Series(beneficios_rede_filt2['namespace'].unique()).sort_values()
namespace = namespace.append(lista_namespaces).reset_index()
namespace2 = namespace.drop(columns = ['index'])    

if select3 == 'Namespace':
    beneficios_rede_filt3 = beneficios_rede_filt2
else:
    beneficios_rede_filt3 = beneficios_rede_filt2[beneficios_rede_filt2['namespace'] == select3]
    

beneficios_rede_filt4 = beneficios_rede_filt3.replace(np.nan,'').reset_index()   
beneficios_rede_filt4.rename(columns = {'Porcentagem de alunos ativos':'6.1.1','Média de exercícios realizados':'6.1.2','Média de conteúdos estudados':'6.1.3','Porcentagem de professores ativos':'6.2.1','Média de exercícios criados':'6.2.2','Média de conteúdos criados':'6.2.3','Porcentagem de professores que viram relatórios':'6.3.1','Média de relatórios vistos por professor':'6.3.2','Número de questões corrigidas automaticamente':'6.4.1','Número de folhas que deixaram de existir':'6.4.2','Horas que foram economizados':'6.4.3','Valor economizado com impressão e papel':'6.4.4'},inplace = True)
beneficios_rede_filt5_ = beneficios_rede_filt4.drop(columns = ['index']).sort_values(by = 'Média', ascending = False)


numeric_col_mask = beneficios_rede_filt5_.dtypes.apply(lambda d: issubclass(np.dtype(d).type, np.number))

d = dict(selector="th", props=[('text-align', 'center')])

beneficios_rede_filt6_ = beneficios_rede_filt5_.style.format({"Média":"{:,.2f}","6.1.1":"{:,.2f}","6.1.2":"{:,.2f}","6.1.3":"{:,.2f}","6.2.1":"{:,.2f}","6.2.2":"{:,.2f}","6.2.3":"{:,.2f}","6.3.1":"{:,.2f}","6.3.2":"{:,.2f}","6.4.1":"{:,.0f}","6.4.2":"{:,.0f}","6.4.3":"{:,.2f}","6.4.4":"R$ {:,.2f}"}).background_gradient(cmap='Blues')                                                    .set_properties(subset=beneficios_rede_filt5_.columns[~numeric_col_mask], # right-align the numeric columns and set their width
                                                    **{'width':'10em', 'text-align':'left'})\
                                                    #.set_properties(subset=beneficios_rede_filt5_.columns[numeric_col_mask], # right-align the numeric columns and set their width
                                                    #**{'width':'10em', 'text-align':'center'})
                                                    

st.dataframe(beneficios_rede_filt6_)
             
#beneficios_rede_filt6


# In[490]:


st.subheader('**Capítulo 7: Benefícios QBR em Redes**')


# In[491]:


st.markdown('**Tópico 7.1: Redes**')

beneficios_rede_total = beneficios_rede_filt6.reset_index().groupby('Rede').agg(C611 = ('6.1.1','mean'),
                                                                                C612 = ('6.1.2','sum'),
                                                                                C613 = ('6.1.3','sum'),
                                                                                C621 = ('6.2.1','mean'),
                                                                                C622 = ('6.2.2','sum'),
                                                                                C623 = ('6.2.3','sum'),
                                                                                C631 = ('6.3.1','mean'),
                                                                                C632 = ('6.3.2','sum'),
                                                                                C641 = ('6.4.1','sum'),
                                                                                C642 = ('6.4.2','sum'),
                                                                                C643 = ('6.4.3','sum'),
                                                                                C644 = ('6.4.4','sum'))
beneficios_rede_total = beneficios_rede_total.reset_index()
#beneficios_rede_total

beneficios_rede_total.rename(columns = {'C611':'6.1.1','C612':'6.1.2','C613':'6.1.3','C621':'6.2.1','C622':'6.2.2','C623':'6.2.3','C631':'6.3.1','C632':'6.3.2','C641':'6.4.1','C642':'6.4.2','C643':'6.4.3','C644':'6.4.4'},inplace = True)

# Filtro de redes

rede = pd.Series(['Rede'])
lista_redes = pd.Series(beneficios_rede_total['Rede'].unique()).sort_values()
rede = rede.append(lista_redes).reset_index()
rede2 = rede.drop(columns = ['index'])

if select == 'Rede':
    beneficios_rede_total2 = beneficios_rede_total
else:
    beneficios_rede_total2 = beneficios_rede_total[beneficios_rede_total['Rede'] == select]

beneficios_rede_total3 = beneficios_rede_total2[beneficios_rede_total2['Rede'] != '']
    
numeric_col_mask = beneficios_rede_total3.dtypes.apply(lambda d: issubclass(np.dtype(d).type, np.number))    
    
beneficios_rede_total4 = beneficios_rede_total3.style.format({"Média":"{:,.2f}","6.1.1":"{:,.2f}","6.1.2":"{:,.2f}","6.1.3":"{:,.2f}","6.2.1":"{:,.2f}","6.2.2":"{:,.2f}","6.2.3":"{:,.2f}","6.3.1":"{:,.2f}","6.3.2":"{:,.2f}","6.4.1":"{:,.0f}","6.4.2":"{:,.0f}","6.4.3":"{:,.2f}","6.4.4":"R$ {:,.2f}"}).background_gradient(cmap='Blues')                                                    .set_properties(subset=beneficios_rede_total3.columns[~numeric_col_mask], # right-align the numeric columns and set their width
                                                    **{'width':'10em', 'text-align':'left'})\
                                                    #.set_properties(subset=beneficios_rede_total3.columns[numeric_col_mask], # right-align the numeric columns and set their width
                                                    #**{'width':'10em', 'text-align':'center'})

st.dataframe(beneficios_rede_total4)


# In[492]:


st.markdown('**Tópico 7.2: Grupos**')

beneficios_grupo_total = beneficios_rede_filt6.reset_index().groupby(['Rede','grupo']).agg(C611 = ('6.1.1','mean'),
                                                                                C612 = ('6.1.2','sum'),
                                                                                C613 = ('6.1.3','sum'),
                                                                                C621 = ('6.2.1','mean'),
                                                                                C622 = ('6.2.2','sum'),
                                                                                C623 = ('6.2.3','sum'),
                                                                                C631 = ('6.3.1','mean'),
                                                                                C632 = ('6.3.2','sum'),
                                                                                C641 = ('6.4.1','sum'),
                                                                                C642 = ('6.4.2','sum'),
                                                                                C643 = ('6.4.3','sum'),
                                                                                C644 = ('6.4.4','sum'))
beneficios_grupo_total = beneficios_grupo_total.reset_index()
#beneficios_rede_total

beneficios_grupo_total.rename(columns = {'C611':'6.1.1','C612':'6.1.2','C613':'6.1.3','C621':'6.2.1','C622':'6.2.2','C623':'6.2.3','C631':'6.3.1','C632':'6.3.2','C641':'6.4.1','C642':'6.4.2','C643':'6.4.3','C644':'6.4.4'},inplace = True)

# Filtro de redes

rede = pd.Series(['Rede'])
lista_redes = pd.Series(beneficios_grupo_total['Rede'].unique()).sort_values()
rede = rede.append(lista_redes).reset_index()
rede2 = rede.drop(columns = ['index'])

if select == 'Rede':
    beneficios_grupo_total2 = beneficios_grupo_total
else:
    beneficios_grupo_total2 = beneficios_grupo_total[beneficios_grupo_total['Rede'] == select]
 
# Filtro de grupos

grupo = pd.Series(['Grupo'])
lista_grupos = pd.Series(beneficios_grupo_total2['grupo'].unique()).sort_values()
grupo = grupo.append(lista_grupos).reset_index()
grupo2 = grupo.drop(columns = ['index'])    

if select2 == 'Grupo':
    beneficios_grupo_total3 = beneficios_grupo_total2
else:
    beneficios_grupo_total3 = beneficios_grupo_total2[beneficios_grupo_total2['grupo'] == select2]
    
beneficios_grupo_total4 = beneficios_grupo_total3[beneficios_grupo_total3['Rede'] != '']

numeric_col_mask = beneficios_grupo_total4.dtypes.apply(lambda d: issubclass(np.dtype(d).type, np.number))    
    
beneficios_grupo_total5 = beneficios_grupo_total4.style.format({"Média":"{:,.2f}","6.1.1":"{:,.2f}","6.1.2":"{:,.2f}","6.1.3":"{:,.2f}","6.2.1":"{:,.2f}","6.2.2":"{:,.2f}","6.2.3":"{:,.2f}","6.3.1":"{:,.2f}","6.3.2":"{:,.2f}","6.4.1":"{:,.0f}","6.4.2":"{:,.0f}","6.4.3":"{:,.2f}","6.4.4":"R$ {:,.2f}"}).background_gradient(cmap='Blues')                                                    .set_properties(subset=beneficios_grupo_total4.columns[~numeric_col_mask], # right-align the numeric columns and set their width
                                                    **{'width':'10em', 'text-align':'left'})\
                                                    #.set_properties(subset=beneficios_grupo_total4.columns[numeric_col_mask], # right-align the numeric columns and set their width
                                                    #**{'width':'10em', 'text-align':'center'})

st.dataframe(beneficios_grupo_total5)

