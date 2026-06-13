import math

#INPUT
a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")

if "pi" in a:
    a = eval(a.replace("pi", str(math.pi)))
else:
    a = float(a)

if "pi" in b:
    b = eval(b.replace("pi", str(math.pi)))
else:
    b = float(b)

f_x = input("Write the function to integrate: ")
method = input("Select integration Method (LRM/RRM/MPM/TRP): ")

#PROCESS
area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0

if method == "RRM":
    shift = 1

elif method == "MPM":
    constant = h / 2

for i in range(0 + shift, n + shift):

    if method == "TRP":

        x_left = a + i * h
        x_right = x_left + h

        height_left = eval(f_x, {"math": math}, {"x": x_left})
        height_right = eval(f_x, {"math": math}, {"x": x_right})

        area += ((height_left + height_right) / 2) * h

    else:

        xi = a + i * h + constant

        height = eval(f_x, {"math": math}, {"x": xi})

        area += height * h

#OUTPUT
print(f"The integral of {f_x} is {area:.4f}")