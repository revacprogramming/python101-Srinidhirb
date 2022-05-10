hrs = input("Enter Hours:")
h = float(hrs)
rte = input("enter the rate:")
r= float(rte)
if(h>40) :
   #a=h*r
    b=(h-40) * (r*1.5)
    pay= (40*r) + b
    print(pay)
else :
    pay = h*r
    print(pay)
    