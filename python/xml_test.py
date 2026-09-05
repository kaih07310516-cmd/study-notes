import xml.etree.ElementTree as ET
data = '''<person>
    <name>hk</name>
    <phone type = "intl">
        +15060258626
      </phone>
      <email hide = "yes"/>
 </person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))