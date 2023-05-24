#!/usr/bin/env python
# coding: utf-8

# ### -- Grafo de rutas --

# In[146]:


import networkx as nt
import matplotlib.pyplot as plt #solo es para dibujar el grafo
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
get_ipython().run_line_magic('matplotlib', 'inline')


# In[154]:


coordenadas = pd.read_excel("coordenadas.xlsx")
conx = pd.read_excel("coordenadas.xlsx", sheet_name="AristasSM")
R = nt.DiGraph()
print(coordenadas)#solo para verificar el contenido


# #### obtener distancias

# In[157]:


#Distancias de la ruta hacia ESTACION San Miguelito
distancia0 = str(geodesic(coordenadas.iloc[0,1], coordenadas.iloc[1,1]).km)
distancia1 = str(geodesic(coordenadas.iloc[1,1], coordenadas.iloc[2,1]).km)
distancia2 = str(geodesic(coordenadas.iloc[2,1], coordenadas.iloc[4,1]).km)
distancia3 = str(geodesic(coordenadas.iloc[2,1], coordenadas.iloc[3,1]).km)
distancia4 = str(geodesic(coordenadas.iloc[3,1], coordenadas.iloc[4,1]).km)
#Distancias de la ruta hacia El Dorado Mall
distancia5 = str(geodesic(coordenadas.iloc[0,1], coordenadas.iloc[6,1]).km)
distancia6 = str(geodesic(coordenadas.iloc[6,1], coordenadas.iloc[12,1]).km)
distancia7 = str(geodesic(coordenadas.iloc[12,1], coordenadas.iloc[7,1]).km)
distancia8 = str(geodesic(coordenadas.iloc[0,1], coordenadas.iloc[8,1]).km)
distancia9 = str(geodesic(coordenadas.iloc[8,1], coordenadas.iloc[9,1]).km)
distancia10 = str(geodesic(coordenadas.iloc[9,1], coordenadas.iloc[10,1]).km)
distancia11 = str(geodesic(coordenadas.iloc[10,1], coordenadas.iloc[11,1]).km)
distancia12 = str(geodesic(coordenadas.iloc[11,1], coordenadas.iloc[13,1]).km)
distancia13 = str(geodesic(coordenadas.iloc[13,1], coordenadas.iloc[7,1]).km)
#Distancias de la ruta hacia la Sede de Tocumen
#Distancias de la ruta hacia Altaplaza
#Distancias de la ruta hacia
#Distancias de la ruta hacia
#Distancias de la ruta hacia
#Distancias de la ruta hacia
#Distancias de la ruta hacia
#Distancias de la ruta hacia

conx= conx.assign(km = [distancia0, distancia1, distancia2, distancia3,distancia4,distancia5, distancia6,distancia7,distancia8,distancia9,distancia10,distancia11,distancia12,distancia13])
print(conx)


# In[158]:


#crear grafo con segun los datos
Rutas = nt.from_pandas_edgelist(conx, source="partida", target = "llegada", edge_attr = "km")
Rutas.nodes()


# #### mostrar opciones

# In[160]:


#recorrido
opcion=int(input("\t 1: Estacion San Miguelito\n\t 2: El Dorado Mall \n\t 3: UTP- Sede de Tocumen \n\t 4: Dorado Mall \n Digite el destino: "))
match opcion:
    case 1:
        print("----Elegiste como llegada la Estación San Miguelito----\n  La ruta mas corta es: ")
        recorrido = nt.dijkstra_path(Rutas, source="UTP", target="ESTACION San Miguelito", weight = True) #esto es lo que debe salir en el mapa
        print(recorrido)
    case 2: 
        print("----Elegiste como llegada El Dorado Mall ----\n  La ruta mas corta es: ")
        recorrido = nt.dijkstra_path(Rutas, source="UTP", target="EL Dorado Mall", weight = True) #esto es lo que debe salir en el mapa
        print(recorrido)
    case 3: print("----Elegiste como llegada UTP Sede de Tocumen----\n  La ruta mas corta es: ")
    case 4: print("----Elegiste como llegada Altaplaza Mall ----\n  La ruta mas corta es: ")
    case 5: print("----Elegiste como llegada  ----\n  La ruta mas corta es: ")
    case 6: print("----Elegiste como llegada  ----\n  La ruta mas corta es: ")
    case 7: print("----Elegiste como llegada  ----\n  La ruta mas corta es: ")
    case 8: print("----Elegiste como llegada  ----\n  La ruta mas corta es: ")
    case 9: print("----Elegiste como llegada----\n  La ruta mas corta es: ")   
    case _: print("Lastimosamente no contamos con esta opcion")


# In[ ]:




