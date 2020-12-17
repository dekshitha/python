hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate per hour:")
r=float(rate)
if(h<=40):
    gpay=r*h;
    print(gpay)
elif(h>40):
    reg=r*h;
    eh=(h-40)*0.5*r;
    pay=reg+eh;
    print(pay)
else:
    print('invalid input')
          
