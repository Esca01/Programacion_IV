# main.py
import pandas as pd
import numpy as np
import UI_Module as ui_module
import API_Module as api_module

# Mapeo entre los nombres de columna en el JSON y los nombres en el DataFrame
column_mapping = {
    "ph_agua_suelo_2_5_1_0": "ph",
    "f_sforo_p_bray_ii_mg_kg": "fosforo_p",
    "potasio_k_intercambiable_cmol_kg": "potasio_k"
}

def main():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)

    user_input = ui_module.get_user_input()
    departamento, municipio, cultivo, limit = user_input

    data = api_module.fetch_data()
    results_df = pd.DataFrame.from_records(data)

    filtered_df = results_df[
        (results_df['departamento'] == departamento) &
        (results_df['municipio'] == municipio) &
        (results_df['cultivo'] == cultivo)
    ].head(limit)

    if len(filtered_df) == 0:
        print("No se encontraron registros para los parámetros ingresados.")
    else:
        # Convierte los valores especiales a NaN para cálculos
        filtered_df.replace(['ND', '<1,00'], np.nan, inplace=True)

        # Renombra las columnas usando el mapeo
        filtered_df.rename(columns=column_mapping, inplace=True)

        # Calcula las medianas
        median_ph = pd.to_numeric(filtered_df['ph'], errors='coerce').median()
        median_phosphorus = pd.to_numeric(filtered_df['fosforo_p'], errors='coerce').median()
        median_potassium = pd.to_numeric(filtered_df['potasio_k'], errors='coerce').median()

        print("\nTabla de registros:")
        print(filtered_df[['departamento', 'municipio', 'cultivo', 'ph', 'fosforo_p', 'potasio_k']])

        print("\nMediana de variables edáficas:")
        print(f"Mediana pH: {median_ph:.2f}")
        print(f"Mediana Fósforo(P): {median_phosphorus:.2f}")
        print(f"Mediana Potasio(K): {median_potassium:.2f}")

if __name__ == "__main__":
    main()
