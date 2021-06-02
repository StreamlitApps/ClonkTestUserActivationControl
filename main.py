
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
from st_aggrid import AgGrid,  DataReturnMode, GridUpdateMode, GridOptionsBuilder

data=pd.DataFrame([[ "Usuario","Fecha último pago", "Tiempo de Prueba"],
                   ["Esteban",dt.date.fromisoformat('2021-03-24'), 120],
                   ["Gabriel", dt.date.fromisoformat('2021-03-04'), 30],
                   ["Jose", dt.date.fromisoformat('2021-06-01'), 15],
                   ["Angela", dt.date.fromisoformat('2021-06-01'), 0],
                   ])
data.columns=data.iloc[0]
data=data[1:]

st.markdown("# Prueba de lógica de registro de usuarios")
data=AgGrid(data, editable=True,
    sortable=True,
    filter=True,
    resizable=True,
    height=180,

    fit_columns_on_grid_load=True,
    key='input_frame')

df=data['data']
df=df.reset_index()
df['Fecha último pago']=pd.to_datetime(df['Fecha último pago'])

st.markdown("# Estado de las personas")
fechas=[df['Fecha último pago'][i]+dt.timedelta(days=int(df['Tiempo de Prueba'][i])) for i in range(len(df))]

c1, c2, c3 = st.beta_columns(3)
c1.markdown("## Usuario")
c2.write("## Vigente hasta")
c3.write ("## Estado")
desactivados=[]
for i in range(len(df)):
    c1.write(df["Usuario"][i])
    c2.write(fechas[i])
    if dt.datetime.now()<fechas[i]:
        c3.write("Activo")
    else:
        c3.write("Desactivado")
        desactivados.append(df["Usuario"][i])
st.markdown("## Usuarios pendientes para pago")
st.write(desactivados)
