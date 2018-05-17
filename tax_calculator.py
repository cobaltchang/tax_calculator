def calc_tax(income):
	myself = income -88000 - 90000 - 128000
	if(myself <= 540000):
		return  int(myself *0.05)
	elif(myself <= 1210000):
		return int ((myself * 0.12)-37800)
	elif(myself <= 2420000):
		return int((myself * 0.20)-134600)
	elif(myself <= 4530000):
		return int((myself * 0.30)-376600)
	elif(myself <= 10310000):
		return int((myself * 0.40)-829600)
	else:
		return int((myself * 0.45)-1345100)
	return 0
	
