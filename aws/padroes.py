# Grupos

duzia1st12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

duzia2nd12 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

duzia3nd12 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]


coluna1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

coluna2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

coluna3 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]




                


red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]


quadrante1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

quadrante2 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

meio1 = [5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

meio2 = [10, 23, 8, 30, 11, 36, 13, 27, 6, 34, 17, 25, 2, 21, 4, 19, 15, 32]



def testing12(bets12, sequencia):
    validationArray = []

    for group in bets12:
        all_numbers_present = all(num in group for num in sequencia)
        validationArray.append(all_numbers_present)
    return validationArray

def testing13(bets13, sequencia):
    validationArray = []

    for group in bets13:
        all_numbers_present = all(num in group for num in sequencia)
        validationArray.append(all_numbers_present)
    return validationArray

bets13 = [duzia1st12, duzia2nd12, duzia3nd12, coluna1, coluna2, coluna3]

bets12 = [red, black, odd, even, quadrante1,quadrante2, meio1, meio2]

label13 = ['1ª Duzia', '2ª Duzia', '3ª Duzia', '1ª Coluna', '2ª Coluna', '3ª Coluna']

label12 = ['Vermelho', 'Preto', 'Impar(Odd)', 'Par(Even)', 'Baixos(1-18)', 'Altos(19-36)', 'Direita do 0', 'Esquerda do 0']





# # Criar um dicionário que associe os rótulos às validações
# relacao_label_validacao13 = dict(zip(label13, validationArray1))
# relacao_label_validacao12 = dict(zip(label12, validationArray2))

# # Exibir a relação para label13
# print("Relação para label13:")
# for label, validacao in relacao_label_validacao13.items():
#     print(f"{label}: {validacao}")

# # Exibir a relação para label12
# print("\nRelação para label12:")
# for label, validacao in relacao_label_validacao12.items():
#     print(f"{label}: {validacao}")

    