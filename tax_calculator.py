def calc_tax(income):
	money=income-88000-90000-128000
	if money>0 and money<=540000:
	   return int(money*0.05)
	elif money>540000 and money<=1210000:
	   money=int((540000*0.05)+((money-540000)*0.12))
	   return money
	elif money>1210000 and money<=2420000:
	   money=int((540000*0.05)+((1210000-540000)*0.12)+((money-1210000)*0.2))
	   return money
	elif money>2420000 and money<=4530000:
	   money=int((540000*0.05)+((1210000-540000)*0.12)+((2420000-1210000)*0.2)+((money-2420000)*0.3))
	   return money
	elif money>4530000 and money<=10310000:
	   money=int((540000*0.05)+((1210000-540000)*0.12)+((2420000-1210000)*0.2)+((4530000-2420000)*0.3)+((money-4530000)*0.4))
	   return money
	elif money>10310000:
	   money=int((540000*0.05)+((1210000-540000)*0.12)+((2420000-1210000)*0.2)+((4530000-2420000)*0.3)+((10310000-4530000)*0.4)+((money-10310000)*0.45))
	   return money

	else:
	    return 0
