"""
Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos. Calcule o total de segundos resultante e imprima na tela para o usuário.

1 dia = 86400 segundos
1 hora = 3600 segundos
1 = 60 segundos
1 segundo = 1000 milisegundos 
"""

print("=========Bem vindo ao programa de soma de segundos=========\n\n")

while True:
    while True:
        day = input("Digite a quantidade de dias: ")
        hour = input("Digite a quantidade de horas: ")
        minutes = input("Digite a quantidade de minutos: ")
        seconds = input("Digite a quantidade de segundos: ")

        if not day.isnumeric() or not hour.isnumeric() or not minutes.isnumeric() or not seconds.isnumeric():
            print("\nErro: valores digitados são inválidos. Digite novamente...\n")
        else:
            break
    
    day = int(day)
    hour = int(hour)
    minutes = int(minutes)
    seconds = int(seconds)

    if hour > 24 or minutes > 60 or seconds > 60:
        print("\nValores excedem o limite determinado. Digite novamente\n")
    else:
        break
        

totalSeconds = day * 86400
totalSeconds = totalSeconds + (hour*3600)
totalSeconds = totalSeconds + (minutes*60)
totalSeconds = totalSeconds + seconds

print("\n\nO número total de segundos é de %d segundos" %(totalSeconds))