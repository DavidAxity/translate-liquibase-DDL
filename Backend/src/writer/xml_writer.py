def guardar_xml(tree, output_path):
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    print(f"✔️ Archivo modificado guardado en: {output_path}")
