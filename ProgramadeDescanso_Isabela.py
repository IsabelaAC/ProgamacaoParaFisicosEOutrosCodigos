'''
Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 40min
'''
import webbrowser
import time


intervalos = 2
contador = 0
print('O programa de controle de descanso foi ativado ')

while contador < intervalos:
    time.sleep(5)
    webbrowser.open('https://www.youtube.com/watch?v=52muHLn6n5k')
    print('Hora de dar uma pausa, já bebeu água?')
    contador = contador + 1
