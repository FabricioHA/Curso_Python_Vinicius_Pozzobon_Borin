"""
Desenvolva um algoritmo que converta uma temperatura em Celsius (C) para Fahrenheit (F). A equação de conversão é:
"""

while True:

    celsius = input("Digite a temperatura em Celsius (C°): ")
    
    if not celsius.replace(".", "").isnumeric():
        print("Valores invalidos")
    
    else:
        celsius = float(celsius)
        break

fahrenheit = (9*celsius)/5+32

print("A temperatura de %.2fC° convertida em Fahrenheit é de %.2fF°" %(celsius, fahrenheit))