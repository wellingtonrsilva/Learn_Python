# import random
# import os

# move_list = ['papel', 'pedra', 'tesoura']
# player_count = 0
# computer_count = 0

# print('====================')
# print('Bem vindo ao jogo Papel, Pedra e Tesoura')

# def main_print():
#     print('=================')
#     print('\nPLACAR:')
#     print('Voce: {}'.format(player_count))
#     print('Computador: {}'.format(computer_count))
#     print('\n')
#     print('Escolha seu lance:')
#     print('0 - Papel | 1 - Pedra | 2 - Tesoura')

# def select_move():
#     return random.choice(move_list)

# def get_player_move():
#     while True:
#         try:
#             player_move = int(input())
#             if player_move not in [0, 1, 2]:
#                 raise
#             return move_list[player_move]

#         except Exception as e:
#             print(e)

# def select_winner(p_move, c_move):
#     global player_count, computer_count
    
#     if p_move == 'papel':
#         if c_move == 'pedra':
#             player_count += 1
#             return 'p'
#         elif c_move == 'tesoura':
#             computer_count += 1
#             return 'c'
#         else:
#             return 'd'

#     if p_move == 'pedra':
#         if c_move == 'tesoura':
#             player_count += 1
#             return 'p'
#         elif c_move == 'papel':
#             computer_count += 1
#             return 'c'
#         else:
#             return 'd'

#     if p_move == 'tesoura':
#         if c_move == 'papel':
#             player_count += 1
#             return 'p'
#         elif c_move == 'pedra':
#             computer_count += 1
#             return 'c'
#         else:
#             return 'd'

# again = 1
# while again == 1:
#     main_print()
#     player_move = get_player_move()
#     computer_count = select_move()
#     winner = select_winner(player_move, computer_count)

#     print('')
#     print('=============')
#     print('Sua jogada: {}'.format(player_move.upper()))
#     print('jogada do computador: {}'.format(computer_move.upper()))

#     if winner == 'p':
#         print('Voce venceu!')
#     elif winner == 'c':
#         print('Voce perdeu!')
#     else:
#         print('Empate!')
#     print('=============')

#     while True:
#         print('Jogar novamente? 0 - SIM | 1 - NAO')
#         next = int(input())
#         if next == 0:
#             break
#         elif next == 1:
#             again = 0
#             break

#     os.system('cls')

# from _typeshed import Self


# class Dog:
#     def __init__(self):
#         self.idade = 10

# dog = Dog()

# print(dog.idade)

# class Animal:
#     def __init__(self):
#         print('Animal criado')
#     def quem_sou_eu(self):
#         print('Eu sou um animal.')
#     def comer(self):
#         print('Comendo')

# class Cachorro(Animal):
#     pass

# animal = Animal()

# print(animal)

# Exercicios_Treinamento

# print('Olá mundo!!!')

# n = int(input('Digite um numero: '))
# print('Obrigado!!')

# n1 = int(input('Digite o n1: '))
# n2 = int(input('Digite o n2: '))

# ntotal = n1 + n2

# print('Valor total de: ', ntotal)

print('Média Bimestre!')
print('================')

def teste():
    n1 = float(input('Digite n1: '))
    n2 = float(input('Digite n2: '))
    n3 = float(input('Digite n3: '))
    n4 = float(input('Digite n4: '))
    return(n1, n2, n3, n4)
    

def media ():
    n1, n2, n3, n4 = teste()
    return (n1 + n2 + n3 + n4)/4

print('Sua média é: ', media())


     

