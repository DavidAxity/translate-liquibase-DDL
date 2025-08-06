import yaml

def cargar_config(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def cargar_diccionario(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
