# imports
import sys, exercise2, exercise1, exercise4, exercise5, main, re, random
from easygui import *
from Bio import pairwise2
from Bio.pairwise2 import format_alignment


def menu_exercise_3():
    Option = buttonbox("A. apagar um elemento da sequência, substituindo-o por ‘-‘\n"
                       "B. adicionar um novo elemento ‘-‘ à sequência, numa determinada posição\n"
                       "C. Smostrar a distância de Hamming entre duas sequências com o mesmo comprimento\n"
                       "D. Mostrar o número de matches e mismatches entre duas sequências\n"
                       "E. Alinhar duas sequências e guardar numa lista de sequencias alinhadas", "Menu Exercise 3",
                       choices=["A", "B", "C", "D", "E", "Go back", "Exit"])
    if Option == "A": exercise_1a()
    if Option == "B": exercise_1b()
    if Option == "Exit": sys.exit()




def exercicio_3a_3b():
    print("De onde quer obter uma sequência?\n1 - Inserir sequência\n2 - Usar sequência manual\n3 - Usar sequência aleatória\n"
          "4 - Usar uma sequência da lista\n5 - Voltar atrás")
    answer = input("Resposta: ")
    answer = buttonbox("De onde quer obter uma sequência?\n\n1 - Inserir sequência\n\n2 - Usar sequência manual\n\n"
                       "3 - Usar sequência aleatória\n\n4 - Usar uma sequência da lista", choices=["1", "2", "3", "4",
                                                                                                   "Go back"])
    if answer == "1":
        exercise_1a()
        exercicio_3a_replace(seq_manual)
    if answer == "2":
        try: exercicio_3a_replace(seq_manual)
        except NameError:
            msgbox("Não existe sequência guardada. Vai voltar atrás.")
            menu_exercise_3()
    if answer == "3":
        try: exercicio_3a_replace(random_seq)     #exercicio_3a_replace(random_seq)
        except NameError:
            msgbox("Não existe sequência guardada. Vai voltar atrás.")
            menu_exercise_3()
    if answer == "4":
        try: first_seq_list
        except NameError:
            msgbox("Não existe lista guardada. Vai voltar atrás.")
            menu_exercise_3()
        '''else:
            print("A lista é:\n" + str(first_seq_list))
            seq1 = int(input("Escolha uma sequência (coloque a posição da mesma): "))
            exercicio_3a_replace(first_seq_list[seq1-1])'''

    if answer == "Go back": menu_exercise_3()




def exercicio_3a_replace(sequencia_ex_3a):
    subseq_letter = enterbox("Which letter you want to replace?")
    seq_substituida = sequencia_ex_3a.replace(subseq_letter, "-")                                                       #usar a função replace para substituir a letra por um -
    msgbox("Now, your sequence is {}".format(seq_substituida))


def exercicio_3b_add(sequencia_ex_3b):
    indice = int(input("Em que posição pretende adicionar um ´-´?\nResposta: "))
    num = int(input("Quantos '-' deseja acrescentar? \nResposta: "))                                                    #escolher a posição onde colocar o - e depois pergunta-se quantos - se quer
    add_thing = "-" * num
    seq_added = sequencia_ex_3b[:indice - 1] + add_thing + sequencia_ex_3b[indice - 1:]                                 #escrever o que está antes da posição que se quer, depois adicionar os "-" e depois colocar o que estava a frente da posição
    print(seq_added)



def exercicio_3c():
    answer = input("De onde quer retirar as sequências?\n1 - Introduzir sequências\n2 - Usar da lista introduzida anteriormente\n3 - Voltar atrás\nResposta: ")
    if answer == "1":                                                                                                   #este menu tem as mesmas configurações que os outros, de ter várias opções
        seq1 = (input("Introduza uma sequência: ").upper())
        seq2 = (input("Introduza outra sequência DO MESMO TAMANHO: ").upper())
        exercicio_3c_hamming(seq1,seq2)
    if answer == "2":
        try:
            print("A lista é:\n" + str(first_seq_list))
            seq1 = int(input("Escolha uma sequência (coloque a posição da mesma): "))
            seq2 = int(input("Escolha outra sequência QUE SEJA DO MESMO TAMANHO DA SEQUÊNCIA ANTERIOR!!(coloque a posição da mesma): "))
            exercicio_3c_hamming(first_seq_list[seq1 - 1], first_seq_list[seq2 - 1])
        except NameError:
            print("Não existe lista guardada. Vai voltar atrás.")
            menu_exercise_3()
    if answer == "3": menu_exercise_3()



def exercicio_3c_hamming(seq1,seq2):                                                                                    #o hamming as sequencias necessitam de ter tamanho igual, pois se não der, dá erro
    if len(seq1) != len(seq2):
        print("As sequências não são de tamanhos iguais. Clique enter para voltar atrás.")
        system("pause")
        exercicio_3c()
    count = 0
    for i in range(0,len(seq1)):                                                                                        #sempre que a letra i de uma sequencia for diferente da letra i da outra sequencia, soma 1 ao count, e depois faz-se o print do count
        if seq1[i] != seq2[i]: count += 1
    print(count)




def exercicio_3d():
    answer = input(
        "De onde quer retirar as sequências?\n1 - Introduzir sequências\n2 - Usar da lista introduzida anteriormente\n3 - Voltar atrás\nResposta: ")
    if answer == "1":                                                                                                   #este menu tem as mesmas configurações que os outros, de ter várias opções
        seq1 = (input("Introduza uma sequência: ").upper())
        seq2 = (input("Introduza outra sequência: ").upper())
        exercicio_3d_match(seq1, seq2)
    if answer == "2":
        try:
            print("A lista é:\n" + str(first_seq_list))
            seq1 = int(input("Escolha uma sequência (coloque a posição da mesma): "))
            seq2 = int(input(
                "Escolha outra sequência: "))
            exercicio_3d_match(first_seq_list[seq1 - 1], first_seq_list[seq2 - 1])
        except NameError:
            print("Não existe lista guardada. Vai voltar atrás.")
            menu_exercise_3()
    if answer == "3": menu_exercise_3()

# Função usada para concluir o exercicio
def exercicio_3d_match(seq1,seq2):
    alignments = pairwise2.align.globalxx(seq1, seq2)                                                                   #usar 2 sequencias e usar o modulo que a professora deu
    for a in alignments: print(format_alignment(*a))



def exercicio_3e():
    answer = input(
        "De onde quer retirar as sequências?\n1 - Introduzir sequências\n2 - Usar da lista introduzida anteriormente\n3 - Voltar atrás\nResposta: ")
    if answer == "1":                                                                                                   #este menu tem as mesmas configurações que os outros, de ter várias opções
        seq1 = (input("Introduza uma sequência: ").upper())
        seq2 = (input("Introduza outra sequência: ").upper())
        exercicio_3e_alinhar(seq1, seq2)
    if answer == "2":
        try:
            print("A lista é:\n" + str(first_seq_list))
            seq1 = int(input("Escolha uma sequência (coloque a posição da mesma): "))
            seq2 = int(input(
                "Escolha outra sequência: "))
            exercicio_3e_alinhar(first_seq_list[seq1 - 1], first_seq_list[seq2 - 1])
        except NameError:
            print("Não existe lista guardada. Vai voltar atrás.")
            menu_exercise_3()
    if answer == "3": menu_exercise_3()

# Função usada para concluir o exercicio
def exercicio_3e_alinhar(seq1,seq2):
    alignments = pairwise2.align.globalxx(seq1, seq2)
    lista=[]                                                                                                            #usar o inicio da funçao de cima para os aligns.
    for i in range(len(alignments)):                                                                                    #como no de cima, são criadas varias listas dentro de 1 só, é escolhido a listai
        ali = alignments[i]                                                                                             #dentro dessa lista i , escolher o index 0 e 1 que são as sequencias, e junta-las numa lista
        lista.append(ali[0])
        lista.append(ali[1])
    final_list_alinhar = [lista[i:i+2] for i in range(0, len(lista), 2)]                                                #do tamanho da lista, escolher as 2 primeiras sequencias e junta-las numa lista. Fazer o mesmo de 2 em 2
    print("Existem {} hipóteses de alinhamento de sequências, e essas hipóteses são: ".format(len(final_list_alinhar)))
    for i in range(len(final_list_alinhar)): print("Lista {} :  {}".format(i+1,final_list_alinhar[i]))
