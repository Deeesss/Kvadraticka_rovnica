print("Program na výpočet kvadratickej rovnice")
print("Tvar rovnice: ax^2 + bx + c = 0")

a = float(input("Zadaj koeficient a: "))
b = float(input("Zadaj koeficient b: "))
c = float(input("Zadaj koeficient c: "))

d = b**2 - 4 * a * c

if d < 0:
    print("Rovnica nemá riešenie v oboru reálných čísiel")
elif d == 0:
    if a != 0:
        x1 = -b / (2 * a)
        print("Rovnice má jeden koreň:")
        print(x1)
    else:
        print("Není kvadratická rovnica")
else:
    if a != 0:
        sqrt_d = d ** 0.5
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        print("Rovnica má dva korene:")
        print(x1)
        print(x2)
    else:
        print("Není kvadratická rovnica")
