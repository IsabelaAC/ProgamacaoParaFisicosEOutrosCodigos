#
import random

#
chute = 0
chances = 7
tentativas = 1
jogador = ''
#
numero_secreto = random.randint(1, 100)
#
print('Bem vindo ao jogo de adivinhe o número!')
#
print('Você terá duas tentativas para acertar o número')
#
print(input('Me diga o seu nome:'))
#
#print(input('Qual o seu palpite'))
#
while tentativas <= 7:
    chute = int(input('Qual o seu palpite?'))
    if chute < numero_secreto:
        print('Voce errou, seu número é menor que o sorteado')
        print('Tentativa %d de %d' % (tentativas, chances))
    elif chute == numero_secreto:
        print('Parabéns!')
        print('Você acertou com %d tentativas' % tentativas)
        tentativas = 7
    else:
        print('Você errou, seu número é maior que o sorteado',)
    #
        print('Tentativa %d de %d' % (tentativas, chances))

    #
    if tentativas == 6:
        print('Ultima tentativa')
    elif tentativas == 7:
        print('Fim de jogo')
        print('O número sorteado era:', numero_secreto)

 #
    tentativas = tentativas + 1


