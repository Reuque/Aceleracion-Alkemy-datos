# -*- coding: utf-8 -*-
"""procesamientoDatos

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AZvQul1m0AhPG94Qs29-gswrwoH02n1Q
"""

import requests
import os

museos = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv", allow_redirects = True)
os.makedirs('museos/2022-mayo')
open('museos/2022-mayo/museos-18-05-2022.csv', 'wb').write(museos.content)

cines = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv", allow_redirects= True)
os.makedirs('cines/2022-mayo')
open('cines/2022-mayo/cines-18-05-2022.csv', 'wb').write(cines.content)

bibliotecas = requests.get("https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv", allow_redirects = True)
os.makedirs('bibliotecas/2022-mayo')
open('bibliotecas/2022-mayo/bibliotecas-18-05-2022.csv', 'wb').write(bibliotecas.content)

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# Preprocesamiento

data_cines = pd.read_csv("cines/2022-mayo/cines-18-05-2022.csv")
data_bibliotecas = pd.read_csv("bibliotecas/2022-mayo/bibliotecas-18-05-2022.csv")
data_museos = pd.read_csv("museos/2022-mayo/museos-18-05-2022.csv")
# Crear tabla
columns = ["cod_localidad", "id_provincia", "id_departamento", "categoría", "provincia", "localidad", "nombre", "domicilio", "código postal", "número de teléfono", "mail", "web"]
data_tabla = pd.DataFrame(columns=columns)

#Alistamos las columnas a eliminar
cols_to_drop_cine = ['Observaciones','Departamento', 'Dirección', 'Piso', 'cod_area', 'Información adicional', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 'tipo_gestion', 'Pantallas', 'Butacas', 'espacio_INCAA',
       'año_actualizacion']
cols_to_drop_bibliotecas = ['Observacion', 'Subcategoria', 'Departamento', 'Piso', 'Cod_tel', 'Información adicional', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Fuente', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion']
cols_to_drop_museos = ['Observaciones', 'subcategoria', 'piso', 'cod_area', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional','fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion']

#Eliminamos las columnas
data_cines2 = data_cines.drop(cols_to_drop_cine, axis=1)
data_bibliotecas2 = data_bibliotecas.drop(cols_to_drop_bibliotecas, axis=1)
data_museos2 = data_museos.drop(cols_to_drop_museos, axis=1)

#Renombramos las columnas a su correspondiente formato
data_museos2 = data_museos2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'categoria':'categoría', 'direccion':'domicilio', 'CP':'código postal', 'telefono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
data_cines2 = data_cines2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia','Dirección':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})
data_bibliotecas2 = data_bibliotecas2.rename(columns={'Cod_Loc':'cod_localidad', 'IdProvincia':'id_provincia', 'IdDepartamento':'id_departamento', 'Categoría':'categoría', 'Provincia':'provincia', 'Localidad':'localidad', 'Nombre':'nombre', 'Domicilio':'domicilio', 'CP':'código postal', 'Teléfono':'número de teléfono',  'Mail':'mail', 'Web':'web'})

data_tabla = pd.concat([data_museos2, data_cines2, data_bibliotecas2])

# Creacion de la segunda tabla cantidad de registros

data_museos3 = data_museos.rename(columns={'fuente':'Fuente', 'categoria':'Categoría', 'provincia':'Provincia', 'nombre':'Nombre'})
data_raw = pd.concat([data_museos3, data_cines, data_bibliotecas])
data_raw2 = df_bruta.drop(['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Observaciones', 'subcategoria', 'localidad', 'direccion', 'piso', 'CP', 'cod_area', 'telefono', 'Mail', 'Web', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'jurisdiccion', 'año_inauguracion', 'actualizacion', 'Departamento', 'Localidad', 'Dirección', 'Piso', 'Teléfono', 'Información adicional', 'tipo_gestion', 'Pantallas', 'Butacas', 'espacio_INCAA', 'año_actualizacion', 'Observacion', 'Subcategoria', 'Domicilio', 'Cod_tel', 'Tipo_gestion', 'año_inicio', 'Año_actualizacion'], axis=1)

data_tabla2 = pd.pivot_table(data_raw2, values='Nombre', index=['Fuente', 'Categoría'], columns=['Provincia'], aggfunc='count', margins=True)

# Creacion de la tercer tabla cantidad de registros

data_raw3 = data_cines[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
data_raw3['espacio_INCAA']= data_raw3['espacio_INCAA'].fillna(0)
data_raw3['espacio_INCAA'].replace({"SI": "si", "si": "1"}, inplace=True)

data_tabla3 = data_raw3.groupby('Provincia').sum()







