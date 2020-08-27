def tickets():
    '''
    asks if you are disabled or not the you pay for paking and subbtrakts
    '''
    ticket_giver = input("are you disabled yes(y) or no(n): ")
    if ticket_giver == 'y':
        print("You are paying 100")
        paying = int(input("pls pay the ammount: "))
        minuse = 100 - paying
        
        if paying > 100:
            print("to much")
        elif paying == 100:
            print("thankyou")
        else:
            print("not yet")
            print(paying)
            print(minuse)
    elif ticket_giver == 'n':
        print('you are paying 500')
        paying_2 = int(input("pls pay the ammount: "))
        minusing = 500 - paying_2
        print(minusing)
        if paying_2 > 500:
            print("to much")
            print("your chage is")
            change = paying_2 - 500
        elif paying_2 == 500:
            print("thankyou")
        else:
            print("not yet")
            print(paying_2)
tickets()