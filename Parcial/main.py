# main.py
import pandas as pd
import UI_Module as ui_module
import API_Module as api_module

def main():
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
        print("\nTabla de registros:")
        print(filtered_df)

        median_ph = filtered_df['ph'].median()
        median_phosphorus = filtered_df['fosforo_p'].median()
        median_potassium = filtered_df['potasio_k'].median()

        print("\nMediana de variables edáficas:")
        print(f"Mediana pH: {median_ph:.2f}")
        print(f"Mediana Fósforo(P): {median_phosphorus:.2f}")
        print(f"Mediana Potasio(K): {median_potassium:.2f}")

if __name__ == "__main__":
    main()
