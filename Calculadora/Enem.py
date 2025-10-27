QuestaoTotal = 90

# Registro 
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')

print("RRRRR    EEEEE   GGGGG   III   SSSSS  TTTTT  RRRRR    OOOO")
print("R    R   E       G       I I  S         T    R    R  O    O")
print("RRRRR    EEEE    G  GGG  I I   SSS      T    RRRRR   O    O")
print("R   R    E       G    G  I I      S     T    R   R   O    O")
print("R    R   EEEEE    GGGG  III  SSSSS      T    R    R   OOOO")

print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
# Registro 

# Nome
while True:
    NomeDoAulo1 = input('Nome: ')
    if NomeDoAulo1.isalpha():
        break
    else:
        print("Digite apenas letras para o nome!")

# Sobrenome
while True:
    NomeDoAulo2 = input('Sobrenome: ')
    if NomeDoAulo2.isalpha():
        break
    else:
        print("Digite apenas letras para o sobrenome!")

# Idade

while True:
    try:
        Idade = float(input('Idade (0 a 100): '))
        if 0 <= Idade <= 100:
            break
        else:
            print("Digite uma idade entre 0 e 100!")
    except ValueError:
        print("Digite apenas números para a idade!")


# Colégio
while True:
    Colegio = input('Colégio: ')
    if Colegio.replace(" ", "").isalpha():  # permite espaços no nome da escola
        break
    else:
        print("Digite apenas letras para o colégio!")

# Série
while True:
    try:
        Serie = int(input('Digite a série (1, 2 ou 3): '))
        if Serie in (1, 2, 3):
            if Serie == 1:
                palavra = "Primeira vez aqui? (1 Série)"
            elif Serie == 2:
                palavra = "Falta um ano em safado! (2 Série) "
            else:
                palavra = " Vixi e seu utimo ano! JKSJKSSKKSKS. (3 Série)"
            print("Você escolheu:", palavra)
            break
        else:
            print("Digite 1, 2 ou 3!")
    except ValueError:
        print("Tu e burro animal! , digite um numero valido (1, 2 ou 3). ")

# Media

print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')

print("M   M   EEEEE   DDDD    I   AAAAA")
print("MM MM   E       D   D   I   A   A")
print("M M M   EEE     D   D   I   AAAAA")
print("M   M   E       D   D   I   A   A")
print("M   M   EEEEE   DDDD    I   A   A")

print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')

while True:
    try:
        Lin = float(input('Linguagens: '))
        if 0 <= Lin <= 1000: 
            break
        else:
            print('Digite um número entre 0 e 1000!')
    except ValueError:
        print('Digite um número válido! (0 a 1000)')

print('')
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('Linguagens =', Lin)
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('')

while True:
    try:
        Mat = float(input('Matematica: '))
        if 0 <= Mat <= 1000: 
            break
        else:
            print('Digite um número entre 0 e 1000!')
    except ValueError:
        print('Digite um número válido! (0 a 1000)')

print('')
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('Linguagens =', Lin)
print('Matematica = ' , Mat)
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('')


while True:
    try:
        Nat = float(input('Natureza: '))
        if 0 <= Nat <= 1000:  
            break
        else:
            print('Digite um número entre 0 e 1000!')
    except ValueError:
        print('Digite um número válido! (0 a 1000)')

print('')
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('Linguagens = ' , Lin)
print('Matematica = ' , Mat)
print('Natureza = ' , Nat)
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('')

while True:
    try:
        Hum = float(input('Humanas: '))
        if 0 <= Hum <= 1000:  
            break
        else:
            print('Digite um número entre 0 e 1000!')
    except ValueError:
        print('Digite um número válido! (0 a 1000)')

print('')
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('Linguagens = ' , Lin)
print('Matematica = ' , Mat)
print('Natureza = ' , Nat)
print('Humanas = ' , Hum)
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('')

while True:
    try:
        Red = float(input('Redação: '))
        if 0 <= Red <= 1000:  
            break
        else:
            print('Digite um número entre 0 e 1000!')
    except ValueError:
        print('Digite um número válido! (0 a 1000)')

print('')
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('Linguagens = ' , Lin)
print('Matematica = ' , Mat)
print('Natureza = ' , Nat)
print('Humanas = ' , Hum)
print('Redação = ' , Red )
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('')

media = (Lin + Mat + Nat + Hum + Red ) / 5

# Media

# Porcentagem

print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')

print("PPPP   OOO   RRRR   CCCC  EEEEE N   N  TTTTT  AAAAA GGGG  EEEEE  M    M")
print("P   P O   O  R   R C     E      NN  N    T    A   A G     E      MM  MM")
print("PPPP  O   O  RRRR  C     EEE    N N N    T    AAAAA G  GG EEE    M M  M")
print("P     O   O  R  R  C     E      N  NN    T    A   A G   G E      M    M")
print("P      OOO   R   R  CCCC EEEEE  N   N    T    A   A  GGG  EEEEE  M    M")

print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')

while True:
    try:
        feitas1 = float(input('Quantas questões você acertou na primeira prova (0 a 90): '))
        if 0 <= feitas1 <= QuestaoTotal:
            break  # valor válido, sai do loop
        else:
            print(f'Digite um número entre 0 e {QuestaoTotal}!')
    except ValueError:
        print('Digite um número válido!')

porcentagem1 = (feitas1 / QuestaoTotal) * 100

while True:
    try:
        feitas2 = float(input('Quantas questões você acertou na primeira prova (0 a 90): '))
        if 0 <= feitas1 <= QuestaoTotal:
            break  # valor válido, sai do loop
        else:
            print(f'Digite um número entre 0 e {QuestaoTotal}!')
    except ValueError:
        print('Digite um número válido!')

porcentagem2 = (feitas2 / QuestaoTotal) * 100

# Porcentagem

# Final
print('')
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('')

print('Nome: ' , NomeDoAulo1)
print('Sobre Nome: ' , NomeDoAulo2)
print('Idade: ' , Idade)
print('Colegio: ' , Colegio)
print('Série: ' , Serie)

print('')
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('')

print('Linguagens = ' , Lin)
print('Matematica = ' , Mat)
print('Natureza = ' , Nat)
print('Humanas = ' , Hum)
print('Redação = ' , Red )
print('')
print('Media Final: ' , media)
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')

print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print("Prova - 1 ; Porcentagem de gestão feita:", porcentagem1 , "%")
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')

print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print("Prova - 2 ; Porcentagem de gestão feita:", porcentagem2 , "%")
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')

print('')
print('──┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈────┈┈┈┄┄╌╌╌╌┄┄┈┈┈──')
print('')


# Final