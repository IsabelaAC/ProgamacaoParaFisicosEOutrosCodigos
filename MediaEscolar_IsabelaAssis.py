#
print('Bem vindo ao sistema escolar' )
#
nome=input('Qual o seu nome? Digite por favor')
#
materia=input('Qual a disciplina?')
#
print('Digite as notas das atividades ')
#
nota01=float(input('Digite a sua nota'))
#
nota02=float(input('Digite a sua nota'))
#
nota03=float(input('Digite a sua nota'))
#
nota04=float(input('Digite a sua nota'))
# 
media=(nota01+nota02+nota03+nota04)/4
#
if media < 7:
    print('Aluno %s, você foi REPROVADA. Sua média em %s foi de %.2f.'
        % (nome, materia, media))
else:
    print('Parabéns!!!!')
    print('Aluno %s, você foi APROVADA. Sua média em %s foi %.2f.'
        % (nome, materia, media))


#Isabela Assis Cardoso
