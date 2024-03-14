"""
Desenvolva um algoritmo para calcular o tempo de redução de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que o fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá, Exiba o total em dias.
"""

"""
dia = 1440 minutos = 86400 segundos
1 hora = 60 minutos = 3600 segundos
1 minuto = 60 segundos
"""

while True:

    cigPerDay = input("Quantos cigarros o paciente consome por dia? ")
    yearSmoked = input("Por quantos anos o paciente já fumou? ")

    if not cigPerDay.isnumeric() or not yearSmoked.isnumeric():
        print("\nValores inválidos. Digite novamente\n")        
    else:
        cigPerDay = int(cigPerDay)
        yearSmoked = int(yearSmoked)
        break

totalCig = cigPerDay * (yearSmoked*365)

daysLost = ((totalCig*10)/60)//24

print("\nO paciente perderá %d dias ao fumar %d cigarros por dia" %(daysLost, totalCig))

"""
Nessa lógica, precisamos saber quantos minutos um ano totalizara para sabermos quantos dias ele perdeu.
a cada cigarro, ele perde 10 minutos, então multiplicaremos o número de cigarros vezes a quantidade de minutos perdidos, 
dando os minutos totais. depois, iremos dividir esses minutos em horas (60 minutos) para no fim dividirmos essas 
horas em dias (24 horas)
"""