unit = input("Is this temperature in Celcius or fahrenheit (C/F):")
temp = float(input("Enter the temperature:"))

if unit.upper() == "C":
    temp = round((9 * temp)/5 + 32, 1)    #(C x 9/5)+32=F
    print(f"The Temperature in fahrenheit is {temp}°")
elif unit.upper() == "F":
    temp = round((temp - 32) * 5 / 9, 1)  #(F - 32)*5/9=C
    print(f"The Temperature in Celcius is {temp}°")
else:
    print(f"Your {unit} is invalid \n please,enter either C or F !")



