import xml.etree.ElementTree as ET

root = ET.Element('shop')
category = ET.SubElement(
    root, 
    'category', 
    {'name': 'Vegan Products'}
)

products = {
    'Good Morning Sunshine': {
        'type': 'cereals',
        'producer': 'OpenEDG Testing Service',
        'price': 9.90,
        'currency': 'USD'
    },
    'Spaghetti Veganietto': {
        'type': 'pasta',
        'producer': 'Programmers Eat Pasta',
        'price': 15.49,
        'currency': 'EUR'
    },
    'Fantastic Almond Milk': {
        'type': 'beverages',
        'producer': 'Drinks4Coders Inc.',
        'price': 19.75,
        'currency': 'USD'
    },
}

for product, prod_info in products.items():
    xml_product = ET.SubElement(
        category, 
        'product', 
        {'name': product}
    )
    for info_name, info in prod_info.items():
        xml_info = ET.SubElement(
            xml_product, 
            info_name
        )
        xml_info.text = str(info)

ET.dump(root)

tree = ET.ElementTree(root)
ET.indent(tree)
tree.write('vegans.xml', 'UTF-8', True)