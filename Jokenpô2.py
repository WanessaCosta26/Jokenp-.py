import random
from time import sleep
print('''
SUAS OPÇÕES 
[ 0 ] PEDRA
[ 1 ] Papel
[ 2 ] tesoura ''')
player1 = int(input('Escolha uma opção: '))
pedra = 0
papel = 1
tesoura = 2
erro = 3
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
computador = random.randint(0,2)
print(f'resposta do computador {computador}')
if player1 == pedra and computador == tesoura:
    print(f'player1 escolheu {player1} e o computador escolheu {computador}')
    print(f'player1 VENCEU!')
elif computador == pedra and player1 == tesoura:
    print(f'player1 escolheu {player1} e o computador escolheu {computador}')
    print('Computador VENCEU!')
elif computador == tesoura and player1 == papel:
    print(f'player1 escolheu {player1} e o computador escolheu {computador}')
    print(f'O Computador VENCEU!')
elif player1 == tesoura and computador == papel:
    print(f'player1 escolheu {player1} e o computador escolheu {computador}')
    print('player1 VENCEU!')
elif player1 == papel and computador == pedra:
    print(f'player1 escolheu {player1} e o computador escolheu {computador}')
    print('player1 VENCEU')
elif computador == papel and player1 == pedra:
    print(f'player1 escolheu {player1} e o computador escolheu {computador}')
    print('Computador VENCEU!')
elif computador == papel and player1 == papel:
    print('EMAPTE! tente novamente!')
elif computador == tesoura and player1 == tesoura:
    print('EMAPTE! tente novamente!')
elif computador == pedra and player1 == pedra:
    print('EMAPTE! tente novamente!')