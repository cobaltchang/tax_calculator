def calc_tax(income):
    income=income-(88000+90000+128000)
    if income<=540000:
      return int(income * 0.05)
    elif income<=1210000:
      return int (income * 0.12 - 37800)
    elif income<=2420000:
      return int(income * 0.2 - 134600)
    elif income<=4530000:
      return int(income * 0.3 - 376600)
    elif income<=10310000:
      return int(income * 0.4 - 829600)
    elif income>=10310001:
      return int(income * 0.45 - 1345100)
    return 0
