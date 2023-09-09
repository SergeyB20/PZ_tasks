number = input('Enter two-digit number:' )
# check on minus
if str(number)[0] == "-":
    spl = str(number).split('-')
    resOfSpl = spl[1]
# revers of number
    if len(resOfSpl) != 2:
        print('Number is not two-digit')
        pass
    else:
        print("Your reversed number:", '-'+resOfSpl[::-1])

# revers of number without minus
else:
    if len(str(number)) != 2:
        print('Number is not two-digit')
        pass
    else:
        print("Your reversed number:", str(number)[::-1])
