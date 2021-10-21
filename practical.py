net_amount=0
select_month=input("Enter the desired Month: ")
days=int(input("No of Days you were present:  "))
month = {"jan":31, "feb":29, "march":31, "apr":30, "may":31, "jun":30, 
       "jul":31, "aug":31, "sep":30, "oct":31, "nov":30, "dec":31}


net_amount=0
while(net_amount<=0):
  while input("Enter y to continue: ")=="y":
    a = input("Enter input: ")
    trans = a.split(" ")
    b=trans[1]
    amt=int(trans[0])
    
    if b=="d":
      if days <=month[select_month]:
        net_amount+= amt+days * 2000
    elif b=="w":
      if days <=month[select_month]:
        net_amount-=amt-days * 2000
    else:
      pass
print("Total Balance:", net_amount)
