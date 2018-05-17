def calc_tax(income):
  a=income-88000-90000-128000
  if a<=540000 :
    return int(a*0.05) 
  elif a>540000 and a<=1210000 :
    return int(a*0.12 - 37800)
  elif a>1210000 and a<=2420000 :
    return int(a*0.2-134600)
  elif a>2420000 and a<=4530000 :
    return int(a*0.3 - 376600)
  elif a>4530000 and a<=10310000 :
    return int(a*0.4 - 829600)
  else :
    return int(a*0.45 - 1345100)
