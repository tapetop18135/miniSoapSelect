from zeep import Client
from lxml import etree 
import xmlschema


client = Client('http://127.0.0.1:8000/soapAPI1/?wsdl')

resultXMLtest = client.service.setTempData("81603","20")
print(resultXMLtest)

resultXMLtest = client.service.getTempData("get_temp")
# print(resultXMLtest)
# root = etree.fromstring(resultlistfood)
# for food in root.findall('food'):
#     print("name :",food.find('name').text)
#     print("price :",food.find('price').text)
#     print("descr :",food.find('description').text.replace('\n',' '))
#     print("cal :",food.find('calories').text)
#     print()

# # print(resultXMLtest)

print("/////////////////////// result ////////////////////////////////////")
utf8_parser = etree.XMLParser(encoding='utf-8')
root = etree.fromstring(resultXMLtest.encode('utf-8'), parser=utf8_parser)
# print(root)
for food in root.findall('item'):
    print("room id :",food.find('room_id').text)
    print("temp :",food.find('temp').text)
    print("date :",food.find('date').text)
    print()

