#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Código para minimizar as linhas de código 

from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')


# In[2]:


# imports e definições
import pandas as pd
import psycopg2
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date, timedelta
import streamlit as st
import math
from PIL import Image
import plotly.offline as py
import plotly.express as px
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)

from psycopg2.extensions import register_adapter, AsIs
def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)
def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)
def addapt_numpy_int32(numpy_int32):
    return AsIs(numpy_int32)
register_adapter(np.float64, addapt_numpy_float64)
register_adapter(np.int64, addapt_numpy_int64)
register_adapter(np.int32, addapt_numpy_int32)

def retrieve_query(cursor):
    data = []
    for row in cursor.fetchall():
        data.append(row)
    return data


# In[3]:


st.image('[LOGO] Eduqo.png')

st.title('Relatório de uso da plataforma QMágico')

image = Image.open('[LOGO] Eduqo.png')
st.sidebar.image(image,caption='Eduqo - Plataforma QMágico',use_column_width=True)

st.sidebar.markdown('Feito por : Alexandre Fernandes (Padre)')


# In[4]:


st.subheader('**Capítulo 1**')


# In[5]:


st.subheader('**Capítulo 2: Dados brutos acerca do tempo gasto pelos usuários ativos na plataforma**')


# In[6]:


st.markdown('**Tópico 2.1: Alunos**')

alunos_tempo = pd.read_excel('alunos_tempo.xlsx')
#alunos_tempo


# In[7]:


alunos_tempo2 = alunos_tempo.drop(columns=['Unnamed: 0'])
#alunos_tempo2

alunos_tempo_total = alunos_tempo2.groupby(['day']).sum().reset_index()
alunos_tempo_total['seconds'] = alunos_tempo_total['seconds']/3600
alunos_tempo_total.rename(columns = {'seconds':'hours'}, inplace=True)
#alunos_tempo_total

alunos_tempo_n_alunos = alunos_tempo2.groupby(['day']).count().reset_index()
alunos_tempo_n_alunos2 = alunos_tempo_n_alunos.drop(columns = ['namespace','user_id'])
alunos_tempo_n_alunos2.rename(columns = {'seconds':'n_alunos'}, inplace=True)
#alunos_tempo_n_alunos2

alunos_tempo_uniao = pd.merge(alunos_tempo_total,alunos_tempo_n_alunos2, on = 'day', how = 'outer')
alunos_tempo_uniao['Horas por aluno'] = alunos_tempo_uniao['hours']/alunos_tempo_uniao['n_alunos']
alunos_tempo_uniao2 = alunos_tempo_uniao.drop(columns = ['hours','n_alunos'])
alunos_tempo_uniao2["Horas por aluno"] = pd.to_numeric(alunos_tempo_uniao2["Horas por aluno"], errors="coerce")
alunos_tempo_uniao2.rename(columns = {'day':'Dia'}, inplace=True)
#alunos_tempo_uniao2

fig1 = px.bar(alunos_tempo_uniao2, x='Dia', y='Horas por aluno')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de alunos por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por aluno')
st.plotly_chart(fig1)


# In[8]:


st.markdown('**Tópico 2.2: Professores**')

professores_tempo = pd.read_excel('professores_tempo.xlsx')
#professores_tempo


# In[9]:


professores_tempo2 = professores_tempo.drop(columns=['Unnamed: 0'])
#professores_tempo2

professores_tempo_total = professores_tempo2.groupby(['day']).sum().reset_index()
professores_tempo_total['seconds'] = professores_tempo_total['seconds']/3600
professores_tempo_total.rename(columns = {'seconds':'hours'}, inplace=True)
#professores_tempo_total

professores_tempo_n_professores = professores_tempo2.groupby(['day']).count().reset_index()
professores_tempo_n_professores2 = professores_tempo_n_professores.drop(columns = ['namespace','user_id'])
professores_tempo_n_professores2.rename(columns = {'seconds':'n_professores'}, inplace=True)
#professores_tempo_n_professores2

professores_tempo_uniao = pd.merge(professores_tempo_total,professores_tempo_n_professores2, on = 'day', how = 'outer')
professores_tempo_uniao['Horas por professor'] = professores_tempo_uniao['hours']/professores_tempo_uniao['n_professores']
professores_tempo_uniao2 = professores_tempo_uniao.drop(columns = ['hours','n_professores'])
professores_tempo_uniao2["Horas por professor"] = pd.to_numeric(professores_tempo_uniao2["Horas por professor"], errors="coerce")
professores_tempo_uniao2.rename(columns = {'day':'Dia'}, inplace=True)
#professores_tempo_professores2

fig1 = px.bar(professores_tempo_uniao2, x='Dia', y='Horas por professor')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de professores por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por professores')
st.plotly_chart(fig1)


# In[10]:


st.markdown('**Tópico 2.3: Administradores**')

admin_tempo = pd.read_excel('administradores_tempo.xlsx')
#admin_tempo


# In[11]:


admin_tempo2 = admin_tempo.drop(columns=['Unnamed: 0'])
#admin_tempo2

admin_tempo_total = admin_tempo2.groupby(['day']).sum().reset_index()
admin_tempo_total['seconds'] = admin_tempo_total['seconds']/3600
admin_tempo_total.rename(columns = {'seconds':'hours'}, inplace=True)
#admin_tempo_total

admin_tempo_n_admin = admin_tempo2.groupby(['day']).count().reset_index()
admin_tempo_n_admin2 = admin_tempo_n_admin.drop(columns = ['namespace','user_id'])
admin_tempo_n_admin2.rename(columns = {'seconds':'n_admin'}, inplace=True)
#admin_tempo_n_admin2

admin_tempo_uniao = pd.merge(admin_tempo_total,admin_tempo_n_admin2, on = 'day', how = 'outer')
admin_tempo_uniao['Horas por administrador'] = admin_tempo_uniao['hours']/admin_tempo_uniao['n_admin']
admin_tempo_uniao2 = admin_tempo_uniao.drop(columns = ['hours','n_admin'])
admin_tempo_uniao2["Horas por administrador"] = pd.to_numeric(admin_tempo_uniao2["Horas por administrador"], errors="coerce")
admin_tempo_uniao2.rename(columns = {'day':'Dia'}, inplace=True)
#admin_tempo_uniao2

fig1 = px.bar(admin_tempo_uniao2, x='Dia', y='Horas por administrador')
fig1.update_layout(showlegend=False,
                    title="Tempo médio de uso de administradores por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Horas por administradores')
st.plotly_chart(fig1)


# In[12]:


st.subheader('**Capítulo 3: Dados brutos acerca do Banco de Questões Eduqo (Produto Banqo)**')
#st.markdown('Nesse capítulo estão presentes as análises acerca do uso do **Banco de questões (Produto Banqo)**')


# In[13]:


st.markdown('**Tópico 3.1: Número de questões**')

questoes_estante = pd.read_excel('questoes_estante.xlsx')
#questoes_estante


# In[14]:


questoes_estante2 = questoes_estante.drop(columns=['Unnamed: 0'])
#uestoes_estante2

questoes_estante_n_questoes = questoes_estante2.groupby(['created']).count().reset_index()
questoes_estante_n_questoes.rename(columns = {'id':'n_questoes'}, inplace=True)
questoes_estante_n_questoes['Nº questões cumulativa'] = questoes_estante_n_questoes['n_questoes'].cumsum()
questoes_estante_n_questoes2 = questoes_estante_n_questoes.drop(columns = ['n_questoes'])
questoes_estante_n_questoes2.rename(columns = {'created':'Data'}, inplace = True)
#questoes_estante_n_questoes2


fig1 = px.area(questoes_estante_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[15]:


st.markdown('**Tópico 3.2: Número de questões EM**')

questoes_estante_em = pd.read_excel('questoes_estante_em.xlsx')
#questoes_estante_em


# In[16]:


questoes_estante_em2 = questoes_estante_em.drop(columns=['Unnamed: 0'])
#uestoes_estante_em2

questoes_estante_em_n_questoes = questoes_estante_em2.groupby(['created']).count().reset_index()
questoes_estante_em_n_questoes.rename(columns = {'id':'n_questoes'}, inplace=True)
questoes_estante_em_n_questoes['Nº questões cumulativa'] = questoes_estante_em_n_questoes['n_questoes'].cumsum()
questoes_estante_em_n_questoes2 = questoes_estante_em_n_questoes.drop(columns = ['n_questoes'])
questoes_estante_em_n_questoes2.rename(columns = {'created':'Data'}, inplace = True)
#questoes_estante_em_n_questoes2


fig1 = px.area(questoes_estante_em_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Médio no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[17]:


st.markdown('**Tópico 3.3: Número de questões EF2**')

questoes_estante_ef2 = pd.read_excel('questoes_estante_ef2.xlsx')
#questoes_estante_ef2


# In[18]:


questoes_estante_ef22 = questoes_estante_ef2.drop(columns=['Unnamed: 0'])
#questoes_estante_ef22

questoes_estante_ef2_n_questoes = questoes_estante_ef22.groupby(['created']).count().reset_index()
questoes_estante_ef2_n_questoes.rename(columns = {'id':'n_questoes'}, inplace=True)
questoes_estante_ef2_n_questoes['Nº questões cumulativa'] = questoes_estante_ef2_n_questoes['n_questoes'].cumsum()
questoes_estante_ef2_n_questoes2 = questoes_estante_ef2_n_questoes.drop(columns = ['n_questoes'])
questoes_estante_ef2_n_questoes2.rename(columns = {'created':'Data'}, inplace = True)
#questoes_estante_ef2_n_questoes2

fig1 = px.area(questoes_estante_ef2_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Fundamental II no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[19]:


st.markdown('**Tópico 3.4: Número de questões EF1**')

questoes_estante_ef1 = pd.read_excel('questoes_estante_ef1.xlsx')
#questoes_estante_ef1


# In[20]:


questoes_estante_ef12 = questoes_estante_ef1.drop(columns=['Unnamed: 0'])
#questoes_estante_ef12

questoes_estante_ef1_n_questoes = questoes_estante_ef12.groupby(['created']).count().reset_index()
questoes_estante_ef1_n_questoes.rename(columns = {'id':'n_questoes'}, inplace=True)
questoes_estante_ef1_n_questoes['Nº questões cumulativa'] = questoes_estante_ef1_n_questoes['n_questoes'].cumsum()
questoes_estante_ef1_n_questoes2 = questoes_estante_ef1_n_questoes.drop(columns = ['n_questoes'])
questoes_estante_ef1_n_questoes2.rename(columns = {'created':'Data'}, inplace = True)
#questoes_estante_ef1_n_questoes2

fig1 = px.area(questoes_estante_ef1_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões de Ensino Fundamental I no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[21]:


st.markdown('**Tópico 3.5: Número de questões BNCC**')

questoes_estante_bncc = pd.read_excel('questoes_estante_bncc.xlsx')
#questoes_estante_bncc


# In[22]:


questoes_estante_bncc2 = questoes_estante_bncc.drop(columns=['Unnamed: 0'])
#questoes_estante_bncc2

questoes_estante_bncc_n_questoes = questoes_estante_bncc2.groupby(['created']).count().reset_index()
questoes_estante_bncc_n_questoes.rename(columns = {'id':'n_questoes'}, inplace=True)
questoes_estante_bncc_n_questoes['Nº questões cumulativa'] = questoes_estante_bncc_n_questoes['n_questoes'].cumsum()
questoes_estante_bncc_n_questoes2 = questoes_estante_bncc_n_questoes.drop(columns = ['n_questoes','name'])
questoes_estante_bncc_n_questoes2.rename(columns = {'created':'Data'}, inplace = True)
#questoes_estante_bncc_n_questoes2

fig1 = px.area(questoes_estante_ef1_n_questoes2, x='Data', y='Nº questões cumulativa')
fig1.update_layout(showlegend=False,
                    title="Número de questões da BNCC no Banco de Questões",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Nº questões cumulativa')
st.plotly_chart(fig1)


# In[23]:


st.markdown('**Tópico 3.6: Número de questões por disciplina**')

questoes_estante_disciplina = pd.read_excel('questoes_estante_disciplina.xlsx')
#questoes_estante_disciplina


# In[24]:


questoes_estante_disciplina2 = questoes_estante_disciplina.drop(columns=['Unnamed: 0'])
#questoes_estante_disciplina2

questoes_estante_disciplina_n_questoes = questoes_estante_disciplina2.groupby(['name']).count().reset_index()
questoes_estante_disciplina_n_questoes.rename(columns = {'id':'n_questoes'}, inplace=True)
questoes_estante_disciplina_n_questoes2 = questoes_estante_disciplina_n_questoes.drop(columns = ['created'])
questoes_estante_disciplina_n_questoes2_ordenado = questoes_estante_disciplina_n_questoes2.sort_values(by='name',ascending=False)
questoes_estante_disciplina_n_questoes2_ordenado.rename(columns = {'name':'Disciplina'}, inplace = True)
questoes_estante_disciplina_n_questoes2_ordenado.rename(columns = {'n_questoes':'Nº de questões'}, inplace = True)
#questoes_estante_disciplina_n_questoes2_ordenado

fig1 = px.bar(questoes_estante_disciplina_n_questoes2_ordenado, x='Nº de questões', y='Disciplina')
fig1.update_layout(showlegend=False,
                    title="Número de questões por disciplina",
                    title_x=0.5,
                    xaxis_title='Nº de questões',
                    yaxis_title='Disciplina')
st.plotly_chart(fig1)


# In[25]:


st.markdown('**Tópico 3.7: Número de questões por fonte**')

questoes_estante_fonte = pd.read_excel('questoes_estante_fonte.xlsx')
#questoes_estante_fonte


# In[26]:


questoes_estante_fonte2 = questoes_estante_fonte.drop(columns=['Unnamed: 0'])
#questoes_estante_fonte2

questoes_estante_fonte_n_questoes = questoes_estante_fonte2.groupby(['name']).count().reset_index()
questoes_estante_fonte_n_questoes.rename(columns = {'id':'n_questoes'}, inplace=True)
questoes_estante_fonte_n_questoes2 = questoes_estante_fonte_n_questoes.drop(columns = ['created'])
questoes_estante_fonte_n_questoes2_ordenado = questoes_estante_fonte_n_questoes2.sort_values(by='n_questoes',ascending=True)
questoes_estante_fonte_n_questoes2_ordenado_filt = questoes_estante_fonte_n_questoes2_ordenado[questoes_estante_fonte_n_questoes2_ordenado['n_questoes'] > 2000] 
questoes_estante_fonte_n_questoes2_ordenado_filt.rename(columns = {'name':'Fonte'}, inplace = True)
questoes_estante_fonte_n_questoes2_ordenado_filt.rename(columns = {'n_questoes':'Nº de questões'}, inplace = True)
#questoes_estante_fonte_n_questoes2_ordenado_filt

fig1 = px.bar(questoes_estante_fonte_n_questoes2_ordenado_filt, x='Nº de questões', y='Fonte')
fig1.update_layout(showlegend=False,
                    title="Número de questões por fonte",
                    title_x=0.5,
                    xaxis_title='Nº de questões',
                    yaxis_title='Fonte')
st.plotly_chart(fig1)


# In[27]:


st.markdown('**Tópico 3.8: Número de tags por questão**')

questoes_estante_ntags = pd.read_excel('questoes_estante_ntags.xlsx')
#questoes_estante_ntags


# In[28]:


questoes_estante_ntags2 = questoes_estante_ntags.drop(columns=['Unnamed: 0','id'])
#questoes_estante_ntags2

questoes_estante_ntags3 = questoes_estante_ntags2.groupby(['count']).count().reset_index()
questoes_estante_ntags3.rename(columns = {'count':'Número de tags','created':'Número de questões'}, inplace = True)
#questoes_estante_ntags3

fig1 = px.bar(questoes_estante_ntags3, x='Número de tags', y='Número de questões')
fig1.update_layout(showlegend=False,
                    title="Número de tags por questão",
                    title_x=0.5,
                    xaxis_title='Número de tags',
                    yaxis_title='Número de questões')
st.plotly_chart(fig1)


# In[29]:


st.subheader('**Capítulo 4: Dados brutos acerca das Avaliações (Produto Diagnóstiqo)**')


# In[30]:


st.markdown('**Tópico 4.1: Números de avaliações criadas**')

numero_avaliacoes = pd.read_excel('numero_avaliacoes.xlsx')
#numero_avaliacoes


# In[31]:


numero_avaliacoes2 = numero_avaliacoes.drop(columns=['Unnamed: 0','namespace','Segmento','name','grupo'])
#numero_avaliacoes2

numero_avaliacoes3 = numero_avaliacoes2.groupby(['creation']).count().reset_index()
numero_avaliacoes3.rename(columns = {'id':'Número de avaliações','creation':'Data'}, inplace = True)
#numero_avaliacoes3

fig1 = px.bar(numero_avaliacoes3, x='Data', y='Número de avaliações')
fig1.update_layout(showlegend=False,
                    title="Número de AAs criadas por dia",
                    title_x=0.5,
                    xaxis_title='Data',
                    yaxis_title='Número de avaliações')
st.plotly_chart(fig1)


# In[32]:


st.markdown('**Tópico 4.2: Números de questões**')

numero_questoes_tipo = pd.read_excel('numero_questoes_tipo.xlsx')
#numero_questoes_tipo


# In[33]:


numero_questoes_tipo2 = numero_questoes_tipo.drop(columns=['Unnamed: 0','namespace','Segmento','name','grupo','id','creation'])
#numero_questoes_tipo2

numero_questoes_tipo3 = numero_questoes_tipo2.groupby(['date_trunc']).sum().reset_index()
numero_questoes_tipo3.rename(columns = {'date_trunc':'Mês'}, inplace = True)

#numero_questoes_tipo3

fig1 = px.bar(numero_questoes_tipo3, x='Mês', y=['Múltipla Escolha','Discursiva','Resposta Curta'])
fig1.update_layout(showlegend=True,
                    title="Número de questões por tipo",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Número de questões')
st.plotly_chart(fig1)


# In[34]:


st.markdown('**Tópico 4.3: Engajamento médio dos alunos**')

engajamento_medio_aa = pd.read_excel('engajamento_medio_aa.xlsx')
#engajamento_medio_aa


# In[35]:


engajamento_medio_aa2 = engajamento_medio_aa.drop(columns=['Unnamed: 0','namespace','Segmento','name','grupo','id','creation','Resposta Curta','Discursiva','Múltipla Escolha'])
#engajamento_medio_aa2

engajamento_medio_aa3 = engajamento_medio_aa2.groupby(['date_trunc']).sum().reset_index()
engajamento_medio_aa3['Engajamento'] = engajamento_medio_aa3['Alunos presentes']/engajamento_medio_aa3['Total de alunos'] 
engajamento_medio_aa4 = engajamento_medio_aa3.drop(columns = ['Alunos presentes','Total de alunos'])
engajamento_medio_aa4.rename(columns = {'date_trunc':'Mês'}, inplace = True)
#engajamento_medio_aa4

fig1 = px.bar(engajamento_medio_aa4, x='Mês', y='Engajamento')
fig1.update_layout(showlegend=False,
                    title="Engajamento médio dos alunos",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Engajamento')
st.plotly_chart(fig1)


# In[36]:


st.markdown('**Tópico 4.4: Tempo médio dos alunos**')

tempo_aa = pd.read_excel('tempo_aa.xlsx')
#tempo_aa


# In[37]:


tempo_aa2 = tempo_aa.drop(columns=['Alunos presentes','Duração','Total de alunos','Unnamed: 0','namespace','Segmento','name','grupo','id','creation','Resposta Curta','Discursiva','Múltipla Escolha'])
#tempo_aa2

tempo_aa3 = tempo_aa2.groupby(['date_trunc']).sum().reset_index()
tempo_aa3['Tempo em AA'] = tempo_aa3['Tempo em AA']/3600
tempo_aa3.rename(columns = {'date_trunc':'Mês'}, inplace = True)
#tempo_aa3

fig1 = px.bar(tempo_aa3, x='Mês', y='Tempo em AA')
fig1.update_layout(showlegend=False,
                    title="Tempo dos alunos em AA",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Horas')
st.plotly_chart(fig1)


# In[38]:


st.subheader('**Capítulo 5: Dados brutos acerca dos cadernos (Produto Pedagógiqo)**')


# In[39]:


st.markdown('**Tópico 5.1: Número de cadernos criados**')

numero_cadernos = pd.read_excel('numero_cadernos.xlsx')
#numero_cadernos


# In[40]:


numero_cadernos2 = numero_cadernos.drop(columns=['Unnamed: 0','namespace','Segmento','name','grupo','creation'])
#numero_cadernos2

numero_cadernos3 = numero_cadernos2.groupby(['date_trunc']).count().reset_index()
numero_cadernos3.rename(columns = {'date_trunc':'Mês','id':'Número de cadernos'}, inplace = True)
#numero_cadernos3

fig1 = px.bar(numero_cadernos3, x='Mês', y='Número de cadernos')
fig1.update_layout(showlegend=False,
                    title="Criação de cadernos",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Número de cadernos')
st.plotly_chart(fig1)


# In[41]:


st.markdown('**Tópico 5.2: Número de materiais nos cadernos**')

numero_materiais_cadernos_parte1 = pd.read_excel('numero_materiais_cadernos_parte1.xlsx')
#numero_materiais_cadernos_parte1

numero_materiais_cadernos_parte2 = pd.read_excel('numero_materiais_cadernos_parte2.xlsx')
#numero_materiais_cadernos_parte2


# In[42]:


numero_materiais_cadernos = numero_materiais_cadernos_parte1.append(numero_materiais_cadernos_parte2)
#numero_materiais_cadernos

numero_materiais_cadernos2 = numero_materiais_cadernos.drop(columns=['Unnamed: 0','namespace','Segmento','name','grupo','creation','id_conteudo','Mês'])
#numero_materiais_cadernos2

numero_materiais_cadernos3 = numero_materiais_cadernos2.groupby(['kind']).count().reset_index()
numero_materiais_cadernos3.rename(columns = {'id':'Número de materiais','kind':'Tipo de material'}, inplace = True)
#numero_materiais_cadernos3

numero_materiais_cadernos3['Tipo de material'] = numero_materiais_cadernos3['Tipo de material'].map({'ARTICLE':'Documento de texto',
                             'ASSIGNMENT':'Tarefa de casa',
                             'AUDIO':'Áudio',
                            'EXERCISELIST':'Lista de exercícios',
                             'GSLIDES':'Google Slides',
                            'PRESENTATION':'PDF',
                             'VIDEO':'Vídeo',
                            'VIDEOCONF':'Vídeoconferência',
                             'GDOCS':'Google Docs',
                            'GSHEETS':'Google Sheets'
                             },
                             na_action=None)

numero_materiais_cadernos10 = numero_materiais_cadernos3.sort_values(by = 'Tipo de material')
fig1 = px.bar(numero_materiais_cadernos10, x='Tipo de material', y='Número de materiais', color="Tipo de material", color_discrete_sequence=["turquoise","red", "green", "blue", "orange", "yellow", "brown", "violet", "black","gray"])
fig1.update_layout(showlegend=False,
                    title="Número de materiais por tipo",
                    title_x=0.5,
                    xaxis_title='Tipo de material',
                    yaxis_title='Número de materiais',
                 )
#fig1.show()

st.plotly_chart(fig1)


# In[74]:


numero_materiais_cadernos4 = numero_materiais_cadernos.drop(columns=['Unnamed: 0','namespace','Segmento','name','grupo','creation','id_conteudo','creation'])
#numero_materiais_cadernos4

numero_materiais_cadernos5 = numero_materiais_cadernos4.groupby(['kind','Mês']).count().reset_index()
numero_materiais_cadernos5.rename(columns = {'id':'Número de materiais','kind':'Tipo de material'}, inplace = True)

numero_materiais_cadernos5['Tipo de material'] = numero_materiais_cadernos5['Tipo de material'].map({'ARTICLE':'Documento de texto',
                             'ASSIGNMENT':'Tarefa de casa',
                             'AUDIO':'Áudio',
                            'EXERCISELIST':'Lista de exercícios',
                             'GSLIDES':'Google Slides',
                            'PRESENTATION':'PDF',
                             'VIDEO':'Vídeo',
                            'VIDEOCONF':'Vídeoconferência',
                             'GDOCS':'Google Docs',
                            'GSHEETS':'Google Sheets'
                             },
                             na_action=None)

numero_materiais_cadernos8 = numero_materiais_cadernos5.sort_values(by = 'Tipo de material')

fig2 = px.bar(numero_materiais_cadernos8, x='Mês', y='Número de materiais', color="Tipo de material", color_discrete_sequence=["turquoise","red", "green", "blue", "orange", "yellow", "brown", "violet", "black","gray"])
fig2.update_layout(showlegend=True,
                    title="Número de materiais por tipo",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Número de materiais',
                 )

#fig2.show()

st.plotly_chart(fig2)

numero_materiais_cadernos6 = numero_materiais_cadernos5.groupby(['Mês']).sum().reset_index()
numero_materiais_cadernos7 = pd.merge(numero_materiais_cadernos5,numero_materiais_cadernos6, on = ['Mês'], how = 'outer')
numero_materiais_cadernos7['Porcentagem'] = numero_materiais_cadernos7['Número de materiais_x']/numero_materiais_cadernos7['Número de materiais_y']
#numero_materiais_cadernos7

numero_materiais_cadernos9 = numero_materiais_cadernos7.sort_values(by = 'Tipo de material')

fig1 = px.bar(numero_materiais_cadernos9, x='Mês', y='Porcentagem', color="Tipo de material", color_discrete_sequence=["turquoise","red", "green", "blue", "orange", "yellow", "brown", "violet", "black","gray"])
fig1.update_layout(showlegend=True,
                    title="Número de materiais por tipo normalizado",
                    title_x=0.5,
                    xaxis_title='Mês',
                    yaxis_title='Porcentagem',
                 )
#fig1.show()

st.plotly_chart(fig1)


# In[ ]:


st.markdown('**Tópico 5.3: Engajamento nos cadernos**')

engajamento_caderno_parte1 = pd.read_excel('engajamento_caderno_parte1.xlsx')
#engajamento_caderno_parte1

engajamento_caderno_parte2 = pd.read_excel('engajamento_caderno_parte2.xlsx')
#engajamento_caderno_parte2


# In[ ]:


engajamento_cadernos = engajamento_caderno_parte1.append(engajamento_caderno_parte2)
engajamento_cadernos

engajamento_cadernos_disciplina2 = engajamento_cadernos.drop(columns=['id','Total de alunos','kind','owner_id','Unnamed: 0','namespace','Segmento','name','grupo','creation','id_conteudo','creation'])
engajamento_cadernos_disciplina3 = engajamento_cadernos_disciplina2[engajamento_cadernos_disciplina2['Engajamento'] > 0]
engajamento_cadernos_disciplina3

engajamento_cadernos_disciplina4 = engajamento_cadernos_disciplina3.groupby(['subject']).mean().reset_index()
engajamento_cadernos_disciplina4.rename(columns = {'subject':'Disciplina'}, inplace = True)
engajamento_cadernos_disciplina5 = engajamento_cadernos_disciplina4.sort_values(by = 'Disciplina', ascending = False)

fig1 = px.bar(engajamento_cadernos_disciplina5, x='Engajamento', y='Disciplina')
fig1.update_layout(showlegend=False,
                    title="Engajamento no cadernos por disciplina",
                    title_x=0.5,
                    xaxis_title='Engajamento',
                    yaxis_title='Disciplina')
fig1.update_xaxes(range=[0, 1])
#fig1.show()
st.plotly_chart(fig1)


# In[ ]:


engajamento_cadernos_segmento2 = engajamento_cadernos.drop(columns=['id','Total de alunos','kind','owner_id','Unnamed: 0','namespace','subject','name','grupo','creation','id_conteudo','creation'])
engajamento_cadernos_segmento3 = engajamento_cadernos_segmento2[engajamento_cadernos_segmento2['Engajamento'] > 0]
engajamento_cadernos_segmento3

engajamento_cadernos_segmento4 = engajamento_cadernos_segmento3.groupby(['Segmento']).mean().reset_index()

engajamento_cadernos_segmento4['Segmento'] = engajamento_cadernos_segmento4['Segmento'].map(
                            {'Ensino Infantil':'1 - Ensino Infantil',
                             'Ensino Fundamental I':'2 - Ensino Fundamental I',
                             'Ensino Fundamental II':'3 - Ensino Fundamental II',
                            'Ensino Médio':'4 - Ensino Médio',
                             'Outro':'5 - Outro'},
                             na_action=None)

engajamento_cadernos_segmento5 = engajamento_cadernos_segmento4.sort_values(by = 'Segmento', ascending = False)

fig1 = px.bar(engajamento_cadernos_segmento5, x='Engajamento', y='Segmento')
fig1.update_layout(showlegend=False,
                    title="Engajamento no cadernos por segmento",
                    title_x=0.5,
                    xaxis_title='Engajamento',
                    yaxis_title='Disciplina')
fig1.update_xaxes(range=[0, 1])
#fig1.show()
st.plotly_chart(fig1)


# In[ ]:


engajamento_cadernos_tipomaterial2 = engajamento_cadernos.drop(columns=['id','Total de alunos','Segmento','owner_id','Unnamed: 0','namespace','subject','name','grupo','creation','id_conteudo','creation'])
engajamento_cadernos_tipomaterial3 = engajamento_cadernos_tipomaterial2[engajamento_cadernos_tipomaterial2['Engajamento'] > 0]
engajamento_cadernos_tipomaterial3

engajamento_cadernos_tipomaterial4 = engajamento_cadernos_tipomaterial3.groupby(['kind']).mean().reset_index()
engajamento_cadernos_tipomaterial4.rename(columns = {'kind':'Tipo de material'}, inplace = True)
engajamento_cadernos_tipomaterial4['Tipo de material'] = engajamento_cadernos_tipomaterial4['Tipo de material'].map({'ARTICLE':'Documento de texto',
                             'ASSIGNMENT':'Tarefa de casa',
                             'AUDIO':'Áudio',
                            'EXERCISELIST':'Lista de exercícios',
                             'GSLIDES':'Google Slides',
                            'PRESENTATION':'PDF',
                             'VIDEO':'Vídeo',
                            'VIDEOCONF':'Vídeoconferência',
                             'GDOCS':'Google Docs',
                            'GSHEETS':'Google Sheets'
                             },
                             na_action=None)

engajamento_cadernos_tipomaterial5 = engajamento_cadernos_tipomaterial4.sort_values(by = 'Tipo de material')

fig1 = px.bar(engajamento_cadernos_tipomaterial5, x='Tipo de material', y='Engajamento', color="Tipo de material", color_discrete_sequence=["turquoise","red", "green", "blue", "orange", "yellow", "brown", "violet", "black","gray"])
fig1.update_layout(showlegend=False,
                    title="Engajamento no cadernos por tipo de material",
                    title_x=0.5,
                    xaxis_title='Tipo de material',
                    yaxis_title='Engajamento')
fig1.update_yaxes(range=[0, 1])
#fig1.show()
st.plotly_chart(fig1)


# In[47]:


st.subheader('**Capítulo 6: QBR**')


# In[65]:


st.markdown('**Tópico 6.1: Benefício 1: Alunos engajados, no seu próprio ritmo e recebendo feedback em tempo real**')

beneficio1_alunos_ativos = pd.read_excel('beneficio1_alunos_ativos.xlsx')
#beneficio1_alunos_ativos


# In[73]:


beneficio1_alunos_ativos2 = beneficio1_alunos_ativos.drop(columns = ['Segmento','Unnamed: 0','grupo','Rede'])
beneficio1_alunos_ativos2

beneficio1_alunos_ativos3 = beneficio1_alunos_ativos2.groupby(['namespace']).sum().reset_index()
beneficio1_alunos_ativos3 = beneficio1_alunos_ativos3[beneficio1_alunos_ativos3['Alunos presentes'] > 0] 
beneficio1_alunos_ativos3['Porcentagem'] = beneficio1_alunos_ativos3['Alunos presentes']/beneficio1_alunos_ativos3['Total de alunos']

beneficio1_alunos_ativos4 = beneficio1_alunos_ativos3.sort_values(by = 'Porcentagem', ascending = False).reset_index()
beneficio1_alunos_ativos5 = beneficio1_alunos_ativos4.drop(columns = ['index'])
beneficio1_alunos_ativos5.rename(columns = {'namespace':'Namespace'}, inplace = True)
beneficio1_alunos_ativos5

st.dataframe(beneficio1_alunos_ativos5)

