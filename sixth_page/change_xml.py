from importlib.resources import path
import xml.etree.ElementTree as et

pathIn = ".\\sixth_page\\old.xml"
pathOut = ".\\sixth_page\\new.xml"
tree = et.parse(pathIn)
rootElement = tree.getroot()
for element in rootElement.findall("food"):
        element.find('price').text = "50.01$"
tree.write(pathOut)