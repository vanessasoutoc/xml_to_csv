import requests
import xml.etree.ElementTree as ET
import csv
import os

# get the xml file
def get_xml(url, xml_file):
    data = requests.get(url)    # send request to url
    with open(xml_file, 'wb') as f: # open file and save xml
        f.write(data.content)
        
        
# tags file xml
def tags_xml(xml_file):
    tree = ET.parse(xml_file)   # import xml from
    root = tree.getroot()
    elem_list = [] # list tags file xml
    for elem in root.findall('./DESPESAS/DESPESA'):
        for child in elem:
            elem_list.append(child.tag)
            
            
        #
        #print(elem_list)
        #break
    return list(set(elem_list))



# parse xml file
def parse_xml(xml_file):
    tree = ET.parse(xml_file)   # import xml from
    
    root = tree.getroot()  # find the root element of xml
    despesas_list = []  # list to store the xml
    for item in root.findall('./DESPESAS/DESPESA'):    # find all DESPESAS/DESPESA node
        despesa = {}              # dictionary to store content of each DESPESA
        for child in item:
            despesa[child.tag] = child.text   # add item to dictionary 

        despesas_list.append(despesa)    # add dictionary to the list
    return despesas_list   # return the complete list

# save as csv
def save_to_csv(data, csv_file, elements):
    with open(csv_file,'w') as f:
        writer = csv.DictWriter(f, fieldnames = elements)    # creating a DictWriter object
        writer.writeheader()    # write headers to csv
        writer.writerows(data)  # write each dictionary element of the list row by row


#url = "http://www.xmlfiles.com/examples/plant_catalog.xml"  # url where the xml file is available
xml_file = input("Caminho completo do arquivo: ")  # file where the xml is saved
head, tail = os.path.split(xml_file)

name_file = os.path.splitext(os.path.basename(tail))[0]
csv_file = name_file + ".csv"  # file where data is saved in csv format

#get_xml(url,xml_file)
tags = tags_xml(xml_file)
all_data = parse_xml(xml_file)
save_to_csv(all_data,csv_file,tags)
print("XML Parsing Successful")
