#coding:cp1252
# imports
import random
import sys  # sys.exit()
from time import sleep
import re
import os
from os import system
from matplotlib import pyplot as pp
import numpy as np
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import seaborn as sns
from easygui import *


#Functions

'''Main Menu'''
def main_menu():

    Option = buttonbox("1. Analize one sequence\n2. Analize several sequences\n 3. Align sequences"
                       "\n 4. Operation with files containing sequences\n 5. Visualize","Main Menu",
                       choices=["1", "2", "3", "4", "5", "Exit"])
    if Option == "1": menu_exercise_1()
    if Option == "2": print("ir po menu 1")
    if Option == "3": print("ir po menu 1")
    if Option == "4": print("ir po menu 1")
    if Option == "5": print("ir po menu 1")
    if Option == "Exit": sys.exit()

#-----------------------------------------------
'''Exercise 1'''
def menu_exercise_1():
    option = buttonbox("A. Insert a sequence manually\nB. Generate a sequence with the letters: A, C, T, G\n"
                    "C. Show the total number of elements in sequence\n"
                   "D. Show the number of occurrences of a letter/sub-sequence and a list with the indexes\n"
                    "E. Show the frequence of a certain set of letters/sub-sequences (total and relative(%) number of each letter\n"
                   "F. Complementary sequence ('A' and 'T' change, and also 'G' and 'C'","Menu Exercise 1",
                    choices=["A", "B", "C", "D", "E", "F", "Go back", "Exit"])
    if option == "A": exercise_1a()
    if option == "B": exercise_1b()
    if option == "F": exercise_1f()
    if option == "Exit": sys.exit()

def exercise_1a():
    global seq_manual
    seq_manual = (enterbox(msg="Input a sequence with the letters: A , C , T , G.").upper())                            #asks for sequence
    if not re.match("^[A, C,T,G]*$", seq_manual):                                                                       #if sequence contains letters that are not A,C,T or G, it gives error
        msgbox("Input only the letters: A , C , T , G.","ERROR","Ok")                                                   #Limpa o ecrã
        exercise_1a()                                                                                                  #Volta a pedir ao utilizador, até que coloque corretamente
    else: return seq_manual
    menu_exercise_1()

def exercise_1b():
    global random_seq
    length = (enterbox("Input a number for the size of the sequence: "))
    if not re.match("^[0,1,2,3,4,5,6,7,8,9]*$", length):                                                                #if sequence contains letters that are not A,C,T or G, it gives error
        msgbox("Input only numbers.","ERROR","Ok")
        exercise_1b()                                                                                                   #Volta a pedir ao utilizador, até que coloque corretamente
    else:
        letters = ["A", "C", "T", "G"]
        random_seq = ''.join([random.choice(letters) for i in range(int(length))])
        msgbox("Your random sequence with {} letters is {}".format(str(length),random_seq),"Random Sequence")
        return random_seq

def exercise_1c():
    opcao = buttonbox("1: Input sequence\n2: Analize from the manual sequence\n"
                   "3: Analize from the random sequence\n4: Go back\nQual opção deseja?","Sequência para analisar",
                      choices=["1", "2", "3", "4"])
    if opcao == "1":
        exercise_1a()
        msgbox("Your sequence {} as a size of {} letters".format(seq_manual, len(seq_manual)),
               "Total number of letters in sequence","Ok")

    if opcao == "2":
        try: msgbox("Your sequence {} as a size of {} letters".format(seq_manual, len(seq_manual)),"Total number of letters in sequence","Ok")
        except NameError:
            answer = buttonbox("1. Input manual sequence to finish the exercise\nIf not, click on 'Go back'",
                               "Error! No sequence found",choices=["1", "Go back"])
            if answer == "1":
                exercise_1a()
                msgbox("Your sequence {} as a size of {} letters".format(seq_manual, len(seq_manual)),
                       "Total number of letters in sequence", "Ok")
            if answer == "Go back":
                exercise_1c()

    if opcao == "3":
        try: msgbox("Your sequence {} as a size of {} letters".format(random_seq, len(random_seq)),"Total number of letters in sequence","Ok")
        except NameError:
            msgbox("There is no sequence.", "Error", "Go back")
            exercise_1c()

    if opcao == "4": menu_exercise_1()

def exercise_1d():                                                                                                      #Função para as opções
    opcao = buttonbox("1: Input sequence\n2: Analize from the manual sequence\n"
                      "3: Analize from the random sequence\n4: Go back", "Sequência para analisar",
                      choices=["1", "2", "3", "4"])
    if opcao == "1":
        exercise_1a()
        indexes_sequence_1d(seq_manual)

    if opcao == "2":
        try: indexes_sequence_1d(seq_manual)
        except NameError:
            answer = buttonbox("1. Input manual sequence to finish the exercise\nIf not, click on 'Go back'",
                               "Error! No sequence found", choices=["1", "Go back"])
            if answer == "1":
                exercise_1a()
                indexes_sequence_1d(seq_manual)
            if answer == "2":
                exercise_1d()

    if opcao == "3":
        try: indexes_sequence_1d(random_seq)
        except NameError:
            answer = buttonbox("1. Input random sequence to finish the exercise\nIf not, click on 'Go back'",
                               "Error! No sequence found",choices=["1", "Go back"])
            if answer == "1":
                exercise_1b()
                indexes_sequence_1d(random_seq)
            if answer == "Go back":
                exercise_1d()
                
    if opcao == "4": menu_exercise_1()

def indexes_sequence_1d(seq):
    letra = (enterbox("Input the letter you want to analyze from the sequence {}".format(seq),"Indexes of letter")).upper()
    '''print("Coloque a letra que deseja analisar da sequência {}".format(seq))
    letra = (input("Letra: ").upper())'''
    list_indexes_1d = []  # Lista vazia para os índices
    temp_index = 0  # index temporário para ser usado em baixo. Dado o valor 0 para iniciar
    for i in range(len(seq)):
        if i == seq.find(str(letra), temp_index):  # se i = indice em que a base escolhida, em cada posição
            list_indexes_1d.append(i)  # junta a lista o indice
            temp_index = i + 1  # temp_index soma i+1 para que a letra que já foi contada, nã0o seja necessaria
    list_plus = [x + 1 for x in
                  list_indexes_1d]  # LIST COMP: para cada x na lista_indice_1d, fazemos x+1 para que se obtenha as posições para o user
    msgbox("In the sequence {} , the letter {} occurs {} times\nOn the indexes: {} \nIn the following "
          "positions: {} \n".format(seq, letra.upper(), seq.count(letra.upper()), list_indexes_1d, list_plus))
    menu_exercise_1()


def exercise_1e():
    opcao = buttonbox("1: Input sequence\n2: Analize from the manual sequence\n"
                      "3: Analize from the random sequence\n4: Go back", "Sequence to analyze",
                      choices=["1", "2", "3", "4"])                                                                     #em cada opção, vai para a função freq_seq

    if opcao == "1":
        exercise_1a()
        freq_seq(seq_manual)

    if opcao == "2":
        try: freq_seq(seq_manual)
        except NameError:
            answer = buttonbox("If you want to input a manual sequence to finish the exercise, choose option 1.\n If"
                               "not, choose option to go back.","Error! No sequence saved",choices=["1", "Go back"])
            if answer == "1":
                exercise_1a()
                freq_seq(seq_manual)
            if answer == "Go back": exercise_1e()

    if opcao == "3":
        try: freq_seq(random_seq)
        except NameError:
            answer = buttonbox("If you want to input a random sequence to finish the exercise, choose option 1.\n If"
                               "not, choose option to go back.", "Error! No sequence saved", choices=["1", "Go back"])
            if answer == "1":
                exercise_1b()
                freq_seq(random_seq)
            if answer == "Go back": exercise_1e()

    if opcao == "4": menu_exercise_1()


def freq_seq(sequence):
    letter = enterbox("Input the letter you want to analyze from the sequence {}".format(sequence),"Frequence of the"
                      "the letter in sequence").upper()
    absolute_freq = int(sequence.count(letter.upper()))                                                                 #A frq.absoluta é contar quando a letra apareçe
    relative_freq = (absolute_freq / len(sequence)) * 100                                                               #A freq relativa é o numero de freq.absoluta, dividimos pelo total de letras, e multiplicamos por 100 para ter percentagem
    msgbox("Na sequência {} , a letra/sequência {} tem frequência absoluta {} vezes e frequência relativa {} "
           "%".format(sequence, letter, absolute_freq , relative_freq))
    menu_exercise_1()


def exercise_1f():
    opcao = buttonbox("1: Input sequence\n2: Analize from the manual sequence\n"
                      "3: Analize from the random sequence\n4: Go back", "Sequence to analyze",
                      choices=["1", "2", "3", "4"])  # em cada opção, vai para a função freq_seq

    if opcao == "1":
        exercise_1a()
        complementary(seq_manual)

    if opcao == "2":
        try:
            complementary(seq_manual)
        except NameError:
            answer = buttonbox("If you want to input a manual sequence to finish the exercise, choose option 1.\n If"
                               "not, choose option to go back.", "Error! No sequence saved", choices=["1", "Go back"])
            if answer == "1":
                exercise_1a()
                complementary(seq_manual)
            if answer == "Go back": exercise_1f()

    if opcao == "3":
        try:
            complementary(random_seq)
        except NameError:
            answer = buttonbox("If you want to input a random sequence to finish the exercise, choose option 1.\n If"
                               "not, choose option to go back.", "Error! No sequence saved", choices=["1", "Go back"])
            if answer == "1":
                exercise_1b()
                complementary(random_seq)
            if answer == "Go back": exercise_1f()

    if opcao == "4": menu_exercise_1()


def complementary(seq):
    global B
    comp_seq = seq.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    upper_comp_seq = comp_seq.upper()
    msgbox("The complementary sequence is {} \n This is the complementary sequence of the "
           "sequence {}".format(upper_comp_seq,seq))
    menu_exercise_1()



def menu_exercise_2():
    Option = buttonbox("A. Insert a sequence\nB. Remove a sequence\n"
                       "C. Show the number of occurrences of a letter/sub-sequence and a list with the indexes, in each sequence\n"
                       "D. Show the frequence of a certain set of letters/sub-sequences (total and relative(%) number of each letter, on each sequence\n"
                       "E. Complementary sequence ('A' and 'T' change, and also 'G' and 'C'", "Menu Exercise 1",
                       choices=["A", "B", "C", "D", "E", "Go back", "Exit"])
    if Option == "A": exercise_1a()
    if Option == "B": exercise_1b()
    if Option == "Exit": sys.exit()


def exercise_2a():
    global first_seq_list                                                                                               #Vai pedir quantas sequencias quer na lista
    number_sequences_list = int(enterbox("How many sequences you want to input on the list to begin?"))
    lista_inicial = []
    for i in range(number_sequences_list):                                                                              #o ciclo vai repetir as vezes que o user quer, e vai a funcao seq_list para analisar as sequencias, e juntar a lista
        seq_list()
        first_seq_list.append(seq_manual_list)
    print(first_seq_list)
    return first_seq_list

def seq_list():
    global seq_manual_list
    seq_manual_list = (input("Introduza uma sequência com as letras A, C, T, G.\nColoque aqui: ").upper())              #mesma função que o exercicio 1a, mas para ser usada no exercicio ea
    if not re.match("^[A, C,T,G]*$", seq_manual_list):  # se a sequência contiver letras diferentes de A,C,T,G
        # vai dar erro. "^" significa que é todos os que fizerem
        print("Erro! Só pode colocar as letras: A,C,T,G")  # match excepto os que estão lá dentro.
        sleep(3)
        system("cls")
        seq_list()
    else:
        return seq_manual_list


def exercicio_2b():
    try: remover(first_seq_list)
    except NameError:
        print("Não existe lista guardada.\nSe quiser introduzir a lista manual para concluir o exercicio, introduza '1'\n"
              "Se quiser voltar atrás (ao exercicio 1.e), introduza '2'.")
        answer = input("Resposta: ")
        if answer == "1":                                                                                               #Vai tentar ir ao menu remover() com a lista inicial
            exercise_2a()                                                                                          #Se não houver, existem 2 opçoes como anteriormente no menu 1
            remover(first_seq_list)
        if answer == "2": menu_exercise_2()


def remover(sequence):
    global LIST_REMOVAL
    print("A sua lista antes da remoção contém as seguintes sequências: " + str(sequence)[1:-1])                       #Escolhe a posição da sequencia
    remove_pos = (int(input(("Qual pretende remover? Introduza a posição em que se encontra:  ")))) - 1
    LIST_REMOVAL = sequence[:remove_pos] + sequence[remove_pos + 1:]                                                     #Lista_REMOVER fica tudo o que está atrás da posição e junta com o que está a frente
    print("Agora, a sua lista passou a ser " + str(LIST_REMOVAL)[1:-1])
    return LIST_REMOVAL


# ----------------------------------------------------
    # Exercicio 2.C: Indice e ocorrência de uma letra / sub-sequência
# Geral (escolha do utilizador)
def exercise_2c():                                                                                                     #É igual ao exercicio 1.d
    prints_escolha_exercicio2_opcao2()
    escolha = input("Qual a opção que deseja? ")
    if escolha == "1":
        exercise_2a()
        ocorr_indice_lista(first_seq_list)

    if escolha == "2":
        try: ocorr_indice_lista(first_seq_list)
        except NameError:
            print("Não existe lista manual guardada.\nSe quiser introduzir a lista manual para concluir o exercicio, introduza '1'\n"
                  "Se quiser voltar atrás (ao exercicio 1.e), introduza '2'.")
            answer = input("Resposta: ")
            if answer == "1":
                exercise_2a()
                ocorr_indice_lista(first_seq_list)
            if answer == "2": exercise_2c()

    if escolha == "3":
        try: ocorr_indice_lista(LIST_REMOVAL)
        except NameError:
            print("Não removeu nenhuma sequência.\nSe quiser introduzir a lista manual para concluir o exercicio, introduza '1'\n"
                  "Se quiser voltar atrás (ao exercicio 1.e), introduza '2'.")
            answer = input("Resposta: ")
            if answer == "1":
                exercicio_2b()
                ocorr_indice_lista(LIST_REMOVAL)
            if answer == "2": exercise_2c()

    if escolha == "4":  menu_exercise_2()

#Função usada para concluir o exercicio
def ocorr_indice_lista(lista):
    print("A sua lista é: \n {} \n ".format(lista))
    num = int(input("Escolha a posição da sequência que pretende analisar. Se pretender analisar a lista toda, pressione 0.\nEscolha: "))
    if num == 0:
        for i in range(len(lista)): indice_sequência_1d(lista[i])                                                       #ciclo que faz com que se analisa cada seq
    else: indice_sequência_1d(lista[num-1])                                                                               #analisar a seq que é pretendida pelo user




#Main program
if __name__ == '__main__':
    main_menu()
    print("Espero que tenha sido util.\n"
          "Realizado por:\nAndré Antunes nº2572\nGonçalo Fonseca nº2465\nMárcio Mota nº2602")