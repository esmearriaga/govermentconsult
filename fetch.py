# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:14:31 2018

@author: Tekken

Installar dbfread con pip y bajar la base de datos en formato .DBF de :http://www.beta.inegi.org.mx/contenidos/proyectos/enchogares/especiales/enif/2015/microdatos/enif_2015_bd_dbf.zip
"""
from dbfread import DBF as DB
import pandas as pd
#%% Frames
Tables = []
for f in ['tmodulo1.dbf','tmodulo2.dbf','tmodulo2.dbf','tmodulo3.dbf','Tvivienda.dbf','tsdem.dbf']:
    Tables.append(pd.DataFrame(iter(DB(f))))


#LOS RESULTADOS SON CERCANOS
# Pregunta 3.11 Tiene celular: si=1 no=2 porcentaje en reporte 
#porcentaje real 74.9%
total=len(Tables[0]["P3_11"]=="1")
si=sum(Tables[0]["P3_11"]=="1")
porcentaje=si/total

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
op1=sum(Tables[0]["P5_6"]=="1")/len(Tables[0]["P5_6"])#real 11.3%
op2=sum(Tables[0]["P5_6"]=="2")/len(Tables[0]["P5_6"])#real 49.9%
op3=sum(Tables[0]["P5_6"]=="3")/len(Tables[0]["P5_6"])#real 2%
op4=sum(Tables[0]["P5_6"]=="4")/len(Tables[0]["P5_6"])#real 6.1%
op5=sum(Tables[0]["P5_6"]=="5")/len(Tables[0]["P5_6"])#real 6.4%
op6=sum(Tables[0]["P5_6"]=="6")/len(Tables[0]["P5_6"])#real 8.7%
op7=sum(Tables[0]["P5_6"]=="7")/len(Tables[0]["P5_6"])#real 4.1%
op8=sum(Tables[0]["P5_6"]=="8")/len(Tables[0]["P5_6"])#real 0.7%
op9=sum(Tables[0]["P5_6"]=="9")/len(Tables[0]["P5_6"])#real 11.1%
razones=Tables[0]["P5_6A"][Tables[0]["P5_6A"]!=""]#en la siguiente columna se escribe la razon de otros

#LOS RESULTADOS NO SON CERCANOS
# Pregunta 8.3 En que Afore se encuentra registrado
#1 banorte, 2 banamex, 3 coopel, 4 sura, 5 profuturo
#6 principal, 7 pensionISSTE, 8 otro, 9 no sabe
p1=sum(Tables[1]["P8_3"]=="1")/len(Tables[1]["P8_3"])#real 16.5%
p2=sum(Tables[1]["P8_3"]=="2")/len(Tables[1]["P8_3"])#real 13.9%
p3=sum(Tables[1]["P8_3"]=="3")/len(Tables[1]["P8_3"])#real 15.2%
p4=sum(Tables[1]["P8_3"]=="4")/len(Tables[1]["P8_3"])#real 4.6%
p5=sum(Tables[1]["P8_3"]=="5")/len(Tables[1]["P8_3"])#real 4.9%
p6=sum(Tables[1]["P8_3"]=="6")/len(Tables[1]["P8_3"])#real 1.8%
p7=sum(Tables[1]["P8_3"]=="7")/len(Tables[1]["P8_3"])#real 3.8%
p8=sum(Tables[1]["P8_3"]=="8")/len(Tables[1]["P8_3"])#real 19.4%
p9=sum(Tables[1]["P8_3"]=="9")/len(Tables[1]["P8_3"])#real 19.9%




