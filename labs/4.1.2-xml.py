import xml.etree.ElementTree as ElementTree

try:
    tree = ElementTree.parse('./labs/nyse.xml')
except FileNotFoundError:
    print('No se encontró el archivo')
except ElementTree.ParseError:
    print('Hubo problemas leyendo el xml')

elements = tree.getroot()
print(elements.tag)

for element in elements.findall('quote'):
    print(element.text.ljust(40), end='')
    for key, attr in element.attrib.items():
        print(attr.ljust(10), end='')

    print()
    # for attr in element.attrib:
    #     print(attr, '\t')
    #     print()