#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:21:15 2018

@author: esmeraldaarriaga
"""

from dbfread import DBF as DB
import pandas as pd
#%% Frames
Tables = []
for f in ['tmodulo1.dbf','tmodulo2.dbf','tmodulo2.dbf','tmodulo3.dbf','Tvivienda.dbf','tsdem.dbf']:
    Tables.append(pd.DataFrame(iter(DB(f))))

data_file='bobjetivo.csv'
credit=pd.read_csv(data_file,header=None, encoding='utf-8')
#LOS RESULTADOS SON CERCANOS
# Pregunta 3.11 Tiene celular: si=1 no=2 porcentaje en reporte 
#porcentaje real 74.9%
total=len(Tables[0]["P3_11"]=="1")
si=sum(Tables[0]["P3_11"]=="1")
porcentaje=(si/total)*100

#LOS RESULTADOS SON CERCANOS
# Pregunta 3.4 Grado de escolaridad
#0 ninguno 1 kinder 2 primaria 3 secundaria 4 secundaria tecnica
#5 normal basica 6 prepa 7 prepa tecnica 8 licenciatura 9 maestria
ninguno=sum(Tables[0]["NIV"]=="0")/len(Tables[0]["NIV"])# real 3.7%
kinder=sum(Tables[0]["NIV"]=="1")/len(Tables[0]["NIV"])# real .1%
primaria=sum(Tables[0]["NIV"]=="2")/len(Tables[0]["NIV"])# real 24.8%
secu=sum(Tables[0]["NIV"]=="3")/len(Tables[0]["NIV"])# real 27.9%
secutec=sum(Tables[0]["NIV"]=="4")/len(Tables[0]["NIV"])# real 2.5%
normb=sum(Tables[0]["NIV"]=="5")/len(Tables[0]["NIV"])# real .1%
prepa=sum(Tables[0]["NIV"]=="6")/len(Tables[0]["NIV"])# real 18.6%
prepatec=sum(Tables[0]["NIV"]=="7")/len(Tables[0]["NIV"])# real 2.9%
lic=sum(Tables[0]["NIV"]=="8")/len(Tables[0]["NIV"])# real 17.6%
maestria=sum(Tables[0]["NIV"]=="9")/len(Tables[0]["NIV"])# real 1.8%

#LOS RESULTADOS NO SON CERCANOS
# Pregunta 5.6 Cual es la razon por la que no tiene una cuenta bancaria
#1 no le interesa, 2 no le alcanza, sus ingresos son insuficientes o variables
#3 Los intereses son bajos o las comisiones son altas, 4 piden requisitos que no tiene
#5 prefiere otras formas de ahorro (tanda, guardar en su casa), 6 no las necesita
#7 no confia en las instituciones financieras o le dan mal servicio
#8 la sucursal le queda lejos o no hay, 9 otro

op1=(sum(Tables[0]["P5_6"]=="1")/len(Tables[0]["P5_6"]))*100#real 11.3%
op2=(sum(Tables[0]["P5_6"]=="2")/len(Tables[0]["P5_6"]))*100#real 49.9%
op3=(sum(Tables[0]["P5_6"]=="3")/len(Tables[0]["P5_6"]))*100#real 2%
op4=(sum(Tables[0]["P5_6"]=="4")/len(Tables[0]["P5_6"]))*100#real 6.1%
op5=(sum(Tables[0]["P5_6"]=="5")/len(Tables[0]["P5_6"]))*100#real 6.4%
op6=(sum(Tables[0]["P5_6"]=="6")/len(Tables[0]["P5_6"]))*100#real 8.7%
op7=(sum(Tables[0]["P5_6"]=="7")/len(Tables[0]["P5_6"]))*100#real 4.1%
op8=(sum(Tables[0]["P5_6"]=="8")/len(Tables[0]["P5_6"]))*100#real 0.7%
op9=(sum(Tables[0]["P5_6"]=="9")/len(Tables[0]["P5_6"]))*100#real 11.1%
razones=Tables[0]["P5_6A"][Tables[0]["P5_6A"]!=""]#en la siguiente columna se escribe la razon de otros


num=credit[0]=="P5_6"
op1=float(sum(Tables[0]["P5_6"]=="1")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 11.3%
op2=float(sum(Tables[0]["P5_6"]=="2")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 49.9%
op3=float(sum(Tables[0]["P5_6"]=="3")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 2%
op4=float(sum(Tables[0]["P5_6"]=="4")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 6.1%
op5=float(sum(Tables[0]["P5_6"]=="5")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 6.4%
op6=float(sum(Tables[0]["P5_6"]=="6")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 8.7%
op7=float(sum(Tables[0]["P5_6"]=="7")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 4.1%
op8=float(sum(Tables[0]["P5_6"]=="8")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 0.7%
op9=float(sum(Tables[0]["P5_6"]=="9")/(((len(Tables[0]["P5_6"])*credit[1][num])/76157088))*100)#real 11.1%
razones=Tables[0]["P5_6A"][Tables[0]["P5_6A"]!=""]#en la siguiente columna se escribe la razon de otros

#LOS RESULTADOS NO SON CERCANOS
# Pregunta 8.3 En que Afore se encuentra registrado
#1 banorte, 2 banamex, 3 coopel, 4 sura, 5 profuturo
#6 principal, 7 pensionISSTE, 8 otro, 9 no sabe
num=credit[0]=="P8_3"
p1=float(sum(Tables[1]["P8_3"]=="1")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 16.5%
p2=float(sum(Tables[1]["P8_3"]=="2")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 13.9%
p3=float(sum(Tables[1]["P8_3"]=="3")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 15.2%
p4=float(sum(Tables[1]["P8_3"]=="4")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 4.6%
p5=float(sum(Tables[1]["P8_3"]=="5")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 4.9%
p6=float(sum(Tables[1]["P8_3"]=="6")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 1.8%
p7=float(sum(Tables[1]["P8_3"]=="7")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 3.8%
p8=float(sum(Tables[1]["P8_3"]=="8")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 19.4%
p9=float(sum(Tables[1]["P8_3"]=="9")/((len(Tables[1]["P8_3"])*credit[1][num])/76157088))#real 19.9%

#%% cualquier pregunta
def porcentaje(pregunta,inciso):
    num=credit[0]==pregunta
    p=float(sum(Tables[1][pregunta]==inciso)/((len(Tables[1][pregunta])*credit[1][num])/76157088))
    return p

preg="P8_3"
inc="1"

p1=porcentaje(preg,inc)

#%% preguntas multiples
#3.9 ingreso fijo 1, 3.12 smartphone 1, 4.8 efectivo 1 # 24.25%
#3.9 ingreso fijo 1, 3.12 smartphone 1, 4.8 tarjeta de debito 2 # 3.25%
#3.9 ingreso fijo 1, 3.12 smartphone 1, 4.8 tarjeta de credito 3 # 1.75%
#3.9 ingreso variable 2, 3.12 smartphone 1, 4.8 efectivo 1 # 21.40%
#3.9 ingreso fijo 1, 3.12 no smartphone 2, 4.8 efectivo 1 # 9.99%
#3.9 ingreso variable 2, 3.12 no smartphone 2, 4.8 efectivo 1 # 15.88%

ej2=Tables[0].groupby(['P3_9', 'P3_12','P4_8']).size().reset_index(name='count')
pobj=credit.loc[credit[0].isin(['P3_9','P3_12','P4_8'])].min()
preguntas=['P3_9', 'P3_12','P4_8']
incisos=['2', '1','1']
def porcentaje(tabla,pobjet,preg,inc):
    num=pobjet[1]
    t=tabla[(tabla[preg[0]]==inc[0]) & (tabla[preg[1]]==inc[1]) & (tabla[preg[2]]==inc[2])]
    p=float(t['count']/((tabla['count'].sum()*num)/76157088))
    return p

p1=porcentaje(ej2,pobj,preguntas,incisos)
p1num=(p1*pobj[1]) #ESTE ES EL BUENO

def numero(tabla,pobjet,preg,inc):
    num=pobjet[1]
    t=tabla[(tabla[preg[0]]==inc[0]) & (tabla[preg[1]]==inc[1]) & (tabla[preg[2]]==inc[2])]
    p=float((num*t['count'])/tabla['count'].sum())
    return p

p2=numero(ej2,pobj,preguntas,incisos)

#4.1 registro de gastos si 1 no 2
#4.5 le enseñaron a ahorrar si 1 no 2
#4.8 forma de pago efectivo 1 debito 2 credito 3 cheques 4
# 1 1 1  23.14%
# 1 1 2  2.46%
# 1 2 1  8.42%
# 2 1 1  36.39%
#pobj(min)  100%
# x         resultado
ej2=Tables[0].groupby(['P4_1', 'P4_5','P4_8']).size().reset_index(name='count')
pobj=credit.loc[credit[0].isin(['P4_1', 'P4_5','P4_8'])].min()
preguntas=['P4_1', 'P4_5','P4_8']
incisos=['2', '1','1']
p1=porcentaje(ej2,pobj,preguntas,incisos)


# pa la primaria
#3.12 smartphone 1, EDAD 20-30, 4.8 tarjeta de debito 2
ej2=Tables[0].groupby(['P3_12', 'EDAD','P4_8']).size().reset_index(name='count')
pobj=credit.loc[credit[0].isin(['P3_12', 'EDAD','P4_8'])].min()
preguntas=['P3_12', 'EDAD','P4_8']
incisos=['1', '20','2']
p1=porcentaje(ej2,pobj,preguntas,incisos)
p1num=(p1*pobj[1])

ej2=Tables[0].groupby(['P3_12', 'EDAD', 'P4_8']).size().reset_index(name='count')
pobj=credit.loc[credit[0].isin(['P3_12', 'EDAD','P4_8'])].min()
preguntas=['P3_12', 'EDAD', 'EDAD','P4_8','P4_8']
incisos=['1', '20', '30','3','2']

def porcentaje(tabla,pobjet,preg,inc):
    num=pobjet[1]
    t=tabla[(tabla[preg[0]]==inc[0]) & (tabla[preg[1]]>inc[1]) & (tabla[preg[2]]<inc[2]) & (tabla[preg[3]]==inc[3]) | (tabla[preg[3]]==inc[3])]
    p=float(t['count'].sum()/((tabla['count'].sum()*num)/76157088))
    return p

p1=porcentaje(ej2,pobj,preguntas,incisos)
p1num=(p1*pobj[1])

#1.23%, 706209
#0.75%, 428769


#que tengan whatsapp
#personas entre 20 y 30 porque tienen chamacos o buscar pregunta que si tienen hijos
#que su metodo de pago sea debito o credito






























