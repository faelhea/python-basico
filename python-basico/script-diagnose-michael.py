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
            
            



        