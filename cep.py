from os import system
system('cls')
import requests, json

nome = input('Digite seu nome: ')
cep = (input('Digite seu CEP: '))
requests = requests.get(f'http://viacep.com.br/ws/{cep}/json')
requests = requests.json()

if __name__ == '__main__':
    system('cls')

    print(f'Olá {nome}. Segue as informações do CEP {cep} informado\n')
    print(f'Rua: {requests["logradouro"]}')
    print(f'CEP: {requests["cep"]}')
    print(f'Bairro: {requests["bairro"]}')
    print(f'Cidade: {requests["localidade"]}')