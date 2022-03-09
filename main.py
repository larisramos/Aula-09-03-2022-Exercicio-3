'''Escrever um programa em Python para ler um número inteiro e informar se ele é divisível por 5'''

n1 = int(input('Digite o valor para a divisão por 5: \n'))
div = n1 % 5
if div == 0:
  print ('O número {} é divisivel por 5!'.format(n1))
else:
  print ('O número {} NÃO é divisivel por 5'.format(n1))
