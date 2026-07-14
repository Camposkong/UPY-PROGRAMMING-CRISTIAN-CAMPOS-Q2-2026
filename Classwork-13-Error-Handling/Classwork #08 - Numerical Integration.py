import math

#INPUT
a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Write the integration method (LRM/RRM/MRM/TM): ")

#PROCESS
try:
    if method not in ["LRM", "RRM", "MRM", "TM"]:
        raise ValueError("El método de integración no es válido. Usa LRM, RRM, MRM o TM.")
except ValueError as e:
    print(e)
    exit()

try:
    if f_x.strip() == "":
        raise ValueError("No escribiste ninguna función")
except ValueError as e:
    print(e)
    exit()

try:
    if "y" in f_x:
        raise ValueError("La función debe estar escrita en términos de x.")
except ValueError as e:
    print(e)
    exit()

try:
     if "^" in f_x:
        raise ValueError("'^' no es el operador de potencia en Python, es '**'")
except ValueError as e:
    print(e)
    exit()
    
try:
     if a != "pi":
          float(a)
except ValueError:
     print("Error: el límite inferior no es un número")
     exit()
           
if "pi" in a:
     a = math.pi
else:
        a = float(a)

try:
     if b != "pi":
          float(b)
except ValueError:
     print("Error: el límite superior no es un número")
     exit()

if "pi" in b:
    b = math.pi
else:
    b = float(b)

try:
    if a >= b:
        raise ValueError("El límite inferior debe ser menor que el límite superior.")
except ValueError as e:
    print(e)
    exit()

n = 1000
h = (b - a) / n


try:
    for i in range(n + 1):
        xi = a + i * h
        eval(f_x.replace("x", str(xi)))
except ZeroDivisionError:
    print("La función no está definida en algún punto del intervalo.")
    exit()

area = 0.0
shift = 0
constant = 0
variable = 0

if method == "RRM":
    shift = 1

if method == "MRM":
    constant = h / 2

if method == "TM":
    variable = 1

    f_0 = f_x.replace("x", str(a))
    area += (h / 2) * eval(f_0)

    for i in range(variable, n):
        xi = a + i * h
        f_xi = f_x.replace("x", str(xi))
        area += (h / 2) * 2 * eval(f_xi)

    f_xn = f_x.replace("x", str(b))
    area += (h / 2) * eval(f_xn)

else:

    for i in range(shift, n + shift):
        xi = a + i * h
        height = f_x.replace("x", str(xi + constant))
        area += h * eval(height)

#OUTPUT
print(f"The integration of {f_x} is {area:.3f}")