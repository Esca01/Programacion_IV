# ui_module.py
def get_user_input():
    departamento = input("Ingrese el Departamento: ")
    municipio = input("Ingrese el Municipio: ")
    cultivo = input("Ingrese el Cultivo: ")
    limit = int(input("Ingrese el número de Registros a consultar: "))
    return departamento, municipio, cultivo, limit
