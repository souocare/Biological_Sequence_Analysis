# imports
import sys, exercise1, exercise3, exercise4, exercise5, main, re, random
from easygui import *

def menu_exercise_2():
    Option = buttonbox("A. Insert a sequence\nB. Remove a sequence\n"
                       "C. Show the number of occurrences of a letter/sub-sequence and a list with the indexes, in each sequence\n"
                       "D. Show the frequence of a certain set of letters/sub-sequences (total and relative(%) number of each letter, on each sequence\n"
                       "E. Complementary sequence ('A' and 'T' change, and also 'G' and 'C'", "Menu Exercise 1",
                       choices=["A", "B", "C", "D", "E", "Go back", "Exit"])
    if Option == "A": exercise_2a()
    if Option == "B": exercicio_2b()
    if Option == "C": exercise_2c_2d_2e(indexes_sequence_list)
    if Option == "D": exercise_2c_2d_2e(freq_lista)
    if Option == "E": exercise_2c_2d_2e(complementary_seq_list)
    if Option == "Go back": exercise_1b()
    if Option == "Exit": sys.exit()


def exercise_2a():
    global first_seq_list                                                                                               #Vai pedir quantas sequencias quer na lista
    number_sequences_list = int(enterbox("How many sequences you want to input on the list to begin?"))
    first_seq_list = []
    for i in range(number_sequences_list):                                                                              #o ciclo vai repetir as vezes que o user quer, e vai a funcao seq_list para analisar as sequencias, e juntar a lista
        seq_list()
        first_seq_list.append(seq_manual_list)
    see_items = ynbox("Your list contains {} items. You want to see the items of your list?".format(len(first_seq_list)))
    if see_items == True:
        msgbox("Your list contains the items:\n\n{}".format('\n\n'.join(first_seq_list)))
    return first_seq_list


def seq_list():
    global seq_manual_list
    seq_manual_list = (input("Introduza uma sequência com as letras A, C, T, G.\nColoque aqui: ").upper())              #mesma função que o exercicio 1a, mas para ser usada no exercicio ea
    seq_manual_list = (enterbox(msg="Introduza uma sequência com as letras A, C, T, G.".upper()))
    if not re.match("^[A, C,T,G]*$", seq_manual_list):  # se a sequência contiver letras diferentes de A,C,T,G
        # vai dar erro. "^" significa que é todos os que fizerem
        msgbox(msg="Erro! Só pode colocar as letras: A, C, T, G.")
        sleep(3)
        system("cls")
        seq_list()
    else:
        return seq_manual_list



def exercicio_2b():
    try: remover(first_seq_list)
    except NameError:
        answer = ynbox("There's no saved sequence.\n"
                       "If you want to input a manual list to conclude the exercise, click 'Yes'\n"
                       "If not, it will go back")
        if answer:                                                                                              #Vai tentar ir ao menu remover() com a lista inicial
            exercise_2a()                                                                                          #Se não houver, existem 2 opçoes como anteriormente no menu 1
            remover(first_seq_list)
        else: menu_exercise_2()


def remover(sequence):
    global LIST_REMOVAL
    msgbox("Your list contains the items:\n\n{}".format('\n\n'.join(first_seq_list)))                                   #Escolhe a posição da sequencia
    #remove_pos = (int(input(("Qual pretende remover? Introduza a posição em que se encontra:  ")))) - 1
    #LIST_REMOVAL = sequence[:remove_pos] + sequence[remove_pos + 1:]                                                    #Lista_REMOVER fica tudo o que está atrás da posição e junta com o que está a frente
    LIST_REMOVAL = sequence.remove(choicebox("Choose the sequence you want to remove", "Remove sequence",sequence))
    #print("Agora, a sua lista passou a ser " + str(LIST_REMOVAL)[1:-1])
    msgbox("Now, your list contains the items:\n\n{}".format('\n\n'.join(first_seq_list)))
    return LIST_REMOVAL



def exercise_2c_2d_2e(exercise_resolution):                                                                             #É igual ao exercicio 1.d
    opcao = buttonbox(
        "1: Introduzir sequências (a uma lista)\n2: Analisar a partir da sequência manual (da lista) antes da remoção\n"
        "3: Analisar a partir da sequência manual (da lista) depois da remoção (se existir)\n4:Voltar atrás"
        , "Qual a sequência que deseja analisar?", choices=["1", "2", "3", "Go back"])
    if opcao == "1":
        exercise_2a()
        exercise_resolution(first_seq_list)

    if opcao == "2":
        try: exercise_resolution(first_seq_list)
        except NameError:
            answer = ynbox("Erro! Não existe lista manual guardada. \nClick 'Yes' if you want to continue the exercise,"
                               " to input a manual list.\nIf not, it will go back.", title="ERROR!")
            #print("Não existe lista manual guardada.\nSe quiser introduzir a lista manual para concluir o exercicio, introduza '1'\n"
                  #"Se quiser voltar atrás (ao exercicio 1.e), introduza '2'.")
            if answer:
                exercise_2a()
                exercise_resolution(first_seq_list)
            else: exercise_2c_2d_2e(exercise_resolution)

    if opcao == "3":
        try: exercise_resolution(LIST_REMOVAL)
        except NameError:
            #print("Não removeu nenhuma sequência.\nSe quiser introduzir a lista manual para concluir o exercicio, introduza '1'\n"
                  #"Se quiser voltar atrás (ao exercicio 1.e), introduza '2'.")
            answer = ynbox("Erro! Não removeu nenhuma sequência. \nClick 'Yes' if you want to continue the exercise, "
                           "to input  \nIf not, it will go back.", title="ERROR!")
            if answer:
                exercicio_2b()
                exercise_resolution(LIST_REMOVAL)
            else: exercise_2c_2d_2e(exercise_resolution)

    if opcao == "4":  menu_exercise_2()



def indexes_sequence_list(list):                                                                  #ANALISAR MELHOR ESTE QUE NAO ENTENDO BEM
    #print("A sua lista é: \n {} \n ".format(lista))
    answer = buttonbox(msg="Do you want to analyse only in one sequence, or all of them?",choices=["Only one", ["All of them"]])
    if answer == "All of them":
        for i in range(len(list)): indexes_sequence_1d(list[i])                                                       #ciclo que faz com que se analisa cada seq
    else:
        choice = integerbox("Please select the sequence you want to analyze:\n\n{}".format('\n\n'.join(list)))
        indexes_sequence_1d(list[choice-1])                                                                               #analisar a seq que é pretendida pelo user


def freq_lista(list):
    LISTA_FREQ = []
    '''num = int(input(
        "Escolha a posição da sequência que pretende analisar. Se pretender analisar a lista toda, pressione 0.\nEscolha: "))
    print("A sua lista é: \n {} \n ".format(lista))'''
    answer = buttonbox(msg="Do you want to analyse only in one sequence, or all of them?",
                       choices=["Only one", ["All of them"]])
    if answer == "All of them":
        for i in range(len(list)): LISTA_FREQ.append(freq_seq(list[i]))                                                 #acontece o mmesmo que a funcao anterior
    else:
        choice = integerbox("Please select the sequence you want to analyze:\n\n{}".format('\n\n'.join(list)))
        freq_seq(list[choice-1])


def complementary_seq_list(list):
    LISTA_COMP = []
    print("A sua lista é: \n {} \n ".format(list))
    num = int(input(
        "Escolha a posição da sequência que pretende analisar. Se pretender analisar a lista toda, pressione 0.\nEscolha: "))
    if num == 0:
        for i in range(len(list)): LISTA_COMP.append(complementary(list[i]))                                         #acontece o mesmo que a funcao anterior
    else:
        freq_seq(list[num])
