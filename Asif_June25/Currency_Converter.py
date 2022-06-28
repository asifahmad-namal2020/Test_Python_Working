
One_Dollar = 208
Error_Message = 'Please Enter a Valid Number'
User = input('Press 1 for Dollar to Rupess or 2 for Rupees to Dollar: ')
if not User.isdigit():
    print(Error_Message)
else:
    if int(User) == 1:
        User_Input_in_Dollar = input('Enter Currency in Dollar: ' )
        if User_Input_in_Dollar.isdigit():
            print('Currency in Rupees is : ',float(User_Input_in_Dollar)*One_Dollar)
        else:
            print(Error_Message)

    elif int(User) == 2:
        User_Input_in_Rupees = input('Enter Currency in Rupees: ')
        if User_Input_in_Rupees.isdigit():
            print('Currency in Dollar is: ', float(User_Input_in_Rupees) / One_Dollar)
        else:
            print(Error_Message)
    else:
        print(Error_Message)

