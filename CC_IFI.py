# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Registro,Historial,Capacitacion,Bonos,Salir

def CC_IFI(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_12= st.sidebar.empty()
  titulo= placeholder1_12.title("Menú")

  placeholder2_12 = st.sidebar.empty()
  registro_12 = placeholder2_12.button("Registro",key="registro_12")

  placeholder3_12 = st.sidebar.empty()
  historial_12 = placeholder3_12.button("Historial",key="historial_12")

  placeholder4_12 = st.sidebar.empty()
  capacitacion_12 = placeholder4_12.button("Capacitaciones",key="capacitacion_12")

  placeholder5_12 = st.sidebar.empty()
  bonos_12 = placeholder5_12.button("Bonos",key="bonos_12")

  placeholder6_12 = st.sidebar.empty()
  salir_12 = placeholder6_12.button("Salir",key="salir_12")

  placeholder7_12 = st.empty()
  conformacion_12 = placeholder7_12.title("Control de Calidad de Información Final I")

  placeholder8_12= st.empty()
  fecha_12= placeholder8_12.date_input("Fecha",key="fecha_12")

  placeholder9_12= st.empty()
  bloque_12= placeholder9_12.number_input("Bloque",max_value=1000000000,step=1,key="bloque_11")
    
  placeholder10_12= st.empty()
  estado_12= placeholder10_12.selectbox("Estado", options=("En Proceso","Aprobado","Rechazado","Reinspección Aprobado","Reinspección Rechazado"), key="estado_12")
              
  placeholder11_12= st.empty()
  predios_12= placeholder11_12.number_input("Cantidad de Predios Revisados",min_value=0,step=1,key="predios_12")

  placeholder12_12= st.empty()
  horas_12= placeholder12_12.number_input("Cantidad de Horas Trabajadas en el Proceso",min_value=0.0,key="horas_12")

  placeholder13_12 = st.empty()
  reporte_12 = placeholder13_12.button("Generar Reporte",key="reporte_12")

  # ----- Registro ---- #
    
  if registro_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    st.session_state.Registro=False
    st.session_state.CC_IFI=False

    código_de_acceso=pd.read_sql(f"select código_de_acceso from usuarios where usuario ='{usuario}'",uri)
    código_de_acceso= código_de_acceso.loc[0,'código_de_acceso']

    if código_de_acceso=="1":        
                    
      Registro.Registro1(usuario,puesto)
                
    elif código_de_acceso=="2":        
                    
      Registro.Registro2(usuario,puesto)   

    elif código_de_acceso=="3":        
                    
      Registro.Registro3(usuario,puesto) 

  #----- Historial ---- #
    
  elif historial_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    st.session_state.CC_IFI=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    st.session_state.CC_IFI=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Capacitación ---- #
    
  elif bonos_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    st.session_state.CC_IFI=False
    st.session_state.Bonos=True
    Bonos.Bonos(usuario,puesto)    


    # ----- Salir ---- #
    
  elif salir_12:
    placeholder1_12.empty()
    placeholder2_12.empty()
    placeholder3_12.empty()
    placeholder4_12.empty()
    placeholder5_12.empty()
    placeholder6_12.empty()
    placeholder7_12.empty()
    placeholder8_12.empty()
    placeholder9_12.empty()
    placeholder10_12.empty()
    placeholder11_12.empty()
    placeholder12_12.empty()
    placeholder13_12.empty()
    st.session_state.Ingreso = False
    st.session_state.CC_IFI=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_12:

    cursor01=con.cursor()

    marca_12=datetime.now(pytz.timezone('America/Chicago')).strftime("%Y-%m-%d %H:%M:%S")
    nombre_12= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)

    nombre_12 = nombre_12.loc[0,'nombre']
      
    horario_12= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    horario_12 = horario_12.loc[0,'horario']

    supervisor_12= pd.read_sql(f"select horario from usuarios where usuario ='{usuario}'",uri)
    supervisor_12 = horario_12.loc[0,'horario']

    cursor01.execute(f"INSERT INTO registro (marca,proceso,usuario,nombre,horario,fecha,bloque,estado,predios,horas,puesto,tipo,supervisor)VALUES('{marca_12}','Control de Calidad IF I','{usuario}','{nombre_12}','{horario_12}','{fecha_12}','{bloque_12}','{estado_12}','{predios_12}','{horas_12}','{puesto}','No Aplica','{supervisor_12}')")
    con.commit()
    st.success('Registro enviado correctamente')