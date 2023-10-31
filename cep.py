from os import system
import requests
system('cls')

def obter_informacoes_cep(cep):
    try:
        # Verifica se o CEP contém apenas números
        if not cep.isdigit():
            raise ValueError("O CEP deve conter apenas números.")

        response = requests.get(f'http://viacep.com.br/ws/{cep}/json')
        data = response.json()

        # Verifica se o CEP existe no retorno da API
        if 'erro' in data:
            raise Exception("CEP não encontrado.")

        return data
    except ValueError as ve:
        print(f"Erro ao processar o CEP: O CEP deve conter apenas números.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return None

def main():
    nome = input('Digite seu nome: ')
    cep = input('Digite seu CEP: ')

    informacoes_cep = obter_informacoes_cep(cep)
    if informacoes_cep:
        print(f'Olá {nome}. Seguem as informações do CEP ({cep}) informado:\n')
        print(f'Rua: {informacoes_cep["logradouro"]}')
        print(f'CEP: {informacoes_cep["cep"]}')
        print(f'Bairro: {informacoes_cep["bairro"]}')
        print(f'Cidade: {informacoes_cep["localidade"]}')
        print(f'UF: {informacoes_cep["uf"]}')

if __name__ == '__main__':
    main()
