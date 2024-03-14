"""
Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do 
desconto e o preço final do produto.
"""
print("==============Descontão Relampago! Cadastre-se já e aproveite!==============\n")

while True:
    price = input("Digite o preço do seu produto: ")
    discountPercentual = input("Digite o percentual de desconto a ser aplicado (0/100)%: ")

    if not price.replace(".", "").isnumeric() or not discountPercentual.replace(".", "").isnumeric():
        print("\nValor inserido é invalido. Digite novamente\n")

    else:
        price = float(price)
        discountPercentual = float(discountPercentual)
        if not discountPercentual <= 100 or not discountPercentual >=0:
            print("\nDesconto digitado fora do limite aceitavel\n")
        else:
            break

discountValue = price * (discountPercentual/100)
finalPrice = price - discountValue

print("\nDesconto aplicado: R$%.2f\nPreço final: %.2f" %(discountValue, finalPrice))