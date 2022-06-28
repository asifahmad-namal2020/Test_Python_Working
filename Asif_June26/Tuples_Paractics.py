
for i in enumerate(range(1,10)):
    print(i)
print('\n')

animal = ['cat','dog','Monkey']
for index, item in enumerate(animal, 2):
    print(index,item)

List_1 = list()
for index,item in enumerate(animal,3):
    List_1.append(index)
    List_1.append(item)
print(List_1)
print('\n')

# Orignal and Copied both are changed

Fruits = ['Mango','Cherry', 'Apple']
Fruit_Copy = Fruits
print(Fruit_Copy)
Fruit_Copy.append('Banana')
print(Fruit_Copy)
print(Fruits)
print('\n')

# Another example

Computer = ['Mouse','Keybaord','LCD']
Computer_System = Computer
print(Computer_System)
Computer_System.append('Wifi')
print(Computer_System)
print(Computer)
print('\n')

# Change in Copy Only

Computer = ['Mouse','Keybaord','LCD']
Computer_System = Computer.copy()
print(Computer_System)
Computer_System.append('Wifi')
print(Computer_System)
print(Computer)
print('\n')



