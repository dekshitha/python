score = input("Enter Score: (between 0.0 and 1.0): ")
s=float(score)
if(s>=0.0):
    if(s<=1.0):
        if(s>=0.9):
           print('A')
        elif(s>=0.8):
           print('B')
        elif(s>=0.7):
           print('C')
        elif(s>=0.6):
           print('D')
        elif(s<0.6):
           print('F')
    else:
        print('enter between the given range')
else:
     print('enter between the given range')
