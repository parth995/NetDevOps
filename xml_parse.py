# used for my practice

import xmltodict

xml_obj = """
<mydocument has="parth">
   <and>
     <many>patel</many>
     <many>brothers</many>
   </and>
   <plus a="raja">
     rani
   </plus>
</mydocument>
"""

doc = xmltodict.parse(xml_obj)
print(doc)
print(doc['mydocument']['@has'])  #  @ is used to access elements attributes

print("########################################")

with open("netconf.xml", "rb") as f:
    xml_decode = f.read()

#print(xml_decode)

xml_dict = xmltodict.parse(xml_decode, xml_attribs=True)

#int_name = xml_dict["interface"]["name"]

#print(type(int_name))