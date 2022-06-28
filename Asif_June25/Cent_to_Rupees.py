
Unit_Dollar = 208  # One Dollar to 208 Rupees
Error_Message = 'Please Enter a Valid Number'

User = input('Enter input for Currency Coversion: ')
if User.isdigit():
    if int(User) == 1:
        Penny = eval(input(('Enter number of Penny: ' )))
    else:
        print(Error_Message)


Nickel = eval(input(('Enter number of Nickel: ' )))

Dime = eval(input(('Enter number of Dime: ' )))

Quarter = eval(input(('Enter number of Quarter: ' )))



Unit_Penny = 1 # 1 penny to 1 cent
Unit_Nickel = 5 # 1 Nickel to 5 cent
Unit_Dime = 10  # 1 Dime to 10 cent
Unit_Quarter = 25  # 1 Dime to 25 cent

Total_Number_of_Cents = ((Penny*Unit_Penny)+(Nickel*Unit_Nickel)+(Dime*Unit_Dime)+(Quarter*Unit_Quarter))
Total_Number_of_Cents_Round_Off = round(Total_Number_of_Cents,3)
print('Total Number of Cents is equal to: ',Total_Number_of_Cents_Round_Off)
One_Dollar = 100      # One_Dollar to equal to 100 cents
Total_Number_of_Dollar = Total_Number_of_Cents_Round_Off/One_Dollar
print('Total Number of Dollar $ is: ',Total_Number_of_Dollar)
print('Total Currency in Rupees is: ',Total_Number_of_Dollar*Unit_Dollar)