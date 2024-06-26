import os
import pandas as pd
import csv

ENCB=["Numero de registro",
       "Medicamento",
       "Fecha de caducidad",
       "Dosis recomendada",
       "Via de administracion",
       "Tipo de conservacion",
       "Leyendas de advertencia",
       "Formula",
       "Datos del fabricante"]

def escritor_datos(data):
    with open("medicamentos.csv", mode="w", newline="") as mdcn:
        esctr=csv.DictWriter(mdcn, fieldnames=ENCB)
        esctr.writeheader()
        esctr.writerow(data)
        

def añadir_datos(data):
    with open("medicamentos.csv", mode="a", newline="") as mdcn: 
            esctr=csv.DictWriter(mdcn, fieldnames=ENCB)
            esctr.writerow(data) 
        
        
def añadir_data():
    try:
        med_id=input("Numero de registro del medicamento: ")
        med_nm=str.upper(input("Nombre del medicamento: ")) #
        med_d=int(input("Dia de caducidad: "))
        med_m=int(input("Mes de caducidad 1-12: "))
        med_a=int(input("Año de caducidad: "))
        med_dosis=input("Dosis recomendada: ")
        med_via=input("Via de administracion: ")
        med_csvtn=str.upper(input("Tipo de conservacion: ")) #
        med_wrngs=input("Advertencias de medicacion: ")
        med_frmla=input("Requiere receta?(Y/N): ")
        med_fbctr=input("Datos del fabricante: ")
        med_expdate=[med_d,med_m,med_a]
        data={"Numero de registro":med_id,
        "Medicamento":med_nm, 
        "Fecha de caducidad":med_expdate,
        "Dosis recomendada":med_dosis,
        "Via de administracion":med_via,
        "Tipo de conservacion":med_csvtn,
        "Leyendas de advertencia":med_wrngs,  
        "Formula":med_frmla,                            
        "Datos del fabricante":med_fbctr}
        if os.path.exists("medicamentos.csv"):   # Este verifica si exite usa el modo append
            añadir_datos(data)
            print(f"Se añadio correctamente {med_nm}")
        else:                                    # Si no existe crea el archivo con el modo write
            escritor_datos(data)
            print(f"Se añadio correctamente {med_nm}")
    except Exception as error:
        print(f"Error en {error}")
    
def consultar_todos_los_datos():
    archivo=pd.read_csv("medicamentos.csv", index_col=0)
    print(archivo)


def consultar_un_solo_dato():
    archivo=pd.read_csv("medicamentos.csv", index_col=0)
    med_ID=input("ID del medicamento: ")
    b = archivo[(archivo["Numero de registro"] == med_ID)]
    print(b)


def consultar_varios_por_caract():
    archivo=pd.read_csv("medicamentos.csv", index_col=0)
    med_csvtn=input("ID del medicamento: ")
    b = archivo[(archivo["Tipo de conservacion"] == med_csvtn)]
    print(b)
    
    
def consultar_todos_algunas_columnas():
    archivo=pd.read_csv("medicamentos.csv", index_col=0)
    a="Numero de registro"
    b="Medicamento"
    c="Fecha de caducidad"
    d="Dosis recomendada"
    e="Via de administracion"
    f="Tipo de conservacion"
    g="Leyendas de advertencia"
    h="Formula"
    i="Datos del fabricante"
    seleccion=int(input("Que datos desea mostrar?: "))
    datos=[]
    while seleccion != 0:
        if seleccion == 1:
            datos.append(a)
        if seleccion == 2:
            datos.append(b)
        if seleccion == 3:
            datos.append(c)
        if seleccion == 4:
            datos.append(d)
        if seleccion == 5:
            datos.append(e)
        if seleccion == 6:
            datos.append(f)
        if seleccion == 7:
            datos.append(g)
        if seleccion == 8:
            datos.append(h)
        if seleccion == 9:
            datos.append(i)
        print(f"Actualmente se mostraran {datos}")        
        seleccion=int(input("Que datos desea mostrar?: "))
    print(archivo[datos])


"""def mdcn_uptr():
    with open('medicamentos.csv', mode='r', newline='') as file:
        reader = csv.DictReader(file)
        medic=list(reader)
        for b in medic:
            print(b)      # ESTO MUESTRA TODOS LOS MEDICAMENTOS
            
    f=input("Numero del medicamento que quiera actualizar: ") # SE DICE EL NUMERO DE REGISTRO DEL MED QUE SE QUIERE ACTUALIZAR
    
    confm=False                # Variable que servira para activar la funcion de escribir los nuevos datos o no 
    for med in medic:
        if med["Numero de registro"] == f: # Se busca el dato dentro de los meds registrados y si se encuentra se activa las sgtes lineas
            print("Se encontro el medicamento, actualizalo: ")
            n=input("Ingrese Numeracion del medicamento: ") #X
            m=input("Ingrese Nombre del medicamento:") #X                    En las "X" se ingresan los nuevos datos    
            t=input("Ingrese Temperatura: ")  #X                     
            med["Numero de registro"] = n #Y
            med["Medicamento"] = m  #Y                             En las "Y" los se reemplazan los datos
            med["Temperatura recomendada"] = t #Y 
            confm=True     # La variable confm toma un valor verdadero                    
            
    if confm: # Cuando cofnm toma un valor verdadero se ejecuta la funcion para escribir los nuevos datos
        with open('medicamentos.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=enc)
            writer.writeheader()
            writer.writerows(medic)
            print("listo")
    else:  # Esto sale cuando no se encontro el codigo
        print("No se encontro esta vaina")"""
        

def eliminar_datos_csv(archivo_csv, criterios):
    try:
        with open(archivo_csv, 'r', newline='') as archivo:
            reader = csv.DictReader(archivo)
            datos = list(reader)

        datos_filtrados = [fila for fila in datos if not all(fila.get(campo) == valor for campo, valor in criterios.items())]

        with open(archivo_csv, 'w', newline='') as archivo:
            campos = datos[0].keys() if datos else []
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(datos_filtrados)

        print("Medicamento eliminado con éxito.")

    except FileNotFoundError:
        print("El archivo de origen no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Ejemplo de uso:
# Especifica el nombre del archivo CSV y los criterios de eliminación (criterios es la id del medicamento)
archivo_csv = 'Medicamentos.csv'
criterios = [med_id]
eliminar_datos_csv(archivo_csv, criterios)
