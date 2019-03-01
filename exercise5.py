# imports
import sys, exercise2, exercise3, exercise4, exercise1, main, re, random
from easygui import *
from matplotlib import pyplot as pp


def menu_exercise_5():
    Option = buttonbox("A. Mostrar num gráfico XY, a sequência de DNA (represente no eixo XX cada elemento da "
                       "sequência e no eixo YY o respetivo nucleótido representado por um número)\n"
                       "B. Mostrar uma figura com 4 gráficos do tipo histograma, para representar a distribuição "
                       "de cada nucleótido nas diferentes sequências.", "Menu Exercise 5",
                       choices=["A", "B", "C", "D", "E", "Go back", "Exit"])
    if Option == "A": exercise_1a()
    if Option == "B": exercise_1b()
    if Option == "Exit": sys.exit()



# ---------------------------------------------------
    # Exercicio 4.A: Carregar Ficheiro
# Geral (escolha do utilizador)
def exercicio_5a():                                                                                                     #funcao das opções como os anteriores
    answer = input("Qual pretende usar?\n1 - Introduzir Sequência\n2 - Sequência Manual do exercicio 1\n3 - Sequência aleatória\n"
                   "4 - Uma das sequências da lista do exercicio 2a.\n5 - Voltar atrás\nResposta: ")
    if answer == "1":
        exercise_1a()
        graph_5a(seq_manual)
    if answer == "2":
        try: graph_5a(seq_manual)
        except NameError:
            print("Não existe sequência guardada.\nSe quiser introduzir a sequência manual para concluir o exercicio, introduza '1'\n"
                  "Se quiser voltar atrás (ao exercicio 5.a), introduza '2'.")
            answer = input("Resposta: ")
            if answer == "1":
                exercise_1a()
                graph_5a(seq_manual)
            if answer == "2": exercicio_5a()
    if answer == "3":
        try: graph_5a(random_seq)
        except NameError:
            print("Não existe sequência guardada.\nSe quiser introduzir a sequência aleatória para concluir o exercicio, introduza '1'\n"
                  "Se quiser voltar atrás (ao exercicio 5.a), introduza '2'.")
            answer = input("Resposta: ")
            if answer == "1":
                exercise_1b()
                graph_5a(random_seq)
            if answer == "2": exercicio_5a()
    if answer == "4":
        try:
            print("A lista do exercicio 2a é: " + str(first_seq_list))
            position = int(input("Indique a posição da sequência que quer analisar: "))
            graph_5a(first_seq_list[position])
        except NameError:
            print(
                "Não existe sequência guardada.\nSe quiser introduzir a sequência aleatória para concluir o exercicio, introduza '1'\n"
                "Se quiser voltar atrás (ao exercicio 5.a), introduza '2'.")
            answer = input("Resposta: ")
            if answer == "1":
                exercise_2a()
                print("A lista do exercicio 2a é: " + str(first_seq_list))
                position1 = int(input("Indique a posição da sequência que quer analisar: "))
                graph_5a(first_seq_list[position1])
            if answer == "2": exercicio_5a()
    if answer == "5": main_menu()

# Função usada para concluir o exercicio
def graph_5a(sequencia):                                                                                                #link: https://stackoverflow.com/questions/26131822/how-to-display-all-label-values-in-matplotlib
    x = np.asarray(list(sequencia))
    nucleotid_number = sequencia.replace("A","1").replace("C","2").replace("G","3").replace("T","4")
    y = np.asarray(list(nucleotid_number))
    sns.set(style="darkgrid",context="talk")
    fig = pp.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(np.arange(len(x)), y, 'o')
    ax1.set_xticks(np.arange(len(x)))
    ax1.set_xticklabels(x)
    pp.xlabel("Sequência de DNA")
    pp.ylabel("Valores")
    pp.title("Nucleótido representado por um número ")
    pp.show()

# ---------------------------------------------------
    # Exercicio 4.B: Guardar sequencia/lista em ficheiro
# Geral (escolha do utilizador)
def exercicio_5b():
    seqs_5b()
    graphs_5b()

# Função usada para concluir o exercicio
def seqs_5b():                                                                                                          #se der, usa-se a sequencia. Se não der, pede-se para introduzir
    try: seq_manual
    except NameError: exercise_1a()
    try: random_seq
    except NameError: exercise_1b()
    try: file_variable
    except NameError: exercicio_4a()
    try: first_seq_list
    except NameError: exercise_2a()

def graphs_5b():
    print("A lista do exercicio 2a é: " + str(first_seq_list))
    position = int(input("Indique a posição da sequência que quer analisar: "))
    seq_lista_graph = first_seq_list[position-1]                                                                         #escolher sequencia da lista para usar

    fig = pp.figure()
    hist1 = pp.subplot(221)
    pp.hist(list(seq_manual), color="r")
    pp.xlabel("Nucleotidos")
    pp.ylabel("Frequência")
    pp.title("Sequência Manual")
    hist2 = pp.subplot(222)
    pp.hist(list(random_seq), color="c")
    pp.xlabel("Nucleotidos")
    pp.ylabel("Frequência")
    pp.title("Sequência Aleatória")
    hist3 = pp.subplot(223)
    pp.hist(list(file_variable), color="g")
    pp.xlabel("Nucleotidos")
    pp.ylabel("Frequência")
    pp.title("Sequência guardada num Ficheiro")
    hist4 = pp.subplot(224)
    pp.hist(list(seq_lista_graph), color="k")
    pp.xlabel("Nucleotidos")
    pp.ylabel("Frequência")
    pp.title("Sequência guardada numa Lista")

    pp.tight_layout()
    pp.show()