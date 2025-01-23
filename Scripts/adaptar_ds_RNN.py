import pandas as pd

# Cargar el dataset con delimitador ;
file_path = "Data_Set_Unido.csv"
df = pd.read_csv(file_path,encoding="ISO-8859-1", delimiter=';')

# Limpiar caracteres no deseados en las fechas y demás columnas de texto
df['Maneuver Date\nand Time (T0)'] = df['Maneuver Date\nand Time (T0)'].str.replace(r'[^\x00-\x7F]+', '', regex=True)
df['Epoch Before Maneuver'] = df['Epoch Before Maneuver'].str.replace(r'[^\x00-\x7F]+', '', regex=True)
df['Epoch After Maneuver'] = df['Epoch After Maneuver'].str.replace(r'[^\x00-\x7F]+', '', regex=True)

# Modificar la columna 'MANEUVER' para que sea un identificador numérico incremental
df['MANEUVER'] = pd.factorize(df['MANEUVER'])[0] + 1  # +1 para empezar en 1

# Mapear 'Maneuver Type' a valores numéricos específicos
df['Maneuver Type'] = df['Maneuver Type'].map({
    'WEST_NM001': 1,
    'South_SKM000': 2,
    'South_SKM001': 3
})

# Convertir 'Maneuver Date\nand Time (T0)' a timestamp en segundos
df['Maneuver_Timestamp'] = pd.to_datetime(df['Maneuver Date\nand Time (T0)'], format='%d/%m/%Y %H:%M:%S', dayfirst=True, errors='coerce').apply(lambda x: x.timestamp() if pd.notnull(x) else None)
df.drop(columns=['Maneuver Date\nand Time (T0)'], inplace=True)  # Opcional: eliminar columna original

# Convertir 'Epoch Before Maneuver' y 'Epoch After Maneuver' a timestamp en segundos
df['Epoch_Before_Timestamp'] = pd.to_datetime(df['Epoch Before Maneuver'], format='%d/%m/%Y %H:%M:%S', dayfirst=True, errors='coerce').apply(lambda x: x.timestamp() if pd.notnull(x) else None)
df['Epoch_After_Timestamp'] = pd.to_datetime(df['Epoch After Maneuver'], format='%d/%m/%Y %H:%M:%S', dayfirst=True, errors='coerce').apply(lambda x: x.timestamp() if pd.notnull(x) else None)
df.drop(columns=['Epoch Before Maneuver', 'Epoch After Maneuver'], inplace=True)  # Opcional: eliminar columnas originales

# Rellenar valores NaN en columnas específicas
columns_with_nan = [
    'Inclination Control Error', 'Cross-Coupling Coefficient DeltaVr',
    'Cross-Coupling Coefficient Delta_Vt', 'Delta_Vr Ranging', 'Delta_Vn Ranging'
]
df[columns_with_nan] = df[columns_with_nan].fillna(0)

# Convertir columnas restantes de tipo 'object' a 'float' si es posible
columns_to_convert = [
    'Total Propellant Kg', 'Inclination Control Error', 'Cross-Coupling Coefficient DeltaVr',
    'Cross-Coupling Coefficient Delta_Vt', 'Delta_Vr Ranging', 'Delta_Vn Ranging',
    'Maneuver_Timestamp', 'Epoch_Before_Timestamp', 'Epoch_After_Timestamp'
]

for column in columns_to_convert:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Guardar el dataset modificado
output_path = "Data_Set_Unido_Modificado.csv"
df.to_csv(output_path, index=False)

print("Modificaciones completadas y guardadas en", output_path)


print(df.dtypes)
print("Exito")