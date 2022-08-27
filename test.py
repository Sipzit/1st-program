from ast import Pass
from encodings import search_function
from re import T
import time


#conversion type 
conversion_system = input("Metric to standard or Standard to metric: ")


#user input imperial
standard = False
metric = False

if "standard to metric" in conversion_system.lower():
    standard = True
    if standard == True:
        conversion_type1 = input("What unit are you wanting to convert:foot, yard, or mile: ")
        ft = "foot" in conversion_type1
        yd = "yard" in conversion_type1
        ml = "mile" in conversion_type1

        conversion_type2 = input("What unit do you want:centimeter, meter, kilometer: ")
        cm = "centimeter" in conversion_type2
        m = "meter" in conversion_type2
        km = "kilometer" in conversion_type2
        
        #Feet conversion
        if ft == True and cm == True:
            num1 = input("Feet: ")
            answer = int(num1)*30.48
            print(str(answer) + str("cm"))
        if ft == True and m == True:
            num1 = input("Feet: ")
            answer = int(num1)*0.3048
            print(str(answer) + str("m"))
        if ft == True and km == True:
            num1 = input("Feet: ")
            answer = int(num1)*0.0003048
            print(str(answer) + str("km"))
       
        #Yard conversion
        if yd == True and cm == True:
            num1 = input("Yard: ")
            answer = int(num1)*91.44
            print(str(answer) + str("cm"))
        if yd == True and m == True:
            num1 = input("Yard: ")
            answer = int(num1)*0.9144
            print(str(answer) + str("m"))
        if yd == True and km == True:
            num1 = input("Yard: ")
            answer = int(num1)*0.000914
            print(str(answer) + str("km"))

        #Mile conversion
        if ml == True and cm == True:
            num1 = input("Miles: ")
            answer = int(num1)*160934.4
            print(str(answer) + str("cm"))
        if ml == True and m == True:
            num1 = input("Miles: ")
            answer = int(num1)*1609.344
            print(str(answer) + str("m"))
        if ml == True and km == True:
            num1 = input("Miles: ")
            answer = int(num1)*1.60
            print(str(answer) + str("km"))
        else:
            print("error")


#Metric to standard conversion

    if "metric to standard" in conversion_system:
        standard = True
    if standard == True:
        conversion_type1 = input("What unit do you want:centimeter, meter, kilometer: ")
        cm = "centimeter" in conversion_type1
        m = "meter" in conversion_type1
        km = "kilometer" in conversion_type1

        conversion_type2 = input("What unit are you wanting to convert:foot, yard, or mile: ")
        ft = "foot" in conversion_type2
        yd = "yard" in conversion_type2
        ml = "mile" in conversion_type2
        

        #Centimeter conversion
        if cm == True and ft == True:
            num1 = input("Centimeter: ")
            answer = int(num1)/30.48
            print(str(answer) + str("cm"))
        if cm == True and yd == True:
            num1 = input("Centimeter: ")
            answer = int(num1)/91.44
            print(str(answer) + str("m"))
        if cm == True and ml == True:
            num1 = input("Centimeter: ")
            answer = int(num1)/160900
            print(str(answer) + str("km"))
       
        #Meter conversion
        if m == True and ft == True:
            num1 = input("Meter: ")
            answer = int(num1)*3.281
            print(str(answer) + str("cm"))
        if m == True and yd == True:
            num1 = input("Meter: ")
            answer = int(num1)*1.094
            print(str(answer) + str("m"))
        if m == True and ml == True:
            num1 = input("Meter: ")
            answer = int(num1)/1609
            print(str(answer) + str("km"))

        #Kilometer conversion
        if km == True and ft == True:
            num1 = input("Kilometer: ")
            answer = int(num1)*3281
            print(str(answer) + str("cm"))
        if km == True and yd == True:
            num1 = input("Kilometer: ")
            answer = int(num1)*1094
            print(str(answer) + str("m"))
        if km == True and ml == True:
            num1 = input("Kilometer: ")
            answer = int(num1)/1.609
            print(str(answer) + str("km"))
        else:
            print("error")
    time.sleep(4)

    
