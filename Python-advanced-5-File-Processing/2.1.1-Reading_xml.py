import xml.etree.ElementTree as ET

tree = ET.parse('./Python-advanced-5-File-Processing/books.xml')
root = tree.getroot()
# root = ET.fromstring(your_xml_as_string)

print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)


# Accessing tree elements by index
print("My books:\n")
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author:', book[0].text)
    print('Year: ', book[1].text, '\n')


# Using iter method, all elements with tag
for author in root.iter('author'):
    print(author.text)


# Retriving all childrens
for book in root.findall('book'):
    print(book.get('title'))
# Dont know how this line work
for author in root.findall('author'):
    print(author.text)
print()


# find returns the first element
print(root.find('book').get('title'))