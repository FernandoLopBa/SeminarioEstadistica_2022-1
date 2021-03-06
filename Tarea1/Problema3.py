# -*- coding: utf-8 -*-
"""Tarea 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HhcBxTROobfWiMf16vFLjk5AOQUvSJQ8
"""
# Importamos las librerías necesarias para calcular el modelo de regresión lineal 
import pandas as pd
import numpy as np
# Exportamos la base correspondiente a las 3 empresas; el monto de sustancia que sobra dependiendo el número de horas que se estuvo usando el aparato A,B,C 
bd="/content/lineal_horm.xlsx"
bd_horm=pd.read_excel(bd)
bd_horm

# Librería para ajustar una proyección lineal
from sklearn import linear_model
reg = linear_model.LinearRegression()

a= bd_horm[0:9]
b= bd_horm[9:18]
c= bd_horm[18:27]

#Empresa A
a1=a[["horas"]]

# Empresa A
a1 = a[["horas"]] 
y_a = a[["monto"]]
#Función que recibe la información con la cual entrenaré al modelo
reg.fit(a1, y_a) 
reg.coef_ 
reg.intercept_
#Deuelve valores que se generaron con el modelo lineal tomando en cuenta la variable 'horas'
Y_a_pred = reg.predict(a1)
y_estim_a= Y_a_pred.reshape(-1)
y_estim_a

x_a=a1.to_numpy().reshape(-1)
x_a

# Datos reales
y_real_a=y_a.to_numpy()
y_real_a=y_real_a.reshape(-1)
y_real_a
n=len(y_real_a)
y_real_a
#Diferencia entre la estimación que se obtuvo con el modelo de regresión lineal y los datos reales 
residual_a=y_real_a-y_estim_a
residual_a

# Obtener el error estándar del estimador beta usando:

"""$$
\begin{equation}
\hat{se}_{\beta}=\sqrt{\frac{\sum_{i} \epsilon_{i}^{2}}{(n-2)\sum_{i}(x-\bar{x})^{2}}}
\end{equation}
$$
"""

reg=linear_model.LinearRegression

A1=a1.to_numpy().reshape(-1)
A1

y_A=y_a.to_numpy().reshape(-1)
y_A

df=pd.DataFrame(y_A,
                columns=['monto'])
df['horas']=A1
df



from sklearn import linear_model

reg=linear_model.LinearRegression()

X=df[["horas"]]
y=df[["monto"]]
reg.fit(X,y)

reg.coef_

reg.intercept_

#Hacemos primero unos primeros estimadores de las betas utilizando una
#muestra bootstrap para "probar" la regresión en la cía. A
horas_1=np.random.choice(A1, len(A1), replace=True)
df_aux1=pd.DataFrame(horas_1, columns=['horas'])
df_aux1=pd.merge(df_aux,df,how="inner", on=['horas'])
df_aux
X_1=df_aux[["horas"]]
y_1=df_aux[["monto"]]
reg_1=linear_model.LinearRegression() 
reg_1.fit(X,y)
reg_1.coef_

#Hacemos 1000 simulaciones de muestras bootstrap del mismo tamaño que
#los datos con los que contamos y con cada una de ellas 
#calculamos un estimador para la betas de la regresión lineal de monto vs
#horas para la cía. A
simul=1000
beta1_boost=np.array([])
beta0_boost=np.array([])
for i in range(0,simul):
  horas_i=np.random.choice(A1, len(A1), replace=True)
  df_aux=pd.DataFrame(horas_i, columns=['horas'])
  df_aux=pd.merge(df_aux,df,how="inner", on=['horas'])
  df_aux
  X=df_aux[["horas"]]
  y=df_aux[["monto"]]
  reg_i=linear_model.LinearRegression() 
  reg_i.fit(X,y)
  beta1_boost=np.append(beta1_boost,reg_i.coef_)
  beta0_boost=np.append(beta0_boost,reg_i.intercept_)

#Construimos un dataframe que contenga los betas estimados con cada una
#de las muestras bootstrap anteriores
betas=pd.DataFrame(beta1_boost,
                columns=['beta_1'])
betas['beta_0']=beta0_boost
betas

#Obtenemos el error estandar 
media_beta1=np.mean(betas["beta_1"])
media_beta1
num=np.sum((betas["beta_1"]-media_beta1)**2)
denom=simul-1
se_beta1=np.sqrt(num/denom)
se_beta1

#Tenemos aquí la media de los estimadores de beta1 con las muestras
#bootstrap anteriores
media_beta1

#Obtenemos el cociente de la media de los estimadores de beta 1:
#Este valor nos dice que tienen una buena presición nuestros estimadores,
#pues la media es en valor absoluto más de 9.5 veces el error estandar
#eso nos dice que el modelo tiene significancia
media_beta1/se_beta1

media_beta0=np.mean(betas["beta_0"])
media_beta0
num=np.sum((betas["beta_0"]-media_beta0)**2)
denom=simul-1
se_beta0=np.sqrt(num/denom)
se_beta0
media_beta0
media_beta0/se_beta0



simul=1000
beta1c_boost=np.array([])
beta0c_boost=np.array([])
for i in range(0,simul):
  horas_i=np.random.choice(A1, 10, replace=True)
  df_aux=pd.DataFrame(horas_i, columns=['horas'])
  df_aux=pd.merge(df_aux,df,how="inner", on=['horas'])
  df_aux
  X=df_aux[["horas"]]
  y=df_aux[["monto"]]
  reg_i=linear_model.LinearRegression() 
  reg_i.fit(X,y)
  beta1c_boost=np.append(beta1_boost,reg_i.coef_)
  beta0c_boost=np.append(beta0_boost,reg_i.intercept_)

betasc=pd.DataFrame(beta1c_boost,
                columns=['beta_1'])
betasc['beta_0']=beta0c_boost
betasc

media_beta1c=np.mean(betasc["beta_1"])
media_beta1c
num=np.sum((betasc["beta_1"]-media_beta1c)**2)
denom=simul-1
se_beta1c=np.sqrt(num/denom)
se_beta1c

media_beta0c=np.mean(betasc["beta_0"])
media_beta0c
num=np.sum((betasc["beta_0"]-media_beta0c)**2)
denom=simul-1
se_beta0c=np.sqrt(num/denom)
se_beta0c

media_beta0c

media_beta0c/se_beta0c

B1=b1.to_numpy().reshape(-1)
B1

y_B=y_b.to_numpy().reshape(-1)
y_B

df2=pd.DataFrame(y_B,
                columns=['monto'])
df2['horas']=B1
df2

# Empresa B

b1 = b[["horas"]]
y_b = b[["monto"]]
reg.fit(b1, y_b)
reg.coef_
reg.intercept_

Y_b_pred = reg.predict(b1)
y_estim_b= Y_b_pred.reshape(-1)
y_estim_b

x_b=b1.to_numpy().reshape(-1)
x_b

y_real_b=y_b.to_numpy()
y_real_b=y_real_b.reshape(-1)
y_real_b
n=len(y_real_b)
y_real_b

residual_b=y_real_b-y_estim_b
residual_b

simul=1000
beta1_boost_B=np.array([])
beta0_boost_B=np.array([])
for i in range(0,simul):
  horas_i=np.random.choice(B1, len(B1), replace=True)
  df_aux=pd.DataFrame(horas_i, columns=['horas'])
  df_aux=pd.merge(df_aux,df2,how="inner", on=['horas'])
  df_aux
  X=df_aux[["horas"]]
  y=df_aux[["monto"]]
  reg_i=linear_model.LinearRegression() 
  reg_i.fit(X,y)
  beta1_boost_B=np.append(beta1_boost,reg_i.coef_)
  beta0_boost_B=np.append(beta0_boost,reg_i.intercept_)

betas_B=pd.DataFrame(beta1_boost_B,
                columns=['beta_1'])
betas_B['beta_0']=beta0_boost_B
betas_B

# Empresa C
c1 = c[["horas"]]
y_c = c[["monto"]]

reg.fit(c1, y_c)
reg.coef_
reg.intercept_

Y_c_pred = reg.predict(c1)
y_estim_c= Y_c_pred.reshape(-1)
y_estim_c

x_c=c1.to_numpy().reshape(-1)
x_c

y_real_c=y_c.to_numpy()
y_real_c=y_real_c.reshape(-1)
y_real_c
n=len(y_real_c)
y_real_c

residual_c=y_real_c-y_estim_c
residual_c

# Calculamos el error estándar de las betas con 1000 simulaciones para la empresa C
simul=1000
beta1_boost_C=np.array([])
beta0_boost_C=np.array([])

for i in range(0,simul):
  horas_i=np.random.choice(c1, len(c1), replace=True)
  df_aux=pd.DataFrame(horas_i, columns=['horas'])
  df_aux=pd.merge(df_aux,df,how="inner", on=['horas'])
  df_aux

  X=df_aux[["horas"]]
  y=df_aux[["monto"]]

  reg_i=linear_model.LinearRegression() 
  reg_i.fit(X,y)

  beta1_boost_C=np.append(beta1_boost,reg_i.coef_)
  beta0_boost_C=np.append(beta0_boost,reg_i.intercept_)

betas_C=pd.DataFrame(beta1_boost_C,
                columns=['beta_1'])
betas_C['beta_0']=beta0_boost_C
betas_C
