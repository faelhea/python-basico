#!/usr/bin/python3

"""
Resumo:

Script para realizar a busca por diretorios vazios, cheio ou inexiste.
O script buscar um arquivo CSV dentro do diretorio especificado, esse arquivo
conte o resultado de uma query feita no banco de dados e escreve o resultado
em um arquivo texto.

Configuração:

#Session1
Nesse campo preciso informar o local e nome da query exportada, para iniciar a busca.

#Session2
Nesse campo e local aonde ele vai gravar a saida do script com o resultado da analise.

"""


#version 1.3b

#Importando bibliotecas.
import csv
import sys
import os

#Session1
with open('/home/rafael/Documents/export.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    #Iniciando a busca
    for row in csv_reader:
        if line_count == 0:
            var1 = 0
            line_count += 1
        else:
            #Session2

            #Abrir um novo arquivo para registro.
            openArquivo = open("/home/rafael/Documents/output.log", "a")

            #atribuir o caminho para variavel.
            var1 = row[1]

            #criando variaveis resultados.
            resultadoBusca = "Diretorio Vazio."
            resultadoBusca1 = "Diretorio com Arquivos."
            resultadoBusca2 = "Diretorio Não Existe."
            
            #Criando a variavel para iniciar a busca.
            diretorio = var1

            #Verificar se o diretorio e vazio se existe arquivo ou se o diretorio não existe.
            if os.path.isdir(diretorio):

                if not os.listdir(diretorio):

                    print(f'{row[0]}, {row[1]}, {row[2]}, {resultadoBusca}', file=openArquivo)

                else:

                    print(f'{row[0]}, {row[1]}, {row[2]}, {resultadoBusca1}', file=openArquivo)
            else:

                print(f'{row[0]}, {row[1]}, {row[2]}, {resultadoBusca2}', file=openArquivo)

            line_count += 1
    #print(f'Processed {line_count} lines.')