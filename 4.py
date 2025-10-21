#Список CharCode, но только для валют с Nominal=10 или Nominal=100
import xml.dom.minidom as minidom 

xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute') 
list = [] 

for node in elements:
    for child in node.childNodes: 
        if child.nodeType == 1: 
            if child.tagName == 'CharCode': 
                if child.firstChild.nodeType == 3: 
                    char_code = child.firstChild.data
            if child.tagName == 'Nominal': 
                if child.firstChild.nodeType == 3: 
                    nominal = child.firstChild.data
    
    if nominal and char_code:
        if nominal in ['10', '100']:
            list.append(char_code)


print("Список CharCode для валют с Nominal = 10 или Nominal = 100:")
for char_code in list:
    print(char_code)

xml_file.close()