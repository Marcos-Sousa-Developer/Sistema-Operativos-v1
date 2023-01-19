<p align="center">
    <img src="https://e7.pngegg.com/pngimages/986/627/png-clipart-computer-icons-system-integration-others-miscellaneous-business-process.png" alt="Logo" width="80" height="80">
</p>

# <h1 align="center">Pesquisa as linhas dos ficheiros</h3>
<h4 align="center">Projeto para a cadeira de Sistemas Operativos (Parte1) (2021/2022)</h5>

<hr>

# Objetivo
Realização de um trabalho de programação em Python envolvendo a criação de processos/threads e a comunicação entre processos/threads.
O comando grep pesquisa as linhas dos ficheiros que contêm determinada palavra ou expressão regular. Uma dada palavra a procurar pode aparecer isolada dentro de uma linha (i.e., está separada das restantes palavras dentro dalinha de texto) ou fazer parte de outra palavra. Por exemplo, nas duas frases seguintes: “O Sistema Operativo utiliza o hardware” e “O Sistema Operativo satisfaz os pedidos do utilizador”; se procurarmos a palavra “utiliza”, o
comando grep devolve ambas as linhas. <br>
Este comando quando usado com várias palavras a pesquisar e com um conjunto alargado de ficheiros, apresenta alguns problemas de desempenho.
Com este trabalho pretende-se desenvolver o comando pgrepwc (parallel grep with counting), uma versão do grep com funcionalidades acrescidas e que funciona em paralelo. O comando irá emitir as linhas de texto que contêm as palavras isoladas a pesquisar, a contagem das linhas resultantes e o número de ocorrências das palavras a pesquisar.

<hr>

# Instruções  

* pgrepwc - pesquisa até um máximo de três palavras em um ou mais ficheiros, devolvendo as linhas de texto que contêm unicamente uma das palavras (isoladamente) ou todas as palavras. Também, conta o número de ocorrências encontradas de cada palavra e o número de linhas devolvidas de cada palavra ou de todas as palavras. A pesquisa e contagem são realizadas em paralelo, em vários ficheiros. 

* -a: opção que define se o resultado da pesquisa são as linhas de texto que contêm unicamente uma das palavras ou
todas as palavras. Por omissão (ou seja, se a opção não for usada), somente as linhas contendo unicamente uma das
palavras serão devolvidas.

* -c: opção que permite obter o número de ocorrências encontradas das palavras a pesquisar.

* -l: opção que permite obter o número de linhas devolvidas da pesquisa. Caso a opção -a não esteja ativa, o número
de linhas devolvido é por palavra.

* -p n: opção que permite definir o nível de paralelização n do comando (ou seja, o número de processos
(filhos)/threads que são utilizados para efetuar as pesquisas e contagens). Por omissão, deve ser utilizado apenas
um processo (o processo pai) para realizar as pesquisas e contagens.

* palavras: as palavras a pesquisar no conteúdo dos ficheiros. O número máximo de palavras a pesquisar é de 3.  

* -f ficheiros: podem ser dados um ou mais ficheiros, sobre os quais é efetuada a pesquisa e contagem. Caso
não sejam dados ficheiros na linha de comandos (ou seja, caso não seja passada a opção -f), estes devem ser lidos
de stdin (o comando no início da sua execução pedirá ao utilizador quem são os ficheiros a processar).

Inicialmente, após a validação das opções do comando, o processo pai deve criar os processos filhos/threads
definidos pelo nível de paralelização do comando (valor n). Estes processos/threads pesquisam as palavras nos
ficheiros, contam as ocorrências das palavras e o número de linhas onde estas foram encontradas nos ficheiros e
escrevem os resultados (linhas encontradas e contagens) para stdout. Os resultados das pesquisas e contagens são
escritos para stdout de forma não intercalada, ou seja, os resultados de cada processo/thread são apresentados
sequencialmente, sem serem intercalados com os resultados dos outros processos/threads. <br>

Os processos/threads realizam as pesquisas e as contagens nos ficheiros atribuídos pelo processo pai. Um dado
ficheiro é atribuído a um só processo/thread, não havendo assim divisão do conteúdo de um ficheiro por vários
processos/threads. Neste sentido, se o valor de n for superior ao número de ficheiros, o comando (o processo pai)
redefine-o automaticamente para o número de ficheiros. <br>

No final, o processo pai terá de escrever para stdout o número total de ocorrências das palavras ou de linhas
encontradas, de acordo com a opção especificada de contagem (c ou l).

#### **Run it on terminal or open the code (main.py) and test it** 
```bash
python3 pgrepwc [-a] [-c|-l] [-p n] {palavras} [-f ficheiros]
```

