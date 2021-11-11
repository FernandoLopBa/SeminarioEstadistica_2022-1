# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from collections import Counter
import numpy as np 
import pandas as pd 
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
import time

#Importar datos
ini_interna=pd.read_csv('base_ini_interna.csv')
ini_parte1=pd.read_csv('base_ini_parte1.csv')
ini_externa= pd.read_csv('base_ini_externa.txt', sep=" ")
comp_2=pd.read_csv('base_comportamiento_2.txt', sep=" ")
comp_3=pd.read_csv('base_comportamiento_3.csv')
inv=pd.read_csv('base_inversion.txt', sep=" ")
ini_interna_externa =pd.merge(ini_interna,pd.merge(ini_parte1,ini_externa))

#Analisis Descriptivo
    
    ##Inicial Interna
ini_interna.head()
#La Base Inicial Interna, cuenta con información del cliente dentro del Banco,
#está compuesta por id, fecha de inicio, componentes internos 1,2,3,4 y las 
#categorías 1,2,3. A continuación se presenta el análisis de cada una de las 
#columnas.


        #Fecha de Inicio
ini_interna["fecha_inicio"] = ini_interna["fecha_inicio"].astype("datetime64")
ini_interna["fecha_inicio"].groupby(ini_interna["fecha_inicio"].dt.year).count().plot(kind="bar", title="Solicitud de prestamos", color="cornflowerblue")
        
#Esta base de datos abarca los años 2016, 2017, 2018, 2019, 2020 y 2021
#La mayor información de clientes se encuentra en el año 2020, sin embargo no
#varía mucho respecto a los otros años, excepto con el año 2021, que tiene sentido, 
#pues aún no termina. 


        ##Comp_Interno1
#Pueden ser inversiones, depositos, captaciones del cliente, dentro del banco       
plt.hist(ini_interna["comp_interno1"])
plt.boxplot(ini_interna["comp_interno1"])
#No es claro cómo varían los datos en el histogrma, pues tenemos pocos datos 
# que son muy grandes, para una mejor visualización está el boxplot. 
#La mayoría de datos se encuentranentre 0 a 50,000. Además decidimos hacer
#un grafico circular, agrupando la información dentro de los interválos que consideramos
#relevantes que son {(0,100),(100,1000.1),(1000,20000),(2000,350,000)}

plt.hist(ini_interna["comp_interno1"][ini_interna["comp_interno1"].between(0,100, inclusive=False)])
plt.hist(ini_interna["comp_interno1"][ini_interna["comp_interno1"].between(100,1000, inclusive=False)])
plt.hist(ini_interna["comp_interno1"][ini_interna["comp_interno1"].between(1000,20000, inclusive=True)])
plt.hist(ini_interna["comp_interno1"][ini_interna["comp_interno1"].between(20000,350000, inclusive=False)])

x=sum(ini_interna["comp_interno1"].between(0,100, inclusive=True))
y=sum(ini_interna["comp_interno1"].between(100.01,1000, inclusive=True))
z=sum(ini_interna["comp_interno1"].between(1000.01,20000, inclusive=True))
w=sum(ini_interna["comp_interno1"].between(20000.01,300000, inclusive=True))
plt.pie([x,y,z,w],labels=["0-100","100-1000","1000-20000",">20000"],autopct="%1.1f%%", shadow=True, startangle=140)


        ##Comp_Interno2
#Caracteristica del producto que está solicitando el cliente, dentro del banco        
sns.set_style("whitegrid")
sns.countplot(x='comp_interno2',data=ini_interna, palette="tab20c")

#Encontramos que hay dos tipos, b0 y b1. La preferencia es por b1


        ##Comp_Interno3
        
plt.hist(ini_interna["comp_interno3"],color="cornflowerblue")
#Esta información va del 1 al 32, y la mayoría de datos se encuentra en el intervalo 
#(1,4)        
        ##Comp_Interno4
plt.hist(ini_interna["comp_interno4"],color="cornflowerblue")         
#Esta información va del 29 al 79, y la mayoría de datos se encuentra en el intervalo 
#(45,52)  
      
        ##Categoria1
plt.hist(ini_interna["categoria1"],color="cornflowerblue")    
#La mayoría de los clientes se encuentran en la categoria 1, y pocos en la 5

        ##Categoria2
plt.hist(ini_interna["categoria2"],color="cornflowerblue")    
#La mayoría de los clientes se encuentran en la categoria 8      

        ##Categoria3
plt.hist(ini_interna["categoria3"],color="cornflowerblue")    
#La mayoría de los clientes se encuentran en el intervalo (146,149)


#Por último, realizamos un diagrama de correlación 
    #Corelacción
int_corr=ini_interna.corr('pearson')
sns.heatmap(int_corr,cmap="coolwarm")

#Notamos que categoria 3 y componente interno 3 tienen una correlación positiva
#Componente 3 y Categoria 2, Categoria 2 y Categoria 3 tienen una correlación
#negativa




    ##Inicial Externa
#Información Externa del cliente    

        ##Comp_Externa1
plt.hist(ini_externa["comp_externo1"],color="salmon")
#Casi todos los datos se encuentran en 0
        ##Comp_Externo2
plt.hist(ini_externa["comp_externo2"],color="salmon")        
#Casi todos los datos se encuentran en 100
        ##Comp_Externo3
plt.hist(ini_externa["comp_externo3"],color="salmon") 
#Casi todos los datos se encuentran dentro de 100-150, también encontramos datos
#negativos, lo cuál nos puede indicar una deuda
        ##Comp_Externo4
plt.hist(ini_externa["comp_externo4"],color="salmon")
#Casi todos los datos se encuentran en 0

#Corelacción
ext_corr=ini_externa.corr('pearson')
sns.heatmap(ext_corr,cmap="coolwarm")
##Notamos que componente externo 3 y 4 tienen una correlación negativa



    ##Inversión
plt.hist(inv["inversion"],color="salmon") 
plt.boxplot(inv["inversion"])

x=sum(inv["inversion"].between(0,100, inclusive=True))
y=sum(inv["inversion"].between(100,1000, inclusive=True))
z=sum(inv["inversion"].between(1000,100000, inclusive=True))
w=sum(inv["inversion"]>100000)
plt.pie([x,y,z],labels=["0-100","100-1,000","1,000-100,000"],autopct="%1.1f%%", shadow=True, startangle=140)

#No es claro cómo varían los datos en el histogrma, pues tenemos pocos datos 
#que son muy grandes, para una mejor visualización está el boxplot. 
#La mayoría de datos se encuentranentre 0 a 10,000. Además decidimos hacer
#un grafico circular, agrupando la información dentro de los interválos que consideramos
#relevantes que son {(0,100),(100,1000),(1000,100,000)}

##Ahora vallamos con el analisis del comportamiento

comp_junta = pd.merge(comp_2,comp_3)
Caso_credito = comp_junta["num_caso"].unique().tolist()
a=list(range(1,int(max(comp_junta["Tiempo_aparicion"]+1))))
x=[]
y=[]
v=[]

#primer acercamiento para conocer el manejo de credito 
#Cuidado tiempo promedio de ejecucion 15 minutos
for i in Caso_credito:
    df_aux = comp_junta[comp_junta.num_caso == i]
    x.append(sum(df_aux["comportamiento_j"]>0)/len(df_aux["comportamiento_j"].tolist()))
    y.append(max(df_aux["comportamiento_j"]))
    v.append(int(max(df_aux["Tiempo_aparicion"])))
#Exploracion del indice de veces que se retrasaron en el pago vs vida total de su credito
dfplot = pd.DataFrame.from_dict(Counter(x), orient='index').reset_index()
plt.hist(dfplot["index"],15,color='blue', ec = 'black')
#Exploracion número maximo de meses que un cliente se retraso
dfplot = pd.DataFrame.from_dict(Counter(y), orient='index').reset_index()
plt.hist(dfplot["index"],10,color='blue', ec = 'black')
#Exploracion para saber la cantidad de meses que lleva con nosotros un cliente
dfplot = pd.DataFrame.from_dict(Counter(v), orient='index').reset_index()
plt.hist(dfplot["index"],100,color='blue', ec = 'black')
plt.bar(dfplot["index"],dfplot[0],color='blue', ec = 'black')



#Segunda exploracion, para ver algunas ventanas continuas de tiempo intentando
#catalogar si un cliente es malo o no
#Cuidado tiempo promedio de ejecución 10 horas :(
#Quitar el comentado y correr bajo su propio riesgo no nos hacemos responsables
#k=0
#z=[]
#
#for k in range(int(max(comp_junta["Tiempo_aparicion"]))):
#    aux = 0
#    for i in Caso_credito:
#        df_aux=comp_junta[comp_junta.num_caso == i]
#        if max(df_aux["Tiempo_aparicion"])-k<=0:
#                continue;
#        else:
#            for j in range(len(df_aux["num_caso"].tolist())-k):
#                df_aux = df_aux[df_aux.Tiempo_aparicion>=j]
#                df_aux2 = df_aux[df_aux.Tiempo_aparicion<=k+j]
#                if sum(df_aux2["comportamiento_j"]>0)==k+1:
#                    aux = aux+1
#                    break;
#    print('Paso ', k,' finalizado hora: ',time.ctime())
#    z.append(aux)


#Exploracion de cuantos clientes en una ventana continua de tiempo no hicieron un pago
#plt.bar(v,z) 

#Con lo anterior podemos observar que hay un decremento drástico de personas con 
#comportamiento_j siempre positivo entre las ventanas de tiempo de 3 y 4 meses, 

#Ahora veamos ¿que pasa con los datos de la primera explicarion de la vida 
#promedio de cada credito, con sacar algunos datos del vector v podremos explicar mas el 
#tipo de credito que se maneja.
v_medidas = np.percentile(v, [75,50,25,5])        


#El vector anterior nos arroja los 3 cuartiles, y el 5% para desprecias esos casos
#al ver que los cuartiles encierran al conjunto 47,60 suponemos que estos creditos
#son del tipo automotriz o similar, ahora con respecto a lo anterior restrinjamos nuestra
#evaluciación de los clientes unicamente a los que tengan 
Caso_credito_new = []

for i in Caso_credito:
    df_aux=comp_junta[comp_junta.num_caso == i]
    if(int(max(df_aux["Tiempo_aparicion"]))>v[3]):
        Caso_credito_new.append(i)
    else:
        continue;
#Ahora con toda la exploración intentaremos catalogar a los clientes buenos, con 1, a los malos 
#con 0, y a los clientes que no estan en la muestra anterior con 2 ya que los datos pueden ser 
#muy pocos como para poder catalogarlos de alguna u otra forma


#NOTA IMPORTANTE:

##¡A partir de este punto si es necesario ejecutar todo para poder tener el modelo #
Cliente_bueno = []
#Ahora con todo lo anterior explorado intentemos catalogar cuando un cliente es bueno o malo
#con el indice de veces que fallo, y solamente tomando en cuenta los clientes que tienen 
#tiempo de aparición mayor que v[3]
for i in Caso_credito:
    if(i in Caso_credito_new):
        df_aux=comp_junta[comp_junta.num_caso == i]
        if(sum(df_aux["comportamiento_j"]>0)/len(df_aux["comportamiento_j"]>.4)):
            Cliente_bueno.append(0)
        else:
            Cliente_bueno.append(1)
    else:
        Cliente_bueno.append(2)

CroosNC= pd.DataFrame(Caso_credito).join(pd.DataFrame(Cliente_bueno),lsuffix='_id_', rsuffix='Comp_final')
CroosNC= CroosNC.rename(columns = {'0_id_':'_id_','0Comp_final':'Comp_final'})

ini_final = pd.merge(ini_interna_externa,CroosNC)
#Como su nombre lo indica ini_final es nuestro conjunto de datos ya explorados y clasificados
#mientras que CrossNC es simplemente la clasificacion a cada numero de cliente.
#Ahora complementemos un poco mas el analisis ya observado con anterioridad
int_corr=ini_final.corr('pearson')
sns.heatmap(int_corr,cmap="coolwarm")


