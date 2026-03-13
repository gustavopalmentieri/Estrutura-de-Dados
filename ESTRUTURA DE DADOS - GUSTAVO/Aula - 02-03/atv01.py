#CÁLCULO DO IMC

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metrôs: '))

imc = peso / (altura ** 2)

if imc < 19:

    print('Abaixo do peso')

elif imc >=  19 and imc < 26:

    print('Peso ideal')

else:

    print('Acima do peso')

