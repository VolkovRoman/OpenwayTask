def Years(value, interest_rate, mult_incr):
    for y in range(1, 100000000000):
        summ = value*(1+interest_rate/100)**y
        if summ/value > mult_incr:
            print(f'In {y} years, with an interest rate of {interest_rate}% the amount of your deposit will increase {mult_incr} times')
            break


Years(value=float(input()), interest_rate=float(input()), mult_incr=float(input()))
