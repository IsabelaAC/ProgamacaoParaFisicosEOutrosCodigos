import random

def jogar() :
    numero_secreto = random.randrange(1,51)
    total_tentativas = 3
    rodada= 1
    pontos= 1000

    print("Qual a dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível de dificuldade:"))

    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas == 6
    else:
        total_tentativas == 3



    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite um número entre 1 e 50:")
        print("*******************************************")
        tentativa = int(chute)


        if(tentativa < 1 or tentativa > 50):
            print("Você deve digitar um número entre 1 e 50!")
            print("*******************************************")

            continue

        print("Você digitou" , chute)
        print("*******************************************")


        acerto= tentativa == numero_secreto
        maior = tentativa > numero_secreto
        menor = tentativa < numero_secreto

        if(acerto):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
             print("Você errou! O seu chute foi maior que o número secreto!")
             print("*******************************************")

            elif(menor):
             print("Você errou! O seu chute foi menor que o número secreto!")
             print("*******************************************")
            pontos_perdidos = abs(numero_secreto - tentativa)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

        if (rodada == total_tentativas + 1):
            print("O número era {}".format(numero_secreto) )


    print("*******************************************")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()