import xml.etree.ElementTree

cars_for_sale = (
    xml.etree.ElementTree
    .parse('./Python-advanced-4-REST-APIS/1.5.1-xml.xml')
    .getroot()
)
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
        print(' =', prop.text)

for car in cars_for_sale.findall('car'):
    print(car.text)
    for prop in car:
        print(prop.text)