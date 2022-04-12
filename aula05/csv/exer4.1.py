import csv
import sys

def main(argv):
    fich_csv = open(argv[1], "r")
    csv_reader = csv.reader(fich_csv, delimiter=",")
    linhas = []
    for row in csv_reader:
        linhas.append(row)
    linhas = linhas[1:]
    fich_csv.close()

    tempMax = float(linhas[0][3])
    tempMin = float(linhas[0][3])
    soma = 0
    for linha in linhas:
        temp = float(linha[3])
        if temp > tempMax:
            tempMax = temp
        if temp < tempMin:
            tempMin = temp
        soma += temp
    media = soma / len(linhas)
    print("Média: {:.2f}".format(media))
    print("Temperatura máxima: {:.2f}".format(tempMax))
    print("Temperatura mínima: {:.2f}".format(tempMin))

main(sys.argv)