import os
from src.config.loader import cargar_config, cargar_diccionario
from src.parser.changelog_modifier import modificar_changelog

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    config_path = os.path.join(BASE_DIR, "resources", "config.yaml")
    config = cargar_config(config_path)
    diccionario = cargar_diccionario(config["dictionary_path"])

    # Ruta absoluta del archivo de salida
    output_file = os.path.join(BASE_DIR, config["output_path"])

    # Crear carpeta de salida si no existe
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    modificar_changelog(config, diccionario, output_file)
