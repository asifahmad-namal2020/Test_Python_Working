# Numbers
#print(2+4)
#print(2*4)
#print(4/3) # Python In division return in float
#print(3**2)
#print(6**6)
#print(5 % 4) # Reminder
#print((2+4)*5)
#print(0.1+0.2)   # Floating numbers have't 100% accurate result, because machine understand machine language
#print(0.1*0.2)   # Floating numbers have't 100% accurate result, because machine understand machine language
#print(3*0.1)     # Floating numbers have't 100% accurate result, because machine understand machine language
#print(0.1*0.2)   # Floating numbers have't 100% accurate result, because machine understand machine language
#print('\n')

#print(0.1+0.2)
print('\n')
print('   18-June-20222   ')
print('\n')
first_name = 'Asif'
print('My Full Name is:',first_name)
last_name = 'Ahmad'
print('My Full Name is:',last_name)
full_name = first_name+' '+last_name
print('My Full Name is:',full_name)
print('My name title is',full_name.title())
print('My full name in upper alphabet is',full_name.upper())
print('My full name in lower alphabet is', full_name.lower())
type_of_name = type(full_name)
print('My name data type is',type_of_name)
White_space_in_name = '   Asif   '
print(White_space_in_name)
print('White Space striped from left side is:',White_space_in_name.lstrip())
print('White Space striped from right side is:',White_space_in_name.rstrip())
print('White Space striped from both sides is:',White_space_in_name.strip())
print('\n')
print('   19-June-20222   ')
print('\n')
Number_1 = float(input('Please enter first number :  ' ))
Number_2 = float(input('Please enter 2nd number :  ' ))
Addition = Number_1+Number_2
Subtraction = Number_1-Number_2
Multiplication = Number_1*Number_2
Division = Number_1/Number_2
Exponent = (Number_1**Number_2)

print('Additon_of_two_numbers is: ',Addition)
print('Subtraction of two number is: ',Subtraction)
print('Multiplication of two number is  ',Multiplication)
print('Division of two number is:  ',Division)
print('Exponent of two number is:  ',Exponent)
print('\n')

print('3rd Equation of Motion: 2as = v^2-vi^2')

Initial_Velocity = float(input('Please enter initial velocity (m/sec): '))
Final_Velocity = float(input('Please enter final velocity (m/sec)^2: '))
Acceleration = float(input('Please enter acceleration (m/sec^2): '))
Distance_Formula = (((Final_Velocity**2)-(Initial_Velocity**2))/(2*Acceleration))
Distance_Formula_Removed_Bracket = ((Final_Velocity**2)-(Initial_Velocity**2)/(2*Acceleration))
print('Actual Distance you covered (m): ', Distance_Formula)
print('After Bracket Removing Distance Covered (m): ',Distance_Formula_Removed_Bracket)

number = eval(input('Enter a number program will find the range r = '))
for i in range(10):                    # Chaotic Function
    number = 3.9 * number * (1-number)
    print(number)

# Part # 3
#number = eval(input('Input a number = '))   # It give the datatype of input
#type(number)



