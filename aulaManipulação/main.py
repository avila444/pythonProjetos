import json
import csv


def main():

    """
    Jeito menos certo de fazer
    arquivoT = open('arquivo.txt', 'w')  # r: ler || w: escrever
    arquivoT.write('HAHAHA')
    arquivoT.close()  #fecha o arquivo

    #Melhor jeito de escrever
    with open('arquivo.txt', 'w') as arquivoT:
        arquivoT.write('Escrevendo...')

    #Melhor jeito de ler
    with open('arquivo.txt', 'r') as arquivoT:
        linhas = arquivoT.readlines()

        for linha in linhas:
            print(linha)

    #JSON
    with open('arquivo.json', 'r') as arquivoJ:
        dic = json.load(arquivoJ)
        #Resto do código
        print(dic['nome'])

    with open('arquivo.json', 'w') as arquivoJ:
        pessoas = {'nome': 'davi'}
        json.dump(pessoas, arquivoJ, indent=2)
    """
    with open('arquivo.csv', 'w') as arquivo:
        writer = csv.writer(arquivo, delimiter=",")
        writer.writerow(['pessoa', 'beleza'])
        writer.writerow(['davi', 'amedrontador'])
        writer.writerow(['delas', 'fofo'])
        writer.writerow(['dbrabos', 'fofo'])


if __name__ == '__main__':
    main()
