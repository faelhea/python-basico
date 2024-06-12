#rotina para deixa a tela sempre limpa
import subprocess

#limpar a tela, saida do comando para limpar a tela.!
subprocess.run(["clear"])

#python teste pára abrir csv export da base de imagens diagnose
"""
import pandas as pd

df = pd.read_csv('/home/rafael/Documents/export.csv')

print(df.to_string())

"""



"""
import csv

with open('/home/rafael/Documents/export.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
"""




#Esse exemplo e bom para localizar um coluna e linha especifica.
#url aonde achei o exemplo. (https://discuss.python.org/t/how-can-i-retrieve-a-specific-element-in-a-csv-file/19659)

"""
import csv
import sys
import subprocess

#limpar a tela, saida do comando para limpar a tela.!
subprocess.run(["clear"])


with open('/home/rafael/Documents/export.csv') as cards:
    csv_reader = csv.reader(cards)
    for index, row in enumerate(csv_reader):
        if index == 1: #colune
            #print(row) #linha
            #print(row[0]) #linha
            #print(row[0],row[1]) #linha
"""
        
#URL = https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
import pandas as pd
import csv

"""
df = pd.read_csv('/home/rafael/Documents/export.csv')

print(df['diretorio'])
#print(df.iloc[0])
# 
"""

"""
file = open('/home/rafael/Documents/export.csv')
csvreader = csv.reader(file)
header  = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
"""

"""
rows=[]
with open('/home/rafael/Documents/export.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)
"""


#script inicial
"""
import csv
import sys
import os

with open('/home/rafael/Documents/export.csv') as cards:
    csv_reader = csv.reader(cards)
    for index, row in enumerate(csv_reader):
        if index == 1: #colune
            print(row) #linha
            #print(row[0]) #linha
            #print(row[0],row[1], row[2]) #linha
            

diretorio = row[1]
print(diretorio)

#Verificar se o diretorio e vazio se existe arquivo ou se o diretorio não existe.
if os.path.isdir(diretorio):
    if not os.listdir(diretorio):
        print("Diretorio Vazio.")
    else:
        print("Diretorio com arquivo.")
else:
    print("Diretorio não existe.")
"""

#Pegar valor e percorrer cada linha do csv
"""
import csv
with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

Eric Idle
John Cleese

print(row)
{'first_name': 'John', 'last_name': 'Cleese'}
"""

#Exemplo para escrita dentro do CSV

"""
import csv

with open('/home/rafael/Documents/some.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name','teste']
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans', 'teste': 'teste feito.'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
    
"""

#Primeira parte do script feito, ele abre o csv e grava as informações em um novo arquivo texto.
#Version 1.0

"""
import csv
import sys

with open('/home/rafael/Documents/export.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #Abrir um novo arquivo para registro.
            var1 = open("/home/rafael/Documents/output.log", "a")
        
            print(f'\t{row[0]}, {row[1]}, {row[2]}', file=var1)
            
            line_count += 1
    print(f'Processed {line_count} lines.')
"""



#Iniciando a segunda parte que inicia  buscar pelo diretorio.
#version 1.2


"""
import csv
import sys
import os


with open('/home/rafael/Documents/export.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            var1 = 0
            line_count += 1
        else:
            #Abrir um novo arquivo para registro.
            var1 = open("/home/rafael/Documents/output.log", "a")
        
            #print(f'\t{row[0]}, {row[1]}, {row[2]}', file=var1)
            #print(f'\t{row[0]}, {row[1]}, {row[2]}')
            var1 = row[1]
            #print(var1[13:18])
            #var2 = var1[13:18]
            #subprocess.run(["find /home/rafael/local -type d -name {0}".format(var2)], shell=True)
            print(var1)
            diretorio = var1
            #Verificar se o diretorio e vazio se existe arquivo ou se o diretorio não existe.
            if os.path.isdir(diretorio):
                if not os.listdir(diretorio):
                    print("Diretorio Vazio.")
                else:
                    print("Diretorio com arquivo.")
            else:
                print("Diretorio não existe.")
            #break
            line_count += 1
    #print(f'Processed {line_count} lines.')

"""


#Versão para fazer buscar e gravar no arquivo.
#version 1.3

import csv
import sys
import os


with open('/home/rafael/Documents/export.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            var1 = 0
            line_count += 1
        else:
            #Abrir um novo arquivo para registro.
            openArquivo = open("/home/rafael/Documents/output.log", "a")

            #Gravar no arquivo externo        
            #print(f'\t{row[0]}, {row[1]}, {row[2]}', file=var1)

            #atribuir o caminho para variavel.
            var1 = row[1]
            #Imprimir o valor da variavel para debug
            #print(var1)

            #criando variaveis resultados.
            resultadoBusca = "Diretorio Vazio."
            resultadoBusca1 = "Diretorio com Arquivos."
            resultadoBusca2 = "Diretorio Não Existe."
            
            #Criando a variavel para iniciar a busca.
            diretorio = var1
            #Verificar se o diretorio e vazio se existe arquivo ou se o diretorio não existe.
            if os.path.isdir(diretorio):
                if not os.listdir(diretorio):
                    #print("Diretorio Vazio.")
                    print(f'{row[0]}, {row[1]}, {row[2]}, {resultadoBusca}', file=openArquivo)
                else:
                    #print("Diretorio com arquivo.")
                    print(f'{row[0]}, {row[1]}, {row[2]}, {resultadoBusca1}', file=openArquivo)
            else:
                #print("Diretorio não existe.")
                print(f'{row[0]}, {row[1]}, {row[2]}, {resultadoBusca2}', file=openArquivo)
            #break
            line_count += 1
    #print(f'Processed {line_count} lines.')

