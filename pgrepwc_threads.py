import re
import argparse,sys,os
from threading import Thread

def lerFicheiro(fileName): 
    with open(fileName, 'r', encoding='utf-8') as fileRead:
        return list(filter(lambda x: x!="",fileRead.read().splitlines()))

def get_dict(palavras):
    dictPalavras = dict()
    for word in palavras:
        dictPalavras[word] = 0
    return dictPalavras

def optionA(ficheiro,palavras,enable=False):

    fileRead = lerFicheiro(ficheiro)
    searchResult = list()

    for linha_ficheiro in fileRead:
        containTrue = list()
        for palavra in palavras:
            word = palavra.lower()
            if bool(re.findall(rf'\b{word}\b',linha_ficheiro.lower())) == True:
                containTrue.append(True)
        if enable == False and len(containTrue) == 1:
            searchResult.append(linha_ficheiro)
        
        elif enable == True and len(containTrue) == len(palavras):
            searchResult.append(linha_ficheiro)
    return searchResult
    

def optionC(ficheiro,palavras):

    fileRead = lerFicheiro(ficheiro)
    dictPalavras = get_dict(palavras)

    for linha_ficheiro in fileRead:
        for word in palavras:
            palavra = word.lower()
            if bool(re.findall(rf'\b{palavra}\b',linha_ficheiro.lower())) == True:
                dictPalavras[word] += len(re.findall(rf'\b{palavra}\b',linha_ficheiro.lower()))

    return dictPalavras

def optionL(searchResult,palavras, aOptionEnable = False):

    if aOptionEnable == True:
        return len(searchResult)
    else:
        dictPalavras = get_dict(palavras)
        for linha in searchResult:
            for word in palavras:
                palavra = word.lower()
                if bool(re.findall(rf'\b{palavra}\b',linha.lower())) == True:
                    dictPalavras[word] += 1

    return dictPalavras

def pgrepwc(a,c,l,p,palavras,ficheiros):

    
    for ficheiro in ficheiros:
        searchResult = optionA(ficheiro,palavras,a)
        formatA = 30*'-' + '--> O RESULTADO DA PESQUISA COM A FLAG -a ' + str(a)+ ' <--' + 30*'-'
        
        if c == True:
            dictPalavrasC = optionC(ficheiro,palavras)
            flag = 50*'-' + 'CASO DA FLAG C ATIVA' + 50*'-'
            formatC = 30*'-' + '--> O NÚMERO DE OCORRÊNCIAS ENCONTRADAS NO FICHEIRO <--' + 30*'-'
            imprime(ficheiro,flag,searchResult,formatA,dictPalavrasC,formatC,c,l)
            atualiza(dictPalavrasC,palavras)

        if l == True:
            dictPalavrasL = optionL(searchResult,palavras, a)
            flag = 50*'-' + 'CASO DA FLAG L ATIVA' + 50*'-'
            formatL = 30*'-' + '--> O NÚMERO DE LINHAS DA PESQUISA DA OPÇÃO -a COM A Flag -a ' + str(a)+ ' <--' + 30*'-'
            imprime(ficheiro,flag,searchResult,formatA,dictPalavrasL,formatL,c,l)
            atualiza(dictPalavrasL,palavras)
        print()
    
        

def imprime(ficheiro,flag,contentA,formatA,contentOPtion,formatOPtion,c,l):

    print(55*'-' + 'INIT: ' +  ficheiro.upper() + 55*'-')
    print()
    print(flag)
    print()

    contador = 1
    if type(contentA) == list:
        print(formatA)
        for l in contentA:
            
            print(str(contador) + '-' + l)
            contador+=1
            print()
            
        if len(contentA) == 0:
            print('->> Não encontrou palavras')
            
    if type(contentOPtion) == dict:
        print(formatOPtion)
        for chave in contentOPtion:
            if c == True:
                print('->> A palavra ' + str(chave) + ' tem ' + str(contentOPtion[chave]) + ' ocorrências')
            else:
                print('->> A palavra ' + str(chave) + ' está em ' + str(contentOPtion[chave]) + ' linhas')

    if type(contentOPtion) == int:
        print(formatOPtion)
        print('->> O número de linhas devolvido é: ' + str(contentOPtion))


def atualiza(contentOption,palavras):

    global myArray
    global myValue

    if type(contentOption) == dict:

        for i in range(len(palavras)):


            myArray[i] += contentOption[palavras[i]]
    else:
        print(myValue)
        myValue += contentOption


def divisionTasks(ficheiros,n):

    if n > len(ficheiros):
        argument.p = len(ficheiros)

    nficheiros,index = len(ficheiros),0

    indexList,taskDivisionList = list(),list()

    for i in range(nficheiros):

        if len(indexList) < n:
            indexList.append(1)
        else:
            indexList[index] = indexList[index]+1
            index +=1
            if index == n:
                index = 0

    inicio,fim  = 0,indexList[0]
    
    for i in indexList[1:]:

        taskDivisionList.append(ficheiros[inicio:fim])

        inicio = fim
        fim += i
        
    taskDivisionList.append(ficheiros[inicio:fim])
        
        
    return taskDivisionList 


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-a', required=False, action='store_true', help=' Define se o resultado da pesquisa, caso ativo: são as linhas de texto que \
                                                        contêm unicamente uma das palavras, caso inativo: todas as palavras ')

    parser.add_argument('-c', required=False, action='store_true', help='Opção que permite obter o número de ocorrências \
                                                    encontradas das palavras a pesquisar')
                                                    
    parser.add_argument('-l', required=False, action='store_true', help= 'Opção que permite obter o número de linhas devolvidas da pesquisa,a. \
                                                        Caso a opção -a não esteja ativa, o número de linhas devolvido é por palavra')
    
    parser.add_argument('-p', required=False, default=1, type=int, help='opção que permite definir o nível de paralelização, número de processos \
                                                                        (filhos)/threads que são utilizados para efetuar as pesquisas e contagens')
    
    parser.add_argument('palavras', nargs='+',help='Palavras a procurar' )

    parser.add_argument('-f',required=True, nargs='*', help='Ficheiros a serem lidos')

    argument = parser.parse_args()

    lista = sys.argv

    myArray = list()
    myValue = 0

    if len(argument.palavras) > 3:

        print('Não pode ser mais de 3 palavras')

    if len(argument.f) == 0:
        filesList = list()
        while len(filesList) == 0:
            print('Não colocou os ficheiros a vereficar. Quais os ficheiros que quer ler? ')
            filesList += input().split()
        argument.f = filesList

    if argument.c == True and argument.l == True: 
        print('Não é possivel usar a opção -c em conjunto com -l')
        exit()

    elif argument.c == False and argument.l == False:
        print('Opção -c ou -l tem de estar ativa')
        exit()
    
    else:

        for i in range(len(argument.palavras)):
            myArray.append(0)

        if argument.p > 0:
            getFileToProcess = divisionTasks(argument.f,argument.p)
            jobs = list()
            for i in range(argument.p):
                newT = Thread(target=pgrepwc, args=(argument.a,argument.c,argument.l,argument.p,argument.palavras,getFileToProcess[i]))

                newT.start()

                jobs.append(newT)


            for i in range(argument.p):
                jobs[i].join()

        
        else:
            for ficheiro in argument.f:
                pgrepwc(argument.a,argument.c,argument.l,argument.p,argument.palavras,[ficheiro])

    print('Resultado Final: ')
    print()

    if argument.a == True and argument.l == True:
        print('O número de linhas da pesquisa no total é: ' + str(myValue))
    else:
        
        for i in range(len(argument.palavras)):

            if argument.c == True:
                    print('A palavra ' + argument.palavras[i] + ' teve um número total de ocorrências igual a: ' + str(myArray[i]))

            else:
                    print('A palavra ' + argument.palavras[i] + ' teve um número total de linhas encontradas de acordo com a opção -a ' \
                          + str(argument.a) + ' igual a: ' + str(myArray[i]))