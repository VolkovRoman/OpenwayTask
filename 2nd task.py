import sys


def calc_A():
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    all_inputs = (a, b, c, d)

    for i in all_inputs:
        if len(str(i)) > 17:
            print("Error! Only 17 characters allowed!")
            sys.exit()

    try:
        summ = (a + b) / (c + d)
        print(summ)

    except ZeroDivisionError:
        print("Division by zero")
    except ValueError:
        print("Wrong type of data")


calc_A()
