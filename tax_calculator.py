
def calc_tax(income):
	all=88000+90000+128000
	money = income -all

	if money<=540000:
		return int(money*0.05)

	elif money>540000 and money<=1210000:
		return int((540000*0.05)+(money-(540000))*0.12)
	elif money>1210000 and money<=2420000:
		return int((540000*0.05)+(670000*0.12)+(money-1210000)*0.2)
	elif money>2420000 and money<=4530000:
		return int((540000*0.05)+(670000*0.12)+(1210000*0.2)+(money-2420000)*0.3)
	elif money>4530000 and money<=10310000:
		return int((540000*0.05)+(670000*0.12)+(1210000*0.2)+(2110000*0.3)+(money-4530000)*0.4)
	else:
		return int((540000*0.05)+(670000*0.12)+(1210000*0.2)+(2110000*0.3)+(5780000*0.4)+(money-10310000)*0.45)


