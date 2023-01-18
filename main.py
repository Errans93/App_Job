import os
from xml.dom import minidom


file = os.listdir(r'C:\IMA')
print('Ci sono queste macchine disponibili:\n')

for f in file:
    print(f)
print()

fil = input('Inserisci il tipo di macchina\n')


file = os.listdir(r'C:\IMA' + '\\' + fil)
print()
for f in file:
    print(f)
print()


# parse an xml file by name
file = minidom.parse(r'C:\Users\edoar\OneDrive\Documenti\Progetti_git\App_Job\prova.xml')

# use getElementsByTagName() to get tag
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
