import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(stuff)
print(lst)
#print(type(lst[0]))
print('User count:', len(lst))

for item in lst:
    print('\nName', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attr', item.get('x'))
    