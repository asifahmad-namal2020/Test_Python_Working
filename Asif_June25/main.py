'''User = eval(input('Press 1 for Kilometer to Miles or 2 for Miles to KM: '))

if User.isdigit():
    print('Enter a valid input')
elif User == 1:
    Input_in_KM = float(input('Enter Distance in KM: '))
    Distance_in_Miles = (Input_in_KM/0.62)
    For_Round_Off = round(Distance_in_Miles,3)
    print('Distance in miles is: ',For_Round_Off)

elif User == 2:
    Input_in_Miles = float(input('Enter Distance in Miles: '))
    Distance_in_Km = Input_in_Miles*0.62
    For_Round_Off = round(Distance_in_Km)
    print('Distance in kilometer is: ',For_Round_Off)
else:
    print(Error_Message)'''

Error_Message = 'Please Enter a Valid Number'
One_KM = 0.62 # Miles

User = input('Press 1 for Kilometer to Miles or 2 for Miles to KM: ')
if not User.isdigit():
    print(Error_Message)
else:
    if int(User) == 1:
        User_Input_in_KM = input('Enter Distance in KM: ' )
        if User_Input_in_KM.isdigit():
            print('The Distance in Miles is : ',float(User_Input_in_KM)*One_KM)
        else:
            print(Error_Message)
    elif int(User) == 2:
        User_Input_in_Miles = input('Enter Distance in Miles: ')
        if User_Input_in_Miles.isdigit():
            print('The Distance in KM is: ' ,float(User_Input_in_Miles)/One_KM)
        else:
            print(Error_Message)
    else:
        print(Error_Message)

