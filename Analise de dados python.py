#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd


# In[35]:


from matplotlib import pyplot as plt
from matplotlib import figure as f
import numpy as np
from sklearn.linear_model import LinearRegression


# In[36]:


dados = pd.read_csv('data-test-analytics.csv')


# In[99]:


dados


# In[38]:


dados.sort_values(by=['created_at'], inplace=True)


# In[39]:


dados.head()


# In[40]:


dados['Criado'] = 1


# In[ ]:





# In[ ]:





# In[41]:


dados['created_at'] = pd.to_datetime(dados['created_at'], errors='coerce')
dados['created_at_YM'] = dados['created_at'].dt.strftime('%Y%m')


# In[42]:


dados['deleted_at'] = pd.to_datetime(dados['deleted_at'], errors='coerce')
dados['deleted_at_YM'] = dados['deleted_at'].dt.strftime('%Y%m')


# In[43]:


Deletados = dados.groupby('deleted_at_YM')[['id']].count()
Deletados = Deletados.add_suffix('_Count').reset_index()


# In[44]:


Deletados


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[45]:


Deletados.columns = ['created_at_YM', 'Deletados']


# In[46]:


Deletados


# In[47]:


Churn = dados.groupby('created_at_YM')[['id']].count()
Churn = Churn.reset_index()


# In[48]:


Churn


# In[49]:


Churn = pd.merge(Churn, Deletados, on="created_at_YM")


# In[50]:


Churn.columns = ['created_at_YM', 'Criado', 'Deletados']
Churn


# In[51]:


Churn['DeletadoAcumulado'] = Churn['Deletados'].cumsum()


# In[52]:


Churn['CriadoAcumulado'] = Churn['Criado'].cumsum()


# In[53]:


Churn['SaldoAcumulado'] = Churn['CriadoAcumulado'] - Churn['DeletadoAcumulado']


# In[54]:


Churn


# In[55]:


start_date = "2017-01-01"
end_date = "2029-12-31"


# In[56]:


after_start_date = Churn["created_at_YM"] >= start_date
before_end_date = Churn["created_at_YM"] <= end_date


# In[57]:


between_two_dates = after_start_date & before_end_date


# In[58]:


Churn = Churn.loc[between_two_dates]


# In[59]:


Churn['Churn'] = Churn['Deletados']/Churn['SaldoAcumulado']


# In[60]:


Churn.head()


# In[61]:


Churn.tail()


# In[62]:


Churn['Churn'].plot(kind="bar")
plt.title('Subscriber Churn')
plt.xlabel('# of months from May, 2016')
plt.ylabel('Churn')
plt.show()


# In[63]:


Churn['Churn%'] = pd.Series(["{0:.2f}%".format(val * 100) for val in Churn['Churn']], index = Churn.index)


# In[64]:


Churn


# In[65]:


# O indicador apresenta crescimento. Matematicamente, ou a quantidade de novas assinaturas esta diminuindo e/ou
# a quantidade de cancelamentos esta aumentando. Demnonstrando sua regressao linear:


# In[66]:


Churn['X'] = np.arange(len(Churn))
Churn


# In[67]:


X = Churn.iloc[:, 8].values.reshape(-1, 1)


# In[68]:


Y = Churn.iloc[:, 6].values.reshape(-1, 1)


# In[69]:


linear_regressor = LinearRegression()


# In[70]:


linear_regressor.fit(X, Y)


# In[71]:


Churn_pred = linear_regressor.predict(X)


# In[ ]:





# In[72]:


print(linear_regressor.intercept_)


# In[73]:


Churn


# In[74]:


plt.scatter(X, Y)
plt.plot(X, Churn_pred, color='red')
plt.title('Subscriber Churn')
plt.xlabel('# of months from May, 2016')
plt.ylabel('Churn')
plt.show()


# In[75]:


print(linear_regressor.coef_)


# In[76]:


# Temos um grafico com os valores do Churn plotados ao longo do tempo e uma reta de regressao linear.
# É visivel uma inversao na tendencia dos valores a partir do mês 35, até onde se apresentava valores 
# praticiamente constantes no indicador.


# In[ ]:


# Diminuição de novas assinaturas e/ou o aumento de cancelamentos?


# In[ ]:


# Analisando novas assinaturas


# In[81]:


X = Churn.iloc[:, 8].values.reshape(-1, 1)
Y = Churn.iloc[:, 1].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Criadas_pred = linear_regressor.predict(X)
plt.scatter(X, Y)
plt.plot(X, Criadas_pred, color='red')
plt.title('Novos assinantes')
plt.xlabel('# of months from May, 2016')
plt.ylabel('Qtd')
plt.show()


# In[79]:


print(linear_regressor.coef_)


# In[ ]:


# Numero de novos assinantes permanece praticamente constante, com uma leve queda ao longo dos anos. 
# O baixo coeficiente de inclicacao -0,08 nos prova


# In[ ]:


# Então o numero de cancelamentos deve ser o principal item que elevou o valor do nosso indicador Churn


# In[112]:


X = Churn.iloc[:, 8].values.reshape(-1, 1)
Y = Churn.iloc[:, 2].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Deletadas_pred = linear_regressor.predict(X)
plt.scatter(X, Y)
plt.plot(X, Deletadas_pred, color='red')
plt.title('Assinaturas canceladas')
plt.xlabel('# of months from May, 2016')
plt.ylabel('Qtd')
plt.show()


# In[85]:


print(linear_regressor.coef_)


# In[ ]:


# Atraves da analise do quantitativo de pessoas que cancelaram as assinaturas, observamos o mesmo comportamento 
# do nosso indicador Churn.
# Os valores de crescimento no numero de cancelamentos se mantem crescente e constante ate cerca do mes 32 meses, ou seja,
# por volta do mes de Dezembro de 2018.


# In[ ]:


# Estaria relacionado ao aumento de precos?


# In[92]:


dados['X'] = np.arange(len(dados))
print(dados.columns)


# In[114]:


X = dados.iloc[:, 17].values.reshape(-1, 1)
Y = dados.iloc[:, 14].values.reshape(-1, 1)
linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Ticket_medio_pred = linear_regressor.predict(X)
plt.scatter(X, Y)
plt.plot(X, Ticket_medio_pred, color='red')
plt.title('Ticket Médio')
plt.xlabel('# de dias de inatividade')
plt.ylabel('Valor')
plt.show()


# In[ ]:


# Notamos o ticket médio constante, não indicando causa do aumento de cancelamentos relacionado com os preços.


# In[98]:


print(linear_regressor.coef_)


# In[ ]:


#Estaria relacionado a não utilização da assinatura? Ou seja, estaria as assinaturas sendo canceladas pelo fato de não #
#estar havendo compras?


# In[101]:


boxplot = dados.boxplot(column=['recency'], by=['status'])


# In[ ]:


# Aqui temos o real motivo do cancelamento. Observando valores médios para q quantidade de dias sem a utilização 
# da assinatura. Enquanto valores médios de dias sem utilização para contas ativas e pausadas 


# In[116]:


plt.scatter(dados.X, dados.average_ticket)
plt.title('Ticket Médio ao longo das dads de criação da assinatura')
plt.xlabel('meses')
plt.ylabel('Valor')
plt.show()


# In[ ]:


# Nota-se que parece não haver uma campanha de descontos progressiva, pois analisando dos dados de ticket médio ao longo dos
# meses, este se mantem constante. 


# In[117]:


plt.scatter(dados.recency, dados.average_ticket)
plt.title('Ticket Médio ao longo do dias de inatividade das contas')
plt.xlabel('dias de inatividade')
plt.ylabel('Valor')
plt.show()


# In[ ]:


# Ticket médio para os dias de inatividade das contas também se mantem constante. 
# Sugerir campanha de descontos progressivos, incentivando a compra, diminuindo o período de inatividade e assim
# evitando novos cancelamentos e impulsionando 


# In[ ]:




