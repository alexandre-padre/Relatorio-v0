#!/usr/bin/env python
# coding: utf-8

# In[190]:


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


# In[319]:


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


# In[288]:


st.image('[LOGO] Eduqo.png')

st.title('Relatório de uso da plataforma QMágico')

image = Image.open('[LOGO] Eduqo.png')
st.sidebar.image(image,caption='Eduqo - Plataforma QMágico',use_column_width=True)

st.sidebar.markdown('Feito por : Alexandre Fernandes (Padre)')


# In[193]:


st.subheader('**Capítulo 1**')


# In[194]:


st.subheader('**Capítulo 2: Dados brutos acerca do tempo gasto pelos usuários ativos na plataforma**')


# In[195]:


st.markdown('**Tópico 2.1: Alunos**')

alunos_tempo = pd.read_excel('alunos_tempo.xlsx')
#alunos_tempo


# In[343]:


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


# In[197]:


st.markdown('**Tópico 2.2: Professores**')

professores_tempo = pd.read_excel('professores_tempo.xlsx')
#professores_tempo


# In[338]:


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


# In[199]:


st.markdown('**Tópico 2.3: Administradores**')

admin_tempo = pd.read_excel('administradores_tempo.xlsx')
#admin_tempo


# In[342]:


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


# In[201]:


st.subheader('**Capítulo 3: Dados brutos acerca do Banco de Questões Eduqo (Produto Banqo)**')
#st.markdown('Nesse capítulo estão presentes as análises acerca do uso do **Banco de questões (Produto Banqo)**')


# In[202]:


st.markdown('**Tópico 3.1: Número de questões**')

questoes_estante = pd.read_excel('questoes_estante.xlsx')
#questoes_estante


# In[351]:


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


# In[204]:


st.markdown('**Tópico 3.2: Número de questões EM**')

questoes_estante_em = pd.read_excel('questoes_estante_em.xlsx')
#questoes_estante_em


# In[353]:


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


# In[206]:


st.markdown('**Tópico 3.3: Número de questões EF2**')

questoes_estante_ef2 = pd.read_excel('questoes_estante_ef2.xlsx')
#questoes_estante_ef2


# In[354]:


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


# In[208]:


st.markdown('**Tópico 3.4: Número de questões EF1**')

questoes_estante_ef1 = pd.read_excel('questoes_estante_ef1.xlsx')
#questoes_estante_ef1


# In[355]:


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


# In[210]:


st.markdown('**Tópico 3.5: Número de questões BNCC**')

questoes_estante_bncc = pd.read_excel('questoes_estante_bncc.xlsx')
#questoes_estante_bncc


# In[356]:


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


# In[237]:


st.markdown('**Tópico 3.6: Número de questões por disciplina**')

questoes_estante_disciplina = pd.read_excel('questoes_estante_disciplina.xlsx')
#questoes_estante_disciplina


# In[358]:


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


# In[262]:


st.markdown('**Tópico 3.7: Número de questões por vestibular**')

questoes_estante_fonte = pd.read_excel('questoes_estante_fonte.xlsx')
#questoes_estante_fonte


# In[363]:


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

