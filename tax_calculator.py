def calc_tax(income):
    free = 88000 + 90000 + 128000
    money = income-free
    if money <= 540000:
       return int(money * 0.05)
    elif money > 540000 and money <= 1210000:
       return int(money * 0.12 - 37800)
    elif money > 1210000 and money <= 2420000:
       return int(money * 0.20 - 134600)
    elif money > 2420000 and money <= 4530000:
       return int(money * 0.30 - 376600)
    elif money > 4530000 and money <= 10310000:
       return int(money * 0.40 - 829600)
    elif money > 10310000:
       return int(money * 0.45 - 1345100)
    else:
       return 0
