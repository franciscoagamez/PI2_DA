
import pandas as pd
import numpy as np
import datetime
import mysql.connector
import pymysql
from sqlalchemy import create_engine

#Funcion cargar excel

def cargar_excel(archivo, hojas, engine='openpyxl'):
    """
    Carga datos desde un archivo Excel y los devuelve en un diccionario de DataFrames.

    Parámetros:
    - archivo (str): Ruta del archivo Excel.
    - hojas (list): Lista de nombres de las hojas a cargar.
    - engine (str, opcional): Motor de Excel a usar. Valor por defecto 'openpyxl'.

    Retorna:
    dict: Un diccionario donde las claves son los nombres de las hojas y los valores son los DataFrames correspondientes.

    Ejemplo:
    datos = cargar_excel('archivo.xlsx', ['Hoja1', 'Hoja2'])
    df_hoja1 = datos['Hoja1']
    df_hoja2 = datos['Hoja2']
    """
    archivo_excel = pd.ExcelFile(archivo, engine=engine)
    datos_hojas = {}

    for nombre_hoja in hojas:
        dataframe_hoja = pd.read_excel(archivo_excel, nombre_hoja)
        datos_hojas[nombre_hoja] = dataframe_hoja

    return datos_hojas



#Funcion detectar sd

def detectar_sd(df):
    """
    Examina la presencia de valores 'SD' en cada columna del DataFrame.

    Parámetros:
    df (pd.DataFrame): El DataFrame a examinar.

    Retorna:
    pd.DataFrame: Un DataFrame que muestra la cantidad y el porcentaje de valores 'SD' en cada columna.
    """
    columnas = df.columns
    lista_resultados = []

    for col in columnas:
        num_sd = (df[col] == 'SD').sum()
        porcentaje_sd = (num_sd / df.shape[0]) * 100
        lista_resultados.append({'Columna': col, 'Cantidad de SD': num_sd, 'Porcentaje de SD': porcentaje_sd})

    df_resultados = pd.DataFrame(lista_resultados)
    df_sd_presentes = df_resultados[df_resultados['Cantidad de SD'] > 0]

    return df_sd_presentes


#Función limpiar_Data

def limpiar_data(df, drop_duplicates=False, drop_na=False, fill_na=None, convert_to_datetime=None, uppercase_columns=None,
                  lowercase_columns=None, titlecase_columns=None, strip_spaces=True, rename_columns=None, drop_columns=None,
                  categorize_columns=None, replace_values=None, new_columns=None, convert_date_columns=None, 
                  convert_to_int_columns=None, convert_to_float=None, new_columns2=None):
    """
    Realiza el proceso de limpieza de datos en un DataFrame.

    Parámetros:
    - df (pd.DataFrame): El DataFrame a limpiar.
    - drop_duplicates (bool): Eliminar duplicados si es True.
    - drop_na (bool): Eliminar filas con valores nulos si es True.
    - fill_na (dict): Diccionario con valores para llenar nulos por columna.
    - convert_to_datetime (list): Lista de columnas a convertir a datetime.
    - uppercase_columns (list): Lista de columnas a convertir a mayúsculas.
    - lowercase_columns (list): Lista de columnas a convertir a minúsculas.
    - titlecase_columns (list): Lista de columnas a convertir a título.
    - strip_spaces (bool): Eliminar espacios en blanco si es True.
    - rename_columns (dict): Diccionario para renombrar columnas.
    - drop_columns (list): Lista de columnas a eliminar.
    - categorize_columns (list): Lista de columnas a convertir a categoría.
    - replace_values (dict): Diccionario de valores para reemplazar en columnas.
    - new_columns (dict): Diccionario con nuevas columnas y valores.
    - convert_date_columns (dict): Diccionario con columnas de fecha y sus formatos.
    - convert_to_int_columns (list): Lista de columnas a convertir a entero.
    - convert_to_float (list): Lista de columnas a convertir a float.
    - new_columns2 (dict): Diccionario con nuevas columnas y expresiones basadas en otras columnas.

    Retorna:
    pd.DataFrame: El DataFrame limpio.
    """
    cleaned_df = df.copy()

    # Eliminar duplicados
    if drop_duplicates:
        cleaned_df = cleaned_df.drop_duplicates()

    # Eliminar filas con valores nulos
    if drop_na:
        cleaned_df = cleaned_df.dropna()

    # Rellenar valores nulos
    if fill_na:
        cleaned_df = cleaned_df.fillna(fill_na)

    # Convertir columnas a tipo datetime
    if convert_to_datetime:
        for col in convert_to_datetime:
            cleaned_df[col] = pd.to_datetime(cleaned_df[col], errors='coerce')

    # Convertir columnas a mayúsculas
    if uppercase_columns:
        for col in uppercase_columns:
            cleaned_df[col] = cleaned_df[col].str.upper()

    # Convertir columnas a minúsculas
    if lowercase_columns:
        for col in lowercase_columns:
            cleaned_df[col] = cleaned_df[col].str.lower()

    # Convertir columnas a formato título
    if titlecase_columns:
        for col in titlecase_columns:
            cleaned_df[col] = cleaned_df[col].str.title()

    # Eliminar espacios en blanco alrededor de los valores
    if strip_spaces:
        cleaned_df = cleaned_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Renombrar columnas
    if rename_columns:
        cleaned_df = cleaned_df.rename(columns=rename_columns)

    # Eliminar columnas
    if drop_columns:
        cleaned_df = cleaned_df.drop(columns=drop_columns)

    # Convertir columnas a categorías
    if categorize_columns:
        for col in categorize_columns:
            cleaned_df[col] = cleaned_df[col].astype('category')

    # Reemplazar valores en columnas
    if replace_values:
        for col, replacements in replace_values.items():
            cleaned_df[col] = cleaned_df[col].replace(replacements)

    # Agregar nuevas columnas con valores específicos
    if new_columns:
        for col, value in new_columns.items():
            cleaned_df[col] = value

    # Agregar nuevas columnas basadas en otras columnas
    if new_columns2:
        for col, expr in new_columns2.items():
            cleaned_df[col] = cleaned_df.eval(expr)

    # Convertir columnas de fecha con formatos específicos
    if convert_date_columns:
        for col, fmt in convert_date_columns.items():
            cleaned_df[col] = pd.to_datetime(cleaned_df[col], format=fmt, errors='coerce')

    # Convertir columnas a tipo entero
    if convert_to_int_columns:
        for col in convert_to_int_columns:
            cleaned_df[col] = pd.to_numeric(cleaned_df[col], errors='coerce').astype('Int64')

    # Convertir columnas a tipo float
    if convert_to_float:
        for col in convert_to_float:
            cleaned_df[col] = cleaned_df[col].astype(float)

    return cleaned_df

#Función para crear la base de datos


def create_mysql_db(csv_file_path, db_name, table_name, host='localhost', user='tu_usuario', password='tu_contraseña'):
    """
    Crea una base de datos MySQL y una tabla a partir de un archivo CSV.

    Parameters:
    - csv_file_path (str): Ruta del archivo CSV.
    - db_name (str): Nombre de la base de datos a crear.
    - table_name (str): Nombre de la tabla a crear.
    - host (str, optional): Dirección del servidor MySQL. Por defecto, 'localhost'.
    - user (str, optional): Usuario de MySQL. Por defecto, 'tu_usuario'.
    - password (str, optional): Contraseña de MySQL. Por defecto, 'tu_contraseña'.

    Returns:
    None
    """
    try:
        # Validaciones
        if not csv_file_path.endswith('.csv'):
            raise ValueError("El archivo debe tener extensión CSV.")

        # Cargar CSV en un DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Conectar a MySQL y crear la base de datos si no existe
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.close()
        connection.close()

        # Conectar a MySQL y crear la tabla si no existe usando pymysql como conector
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:3306/{db_name}')
        connection = engine.connect()
        df.to_sql(table_name, connection, index=False, if_exists='replace')
        connection.close()

        print("Base de datos y tabla creadas exitosamente.")
    except pd.errors.EmptyDataError:
        raise ValueError("El archivo CSV está vacío.")
    except pymysql.MySQLError as err:
        print(f"Error al conectar a MySQL: {err}")
        raise
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise

# Asegúrate de tener pymysql instalado. Puedes instalarlo con: pip install pymysql
