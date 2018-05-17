def calc_tax(income):
    free=88000+90000+128000
    tax=income-free
    if(tax<=540000):
        return int(tax*0.05)
    elif(tax<=1210000 and tax>540000):
        return int((tax*0.12)-37800)
    elif(tax<=2420000 and tax>1210000):
        return int((tax*0.2)-134600)
    elif(tax<=4530000 and tax>2420000):
        return int((tax*0.3)-376600)
    elif(tax<=10310000 and tax>4530000):
        return int((tax*0.4)-829600)
    elif(tax>10310000):
        return int((tax*0.45)-1345100)
    else:
        return 0
