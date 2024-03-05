"""
A concatenação de strings pode ser feita com o sinal de +, como por exemplo:
"""

s1 = "Fabricio "
s2 = "holandino"
print(s1+s2)

# Ou, dessa forma:

s1 = s1 + s2
print(s1)

"""
Também podemos multiplicar o numeros de vezes que uma string é exibida na saída,
como imprimir o sinal "-" 10 vezes, como no exemplo abaixo:
"""

s1 = "A" + "-" * 10 + "B"
print(s1)

"""
Exercicio: Imprima na tela uma variável do tipo string que escreva a seguinte frase abaixo. Crie a string concatenando tudo em uma só linha de código.
Linguagens de programação:

Python ----- C ----- Java ----- PHP
Para dar uma quebra de linha (enter) utilize \n. Para fazer uma tabulação (tab), utilize \t. Não esqueça de usar também o multiplicador de strings.
"""

s1 = "Python " + "-" * 5 + " C " + "-" * 5 + " Java " + "-" * 5 + " PHP"
print(s1)

s1 = s1 = "Linguagens de Programação:\n"+"\t Python " + "-" * 5 + " C " + "-" * 5 + " Java " + "-" * 5 + " PHP"

"""
Lembrando que em Python, realizar a concatenação entre variáveis numericas não é permitido. Para isso, utilize alguma composição,
que é o que verei no próximo arquivo py...
"""
