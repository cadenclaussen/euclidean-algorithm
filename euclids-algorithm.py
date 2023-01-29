import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
try: 
    findGCD = sys.argv[3]
except:
    findGCD = "0"
try: 
    p = sys.argv[4]
except:
    p = "1"

if a / 1000000000000 > 1 or b / 1000000000000 > 1:
    print("Your numbers are to large")
    sys.exit()

if findGCD == "0":
    while a != b:
        if a > b:
            count = 1
            while a - b * count > b:
                count += 1
            a -= b * count
        else:
            count = 1
            while b - a * count > a:
                count += 1
            b -= a * count
        if p != 0:
            print("(" +str(a)+ "," +str(b)+ ")")
        
    print("")
    if a == 1:
        print(a)
        print("The two numbers you inputed are relatively prime")

else: 
    while a != b and a != int(findGCD) and b != int(findGCD):
        if a > b:
            a -= b
        else:
            b -= a

        if p != 0:
            print("(" +str(a)+ "," +str(b)+ ")")
            
