print('Condicionais - Exemplo 1')
print('*-* Cálculo da Média *-*')

#entrada de dados
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
n_faltas = int(input('Faltas: '))

#processamento
media = (nota1+nota2)/2

#saida de dados
print(f'Média: {media : .1f}')

if media ==10:
    print('Parabéns!!!')

if media >= 6 and n_faltas <= 18:
    print('Aprovado!')
elif media >= 6 and n_faltas > 18:
    print('Reprovado por faltas')
elif media <6 and n_faltas <= 18:
    print('EXAME!!!')
    exame = float(input('Nota do Exame: '))
    media = (media + exame) /2
    if media >= 6:
        print(f'Aprovado pelo Exame! Sua nova média é: {media : .1f}')
    else:
        print('Reprovado')
else: 
    print('Reprovado!')