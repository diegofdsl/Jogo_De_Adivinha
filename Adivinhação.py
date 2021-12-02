import random

numero_aleatorio=random.randint(0,10)
nome=input('Qual seu nome ')
print('Ola',nome,'.Tente adivinhar um número entre 0 e 10,você só tem 5 oportunidades')

for chances in range(0,6):
    print('Qual sua escolha')
    palpite=int(input())
    if palpite<numero_aleatorio:
        print('Tente um número maior')
    elif palpite>numero_aleatorio:
        print('Tente um número menor')
    else:
         break

if palpite==numero_aleatorio:
        print('Parabéns,você acertou')
else:
        print(nome,'o número que eu estava pensando era ',numero_aleatorio)
    
