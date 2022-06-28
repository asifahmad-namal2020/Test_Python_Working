import math
Value_of_a= eval(input('Please enter the value of a: ' ))
Value_of_b = eval(input('Please enter the value of b: ' ))
Value_of_c = eval(input('Please enter the value of c: ' ))

Sqrt_Value = math.sqrt(Value_of_b**2)-(4*Value_of_a*Value_of_c)

Positive_Root = -Value_of_b + Sqrt_Value/(2*Value_of_a)
Round_Off_Positive = round(Positive_Root,3)
Negative_Root = -Value_of_b - Sqrt_Value/(2*Value_of_a)
Round_Off_Negative = round(Positive_Root,3)
print('Positive Root Value is: ', Round_Off_Positive)
print('Negative Root Value is: ', Round_Off_Negative)


