import csv
import os
from datetime import datetime

# Arquivo CSV para armazenar as faturas
FILE_NAME = 'faturas.csv'

# Função para inicializar o arquivo CSV se não existir
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Descrição', 'Valor', 'Data de Vencimento', 'Pago'])

# Função para adicionar uma nova fatura
def adicionar_fatura(descricao, valor, data_vencimento):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([descricao, valor, data_vencimento, 'Não'])

# Função para marcar uma fatura como paga
def marcar_fatura_como_paga(descricao):
    faturas = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == descricao:
                row[3] = 'Sim'
            faturas.append(row)
    
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(faturas)

# Função para listar todas as faturas
def listar_faturas():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Descrição: {row[0]}, Valor: {row[1]}, Data de Vencimento: {row[2]}, Pago: {row[3]}")

# Função para deletar uma fatura
def deletar_fatura(descricao):
    faturas = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != descricao:
                faturas.append(row)
    
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(faturas)

# Função principal para interação com o usuário
def main():
    initialize_file()
    
    while True:
        print("\nControle de Faturas")
        print("1. Adicionar Fatura")
        print("2. Listar Faturas")
        print("3. Marcar Fatura como Paga")
        print("4. Deletar Fatura")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            descricao = input("Descrição da Fatura: ")
            valor = input("Valor: ")
            data_vencimento = input("Data de Vencimento (DD/MM/AAAA): ")
            adicionar_fatura(descricao, valor, data_vencimento)
            print("Fatura adicionada com sucesso!")
        
        elif opcao == '2':
            listar_faturas()
        
        elif opcao == '3':
            descricao = input("Descrição da Fatura a ser marcada como paga: ")
            marcar_fatura_como_paga(descricao)
            print("Fatura marcada como paga.")
        
        elif opcao == '4':
            descricao = input("Descrição da Fatura a ser deletada: ")
            deletar_fatura(descricao)
            print("Fatura deletada.")
        
        elif opcao == '5':
            print("Saindo do sistema...")
            break 

        

    
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
