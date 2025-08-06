import os
import xml.etree.ElementTree as ET
from src.utils.modify_sql_utils import crear_modifySql_element, contiene_modifySql
from src.writer.xml_writer import guardar_xml

def modificar_changelog(config, diccionario, output_file):
    changelog_path = config["changelog_path"]
    target_db = config["database_config"]["destination_database"]

    if not os.path.exists(changelog_path):
        raise FileNotFoundError(f"No se encontró el changelog: {changelog_path}")
    
    if target_db not in diccionario:
        raise ValueError(f"No hay reglas para la base de datos destino: {target_db}")
    
    tree = ET.parse(changelog_path)
    root = tree.getroot()
    ns = {"db": "http://www.liquibase.org/xml/ns/dbchangelog"}
    ET.register_namespace("", ns["db"])

    reglas = diccionario[target_db]

    for changeset in root.findall("db:changeSet", ns):
        tiene_estructura = (
            changeset.find("db:createTable", ns) is not None or
            changeset.find("db:addColumn", ns) is not None
        )

        if tiene_estructura and not contiene_modifySql(changeset, target_db):
            modifySql = crear_modifySql_element(reglas, target_db)
            changeset.append(modifySql)

    guardar_xml(tree, output_file)
