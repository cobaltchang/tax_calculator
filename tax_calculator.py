def calc_tax(income):
    free=88000+90000+128000
    money = income-free
    if money<=0:
        money = 0
    elif money>0 and money<=540000:      
        income=money*0.05
        return int(income)
    elif money>540000 and money<=1210000:
        income = (money-540000)*0.12+540000*0.05
        return int(income)
    elif money>1210000 and money<=2420000:
        income = (money-1210000)*0.2+(1210000-540000)*0.12+540000*0.05
        return int(income)
    elif money>2420000 and money<=4530000:
        income = (money-2420000)*0.30+(2420000-1210000)*0.2+(1210000-540000)*0.12+540000*0.05
        return int(income)
    elif money>4530000 and money<=10310000:
        income = (money-4530000)*0.4+(4530000-2420000)*0.30+(2420000-1210000)*0.2+(1210000-540000)*0.12+540000*0.05
        return int(income)
    else:
        income = (money-10310000)*0.45+(10310000-4530000)*0.4+(4530000-2420000)*0.30+(2420000-1210000)*0.2+(1210000-540000)*0.12+540000*0.05
        return int(income)
    return 0
