# imports
import sys, exercise2, exercise3, exercise4, exercise5, main, re, random
from easygui import *


#Main Menu
def menu_exercise_1():
    while True:
        option = buttonbox("A. Insert a sequence manually\n\nB. Generate a sequence with the letters: A, C, T, G\n\n"
                           "C. Show the total number of elements in sequence\n\n"
                           "D. Show the number of occurrences of a letter/sub-sequence and a list with the indexes\n\n"
                           "E. Show the frequence of a certain set of letters/sub-sequences (total and relative(%) number of each letter\n\n"
                           "F. Complementary sequence ('A' and 'T' change, and also 'G' and 'C'", "Menu Exercise 1",
                           choices=["A", "B", "C", "D", "E", "F", "Go back", "Exit"])
        if option == "A": exercise_1a()
        if option == "B": exercise_1b()
        if option == "C": exercise_1c()
        if option == "D": exercise_1d_1e_1f(indexes_sequence_1d)
        if option == "E": exercise_1d_1e_1f(freq_seq)
        if option == "F": exercise_1d_1e_1f(complementary)
        if option == "Go back": main.main_menu()
        if option == "Exit": sys.exit()


#Exercise 1a
def exercise_1a():
    global seq_manual
    seq_manual = (enterbox(msg="Input a sequence with the letters: A , C , T , G.").upper())                            #asks for sequence
    if not re.match("^[A, C,T,G]*$", seq_manual):                                                                       #if sequence contains letters that are not A,C,T or G, it gives error
        msgbox("Input only the letters: A , C , T , G.","ERROR","Ok")                                                   #Limpa o ecrã
        exercise_1a()                                                                                                  #Volta a pedir ao utilizador, até que coloque corretamente
    else: return seq_manual


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
    opcao = buttonbox("Qual opção deseja?\n\n1: Input sequence\n\n2: Analize from the manual sequence\n\n"
                      "3: Analize from the random sequence","Sequência para analisar",
                      choices=["1", "2", "3", "Go back"])
    if opcao == "1":
        exercise_1a()
        msgbox("Your sequence {} as a size of {} letters".format(seq_manual, len(seq_manual)),
               "Total number of letters in sequence", "Ok")

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

    if opcao == "Go back": menu_exercise_1()



#Exercise 1d_1e_1f:
def exercise_1d_1e_1f(exercise_resolution):
    option = buttonbox("1: Input sequence\n\n2: Analize from the manual sequence\n\n"
                      "3: Analize from the random sequence", "Sequence to analyze",
                      choices=["1", "2", "3", "Go back"])  # em cada opção, vai para a função freq_seq

    if option == "1":
        exercise_1a()
        exercise_resolution(seq_manual)

    if option == "2":
        try:
            exercise_resolution(seq_manual)
        except NameError:
            answer = buttonbox("If you want to input a manual sequence to finish the exercise, choose option 1.\n If"
                               "not, choose option to go back.", "Error! No sequence saved", choices=["1", "Go back"])
            if answer == "1":
                exercise_1a()
                exercise_resolution(seq_manual)
            if answer == "Go back": exercise_1d_1e_1f(exercise_resolution)

    if option == "3":
        try:
            exercise_resolution(random_seq)
        except NameError:
            answer = buttonbox("If you want to input a random sequence to finish the exercise, choose option 1.\n If"
                               "not, choose option to go back.", "Error! No sequence saved", choices=["1", "Go back"])
            if answer == "1":
                exercise_1b()
                exercise_resolution(random_seq)
            if answer == "Go back": exercise_1d_1e_1f(exercise_resolution)

    if option == "Go back": menu_exercise_1()


#Complementary functions to use on the exercises above.

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



def freq_seq(sequence):
    letter = enterbox("Input the letter you want to analyze from the sequence {}".format(sequence),"Frequence of the"
                      "the letter in sequence").upper()
    absolute_freq = int(sequence.count(letter.upper()))                                                                 #A frq.absoluta é contar quando a letra apareçe
    relative_freq = (absolute_freq / len(sequence)) * 100                                                               #A freq relativa é o numero de freq.absoluta, dividimos pelo total de letras, e multiplicamos por 100 para ter percentagem
    msgbox("Na sequência {} , a letra/sequência {} tem frequência absoluta {} vezes e frequência relativa {} "
           "%".format(sequence, letter, absolute_freq , relative_freq))


def complementary(seq):
    global B
    comp_seq = seq.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    upper_comp_seq = comp_seq.upper()
    msgbox("The complementary sequence is {} \n This is the complementary sequence of the "
           "sequence {}".format(upper_comp_seq,seq))
