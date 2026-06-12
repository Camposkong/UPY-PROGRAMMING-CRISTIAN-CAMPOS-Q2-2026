#UTFSM verification digit

# Pedir el ROL sin guion ni dígito verificador get rol from user
rol = input("Enter the ROL: ")

# Invertir el número usando while
reversed_rol = ""
i = len(rol) - 1

while i >= 0:
    reversed_rol = reversed_rol + rol[i]
    i = i - 1

# Multiplicadores que se repiten
multipliers = [2, 3, 4, 5, 6, 7]

total = 0
position = 0

# Multiplicar cada dígito por su multiplicador
for digit in reversed_rol:
    total = total + int(digit) * multipliers[position]

    position = position + 1

    # Si llega al final de la lista, vuelve a empezar
    if position == len(multipliers):
        position = 0

# Calcular el dígito verificador
remainder = total % 11
verification_digit = 11 - remainder

# Mostrar resultado
print("The total sum is:", total)
print("The verification digit is:", verification_digit)