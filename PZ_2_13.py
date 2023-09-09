def solve(number):
    # check on minus
    if str(number)[0] == "-":
        spl = str(number).split('-')
        ResSpl = spl[1]
        # revers of number
        if len(ResSpl) != 2:
            print('Number is not two-digit')
            start()
        else:
            print("Your reversed number:", '-' + ResSpl[::-1])

    # revers of number without minus
    else:
        if len(str(number)) != 2:
            print('Number is not two-digit or other')
            start()
        else:
            print("Your reversed number:", str(number)[::-1])


def start():
    solve(input('Enter two-digit number:'))


start()

