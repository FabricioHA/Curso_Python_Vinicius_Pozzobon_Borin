"""
Existem várias formas de fazer uma Composições entre strings e valores numéricos.
Começando com a F-STRING, ela permite concatenar uma string em um formato agil, como veremos abaixo um exemplo

texto = f"Oi {frase1}, tudo bem?"

Nessa estrutura, podemos simplesmente colocar um f de format na frente para indicar uma f-string. Os colchetes indicam
onde a string será inserida, permitindo a incerção de valores númericos.
"""

idade = 75
totalDate = f"isso foi a mais de {idade} anos ( Composição com f-string )"
print(totalDate)

totalDate = "isso foi a mais de {} anos ( Composição com .format() )".format(idade,)
print(totalDate)

totalDate = ("isso foi a mais de %s anos (Composição com percentuals)" %(idade))    
print(totalDate)