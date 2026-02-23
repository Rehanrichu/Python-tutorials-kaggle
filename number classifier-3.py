x = int(input("Add the number ="))
if x == 0 :
    sign ="zero"
elif x >= 1 :
    sign = "positive"
else:
    sign ="negative"
if x%2 == 0:
    parity = "even"
else:
    parity = "odd"

print("the number",x,"is",sign,"and",parity)
