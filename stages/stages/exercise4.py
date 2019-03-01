# imports
import sys, exercise2, exercise3, exercise1, exercise5, main, re, random, os
from easygui import *
from os import system


def menu_exercise_4():
    Option = buttonbox("A. Carregar as sequências guardadas num ficheiro\n"
                       "B. Guardar uma sequência ou lista de sequências num ficheiro", "Menu Exercise 4",
                       choices=["A", "B", "C", "D", "E", "Go back", "Exit"])
    if Option == "A": exercise_1a()
    if Option == "B": exercise_1b()
    if Option == "Exit": sys.exit()




def exercicio_4a():
    global file_variable
    path = input("Introduza o link do caminho para o ficheiro: ")
    file = open(path,"r")                                                                                               #abrir o ficheiro que a pesssoa introduz o caminho e faz o "read", e faz o print do que está lá dentro
    file_variable = file.read()
    print(file_variable)


def exercicio_4b():
    print("O que pretende guardar?\n1-Sequência guardada do exercicio 1\n2-Sequência aleatória\n3-Lista guardada anteriormente\n"
          "4-Lista depois de remover um elemento\n5-Nova sequência\n6-Nova lista\n7-Voltar ao menu anterior\n8/Voltar ao menu inicial")
    answer = input("Escolha a opção: ")
    if answer == "1": ex_4b_sequencias(seq_manual,exercise_1a())
    if answer == "2": ex_4b_sequencias(random_seq,exercise_1b())                                                       #esta função é a das escolhas ,e dependendo das escolhas, usar a sequencia/lista da função
    if answer == "3": ex_4b_sequencias(first_seq_list,exercise_2a())
    if answer == "4": ex_4b_sequencias(LIST_REMOVAL,exercicio_2b())
    if answer == "5":
        seq = input("Coloque a sequência pretendida: ")
        ex_4b_insert(seq)
    if answer == "6":
        exercise_2a()
        ex_4b_insert(first_seq_list)
    if answer == "7": menu_exercise_4()
    if answer == "8": main_menu()




# Função usada para concluir o exercicio
def ex_4b_sequencias(seq_lista , exercicio):
    try: ex_4b_insert(seq_lista)
    except NameError:
        print("A sua opção não contém nenhum elemento. O que quer fazer?\n1-Inserir\n2-Voltar atrás\n3-Voltar ao menu principal\ns-Sair")
        opcao = input("Esolha a sua opção: ")
        if opcao == "1": exercicio
        if opcao == "": exercicio_4b()                                                                                  #teoricamente, se funcionar, vai para função insert com a sequencia que se quer
        if opcao == "3": main_menu()
        if opcao == "4": sys.exit()




def ex_4b_insert(seq_add_file):
    path = input("Introduza o link do caminho onde deseja guardar o ficheiro: ")
    file_name = input("Introduza o nome que deseja para o ficheiro: ")
    path_file = os.path.join(path, file_name + ".txt")                                                                  #escolher o caminho, o nome do ficheiro e juntar tudo para criar ficheiro
    file1 = open(path_file, "w")
    try: file1.write(seq_add_file)
    except NameError:
        print("Não tem nada guardado nesta opção. O menu vai voltar atrás.")
        exercicio_4b()
