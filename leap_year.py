year=int(input())
if year%100 == 0 and year%400 == 0:
    print("Leap year")
elif year%4 == 0:
    print("Leap year")
else:
    print("Not Leap year")        
