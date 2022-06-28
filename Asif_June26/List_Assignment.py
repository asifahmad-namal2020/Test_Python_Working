# Printing name of programming languages using for loop
Languages_List = ['C','C++','Java','Python','Ardunio']
for i in Languages_List:
    print('A Nice Programming Language is',[i])

# Append
New_Languages_List = ['C','C++','Java','Python','Ardunio']
New_Languages_List.append('Assembly')
print(New_Languages_List)

# POP
New_Languages_List.pop()
print(New_Languages_List)

#POP(i)
New_Languages_List.pop(0)
print(New_Languages_List)

# Insert
New_Languages_List.insert(0,'C')
print(New_Languages_List)

# Remove
New_Languages_List.remove("C")
print(New_Languages_List)

#Reverse
New_Languages_List = ['C','C++','Java','Python','Ardunio']
New_Languages_List.reverse()
print(New_Languages_List)

# Sort_Reverse
New_Languages_List.sort(reverse=True)
print(New_Languages_List)
print('\n')

# Sort
New_Languages_List.sort()
print(New_Languages_List)

# Sorted
print(sorted(New_Languages_List))
