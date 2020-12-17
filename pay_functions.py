def computepay(h,r):
    if(h<=40):
       gpay=r*h;
       return gpay
    elif(h>40):
       reg=r*h;
       eh=(h-40)*0.5*r;
       pay=reg+eh;
       return pay
    else:
       print('invalid input')


hrs = input("Enter Hours:")
h=h = float(hrs)
rate=input("Enter Rate per hour:")
r=float(rate)
p = computepay(h,r)
print("Pay",p)
