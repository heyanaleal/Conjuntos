from colorama import Fore, Back, Style

loop=True

# INDICE #

while loop==True:
    indice=input(Fore.LIGHTBLUE_EX + '\nÍndice conjuntos' + Style.RESET_ALL + '\n1. Diferença \n2. Diferença simétrica\n3. União\n4. Intersecção\n5. Pertinência\n6. Subconjunto\n' + Fore.RED + 'Digite o número referente a operação desejada:\n')

#Filtro de erro indice#
    if indice != '1' and indice != '2' and indice != '3' and indice != '4' \
        and indice != '5' and indice != '6':
        print(Fore.RED + 'ERRO! Não foi digitado um número correto =(')

    if indice == '1':
            print(Fore.CYAN + '---Diferença entre conjuntos---')
            print(Fore.RED + 'Use o  colchetes e a vírgula para inserir - ex:[1,2,3,4]')
            a = input(Style.RESET_ALL+"Digite o 1º conjunto desejado:")
            conjuntoa = set(a)
            b = input("Digite o 2º conjunto desejado:")
            conjuntob = set(b)
            diferençaa = set(conjuntoa.difference(conjuntob))
            diferançab= set(conjuntob.difference(conjuntoa))
            if conjuntoa.difference(conjuntob):
                print( "A diferença  do 1º conjunto para o 2º conjunto é: {}".format(diferençaa))
            else:
                print("Não há diferença do 1º conjunto para o 2º conjunto")

            if conjuntob.difference(conjuntoa):
                    print( "A difereça  do 2º conjunto  para o 1º conjunto é: {}".format(diferançab))
            else:
                    print("Não há diferença do 2º conjunto  para o 1º conjunto ")

    if indice == '2':
        print(Fore.LIGHTGREEN_EX + '---Diferença simétrica entre os conjuntos---')
        print(Fore.RED+'Use o  colchetes e a vírgula para inserir - ex:[1,2,3,4]')
        a = input(Style.RESET_ALL+"Digite o 1º conjunto desejado:")
        conjuntoa = set(a)
        b = input("Digite o 2º conjunto desejado:")
        conjuntob = set(b)
        diferença =(conjuntoa.symmetric_difference(conjuntob))
        if conjuntoa.symmetric_difference(conjuntob):
            print("A difereça simétrica entre os conjuntos é: {}".format(diferença))

    if indice =='3':
        def uniao(*arg):
            return list(set([j for i in arg for j in i]))
        print(Fore.MAGENTA+ '---União entre conjuntos---')
        print(Fore.RED + 'Use o  colchetes e a vírgula para inserir - ex:[1,2,3,4]')
        a = input(Style.RESET_ALL+"Digite o 1º conjunto desejado:")
        conjuntoa = set(a)
        b = input("Digite o 2º conjunto desejado:")
        conjuntob = set(b)
        print("A união dos conjuntos é{}".format(uniao(conjuntoa,conjuntob)).replace(",","-"))

    if indice =='4':
        print(Fore.YELLOW + '---Intersecção entre os conjuntos ---')
        print(Fore.RED + 'Use o  colchetes e a vírgula para inserir - ex:[1,2,3,4]')
        a = input(Style.RESET_ALL+"Digite o 1º conjunto desejado:")
        conjuntoa = set(a)
        b = input("Digite o 2º conjunto desejado:")
        conjuntob = set(b)
        intersecção=(conjuntoa).intersection(conjuntob)
        if set(conjuntoa).intersection(conjuntob):
            print("A intersecção dos conjuntos é {}".format(intersecção).replace(",","-"))
        else:
            print("Os conjuntos são disjuntos")

    if indice =='5':
        print(Fore.CYAN+ '---Pertinência---')
        print(Fore.RED + 'Use o  colchetes e a vírgula para inserir - ex:[1,2,3,4]')
        a = input(Style.RESET_ALL+"Digite o conjunto desejado:")
        conjuntoa = set(a)
        print(Fore.RED+'Digite o valor da pertinência sem os colchetes - ex:1 ')
        pertinencia = input(Style.RESET_ALL+"Digite o valor que deseja saber sua pertinencia:")
        if pertinencia in conjuntoa:
            print("{} Pertence ao conjunto".format(pertinencia))
        else:
            print('{} Não pertence ao conjunto'.format(pertinencia))

    if indice =='6':
        print(Fore.LIGHTMAGENTA_EX + '---Intersecção entre os conjuntos ---')
        print(Fore.RED + 'Use o  colchetes e a vírgula para inserir - ex:[1,2,3,4]')
        a = input(Style.RESET_ALL+"Digite o 1º conjunto desejado:")
        conjuntoa = set(a)
        b = input("Digite o 2º conjunto desejado:")
        conjuntob = set(b)
        if set(conjuntoa).issubset(conjuntob):
            print('O 1º conjunto é subconjunto do 2º conjunto')
        else:
            set(conjuntob).issubset(conjuntoa)
            print('O 2º conjunto é subconjunto do 1º conjunto')


    # LOOP DE NOVA PESQUISA COM FILTRO DE ERRO
    while True:
        voltar_indice = str(input(Fore.LIGHTBLACK_EX + 'Deseja realizar uma nova operação?(Sim/Não/)\n'))
        if voltar_indice != 's' and voltar_indice != 'sim' and voltar_indice != 'S' and voltar_indice != 'SIM' and voltar_indice != 'n' and voltar_indice != 'nao' and voltar_indice != 'não' and voltar_indice != 'N' and voltar_indice != 'NAO' and voltar_indice != 'NÃO':
            continue
        elif voltar_indice == 's' or voltar_indice == 'sim' or voltar_indice == 'S' or voltar_indice == 'SIM':
            break
        else:
            loop = False
            break
        continue