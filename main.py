from xml.dom import minidom


workbook = xlsxwriter.Workbook('hello.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'Geeks')
worksheet.write('C1', 'For')
worksheet.write('D1', 'Geeks')

# Finally, close the Excel file
# via the close() method.
workbook.close()

# parse an xml file by name
file = minidom.parse('prova.xml')

#use getElementsByTagName() to get tag
models = file.getElementsByTagName('model')
machines = file.getElementsByTagName('machine')

# one specific item attribute
print('model #2 attribute:')
print(models[1].attributes['name'].value)
print(machines[0].attributes['Type'].value)
print(machines[0].attributes['ifixName'].value)
print(machines[0].attributes['Historian'].value)
print(machines[0].attributes['MachineDescription'].value)
print(machines[0].attributes['PLCType'].value)
print(machines[0].attributes['Base'].value)
print(machines[0].attributes['Type'].value)

# all item attributes
print('\nAll attributes:')
for elem in machines:
  print(type(elem))


# one specific item's data
print('\nmodel #2 data:')
print(models[1].firstChild.data)
print(models[1].childNodes[0].data)

# all items data
print('\nAll model data:')
for elem in models:
  print(elem.firstChild.data)