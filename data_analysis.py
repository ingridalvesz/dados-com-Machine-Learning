import pandas as pd
import plotly.express as px

dados = pd.read_csv('marketing_investimento.csv')
dados 

dados.info() 

px.histogram(dados, x = 'aderencia_investimento', text_auto = True)

px.histogram(dados, x = 'estado_civil', text_auto = True, color = 'aderencia_investimento', barmode = 'group')

px.histogram(dados, x = 'escolaridade', text_auto = True, color = 'aderencia_investimento', barmode = 'group')

px.histogram(dados, x = 'inadimplencia', text_auto = True, color = 'aderencia_investimento', barmode = 'group')

px.histogram(dados, x = 'fez_emprestimo', text_auto = True, color = 'aderencia_investimento', barmode = 'group')

px.box(dados, x ='idade', color = 'aderencia_investimento')

px.box(dados, x ='saldo', color = 'aderencia_investimento')

px.box(dados, x ='tempo_ult_contato', color = 'aderencia_investimento')

px.box(dados, x = 'numero_contatos', color = 'aderencia_investimento')

dados 

x = dados.drop('aderencia_investimento', axis = 1)
y = dados['aderencia_investimento']

x

y

#%%