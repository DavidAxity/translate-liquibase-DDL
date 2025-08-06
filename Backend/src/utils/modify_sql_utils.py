import xml.etree.ElementTree as ET

def crear_modifySql_element(reemplazos, target_db):
    modifySql = ET.Element("modifySql", dbms=target_db)
    for r in reemplazos:
        ET.SubElement(modifySql, "replace", {
            "replace": r["replace"],
            "with": r["with"]
        })
    return modifySql

def contiene_modifySql(changeset, target_db):
    for child in changeset.findall("modifySql"):
        if child.attrib.get("dbms") == target_db:
            return True
    return False
