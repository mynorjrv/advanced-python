import xml.etree.ElementTree as ET

tree = ET.parse('./Python-advanced-5-File-Processing/books.xml')
root = tree.getroot()
# root = ET.fromstring(your_xml_as_string)

print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)
