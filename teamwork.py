def tickets(disabled,users):
    '''
    cheks if disabeld or not
    '''
    a = input("are you disabled or not: ")
    if a == 'disabled':
        disabled = 200
        return disabled
    elif a == 'not':
        users = 500
        return users
tickets(200,500)
    