students = ['Imran', 'Ali', 'Hamza', 'Ahmad']
print(students)
print('\n')

students = ['Imran',60, 70,100,'Ali','Hamza',39,'Ahmad']
print(students)
print(students[0])
print(students[4])
print(students[7])
print('\n')

print(type(students[1]))
print(type(students[0]))

for students in students:
    print(students)
print('\n')

list_1 = list()
print(type(list_1))
print('\n')

list_2 = [0,1,1,2,2,3]
print(list_2)
print('\n')

students = ['imran', 'Ali', 'Hamza', 'Ahmad']
print(students[0].title())
print(students[3].title())
print('\n')

for students in students:
    print(students.title())
print('\n')

list_3 = [2]*10
print(list_3)
print(type(list_3))
print('\n')

students = ['imran', 'Ali', 'Hamza', 'Ahmad']
print(students[-1])
print(students[-2])
print(students[-3])
print('\n')

students = ['imran', 'Ali', 'Hamza', 'Ahmad']
students.append('Asif')
print(students)
students.append(['Ali','Hamza'])
print(students)
print(students[-1])
print('\n')
print('\n')

#students = ['imran', 'Ali', 'Hamza', 'Ahmad']
for students in students:
    if type(students) == list:
        for s in students:
            print(s)
    else:
        print(students)
print('\n')
print('\n')

# Last removing last element
students = ['imran', 'Ali', 'Hamza', 'Ahmad']
print(students.pop())
print(students)
print('\n')

# Adding some element index 1
students.insert(1,'Salman')
print(students)
print('\n')

# Adding two list
EE_Class = ['Asif','Waqas','Zohaib']
Address = ['Peshawar','DI Khan','AJ Kashmir']
Mixed_List = EE_Class+Address
print(Mixed_List)
print('\n')
print('\n')

# Reverse List

List_Reverse = ['a','b','c']
print(List_Reverse)
print(List_Reverse.reverse())

# Sorting
List_Reverse.sort(reverse=True)
print(List_Reverse)
print(sorted(students))
#print(students.sort())
print(students)
print('\n')

# Clear List
print(students.clear())
print('\n')

# Modify List
Fruits = ['Mango','Cherry', 'Apple']
Fruits[1] = 'Banana'
print(Fruits)
print('\n')

Fruits.append("Orange")
print(Fruits.index('Banana'))
print(Fruits)
print('\n')

print(Fruits.count('Mango'))
print('\n')

print('Apple' in Fruits)
print('\n')

print(len(Fruits))
print('\n')

print(Fruits)
del Fruits[2]
print(Fruits)
print('\n')

students = ['Imran', 'Ali', 'Hamza', 'Ahmad','Farhan','Habib','Ahmad']
print(students)
print('1st Batch Student:',students[0:2])      # Range is less than two [ )
print('2nd Batch Student:',students[3:7])
print('\n')

First_Batch = students[:]
print(First_Batch)
print('\n')

for i in range(1,20,3):    # Increment of 3
    print(i)
print('\n')

Numbers = list(range(1,20))
print(Numbers)
print('\n')

Numbers = list(range(1,20,2))
print(Numbers)
print('\n')

Numbers = list(range(1,20,1))
print(Numbers)
print('\n')

Max_Number =max(Numbers)
print(Max_Number)
print('\n')

Min_Number = min(Numbers)
print(Min_Number)
print('\n')

Sum = sum(Numbers)
print(Sum)
print('\n')

