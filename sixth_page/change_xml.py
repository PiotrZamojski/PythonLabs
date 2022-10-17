from importlib.resources import path
import xml.etree.ElementTree as et

pathIn = ".\\fifth_page\\old.xml"
pathOut = ".\\fifth_page\\new.xml"
tree = et.parse(pathIn)
rootElement = tree.getroot()
for element in rootElement.findall("food"):
        element.find('price').text = "50.01$"
tree.write(pathOut)