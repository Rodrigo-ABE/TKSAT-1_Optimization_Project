import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Cargar el dataset
file_path = "DATA_SET_SUR_V2.csv"
df = pd.read_csv(file_path,encoding="ISO-8859-1", delimiter=';')

# Convertir las columnas de fecha a timestamps (en segundos) y manejar el tipo de dato
date_columns = ['Maneuver Date', 'Epoch BM']
for col in date_columns:
    df[col] = pd.to_datetime(df[col], format='%d/%m/%Y %H:%M', dayfirst=True, errors='coerce').astype(int) // 10**9

# Guardar el dataset modificado
df.to_csv("DATA_SET_SUR_V2_Modificado.csv", index=False)

print("Well Done")