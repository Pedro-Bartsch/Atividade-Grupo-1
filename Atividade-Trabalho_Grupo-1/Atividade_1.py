"""Nomes dos integrantes da equipe: Pedro Henrique Bartsch da Silva, Kauany dos Santos Paterno, Giseli Kethelin, Mateus W., Luiz Guilherme
Garcia, Vinícius Pinheiro, Guilherme Torres, Victor Stipp.

Turma: TDESI 1/V1
Tema da atividade: Conta bancária
"""

class ContaBancaria:
    def __init__(self, nome):
        self.__saldo = 0  
        self.numero_conta = 123456
        self.nome_titular = nome

    def consulta_saldo(self):
        print(f'Seu saldo atual é de R${self.__saldo:,.2f}')

    def _alterar_saldo(self, valor):
        self.__saldo += valor

    def deposito(self, valor):
        if valor > 0:
            self._alterar_saldo(valor)
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Deposite um valor válido')

    def saque(self, valor):
        if valor > 0:
            if self.__saldo - valor >= 0:
                self._alterar_saldo(-valor)
                print(f'Saque de R${valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para sacar esse valor.')
        else:
            print('Valor inválido para saque.')

class ContaCorrente(ContaBancaria):
    def __init__(self, nome):
        super().__init__(nome)
        self.limite = -1000  

    def saque(self, valor):
        if valor > 0:
            if self._ContaBancaria__saldo - valor >= self.limite:
                self._alterar_saldo(-valor)
                print(f'Saque de R${valor:.2f} realizado com sucesso.')
            else:
                print(f'Saldo insuficiente. Limite do cheque especial é R$ {self.limite}')
        else:
            print('Valor inválido para saque.')

class ContaPoupanca(ContaBancaria):
    def __init__(self, nome):
        super().__init__(nome)

    def aplicar_rendimento(self, taxa):
        rendimento = self._ContaBancaria__saldo * (taxa / 100)
        self._alterar_saldo(rendimento)
        print(f'Rendimento de R${rendimento:.2f} aplicado com sucesso.')

class ContaSalario(ContaBancaria):
    def __init__(self, nome):
        super().__init__(nome)

    def saque(self, valor):
        if valor > 0:
            if self._ContaBancaria__saldo - valor >= 0:
                self._alterar_saldo(-valor)
                print(f'Saque de R${valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente. Conta salário não permite cheque especial.')
        else:
            print('Valor inválido para saque.')

opcao = 0
conta_corrente = None
conta_salario = None
conta_poupanca = None

def verificar_conta():
    """Verifica se as contas foram criadas. Se não, exibe uma mensagem de erro."""
    if not conta_corrente or not conta_salario or not conta_poupanca:
        print("""
            ===========================================================================================
            |                                                                                          |
            |  Erro: Nenhuma conta foi criada. Por favor, crie as contas primeiro (opção 4).           |
            |                                                                                          |
            ============================================================================================""")
        return False
    return True

def menu_conta_corrente():
    """Menu para a Conta Corrente"""
    while True:
        print("""
 _________|=========================|__________
|         |   MENU CONTA CORRENTE   |          |
|         |=========================|          |
|                                              |
| [ 1 ] Depósito                               |
| [ 2 ] Saque                                  |
| [ 3 ] Consultar saldo                        |
| [ 4 ] Voltar ao menu princilpal              |
|                                              |
================================================""")
        acao = int(input("Escolha a ação: "))
        if acao == 1:
            valor = float(input("Valor do depósito: "))
            conta_corrente.deposito(valor)
        elif acao == 2:
            valor = float(input("Valor do saque: "))
            conta_corrente.saque(valor)
        elif acao == 3:
            conta_corrente.consulta_saldo()
        elif acao == 4:
            break  
        else:
            print("Ação inválida.")

def menu_conta_salario():
    """Menu para a Conta Salário"""
    while True:
        print("""
 _________|=========================|__________
|         |   MENU CONTA SALÁRIO    |          |
|         |=========================|          |
|                                              |
| [ 1 ] Saque                                  |
| [ 2 ] Consultar saldo                        |
| [ 3 ] Voltar ao menu princilpal              |
|                                              |
================================================""")
        
        acao = int(input("Escolha a ação: "))
        if acao == 1:
            valor = float(input("Valor do saque: "))
            conta_salario.saque(valor)
        elif acao == 2:
            conta_salario.consulta_saldo()
        elif acao == 3:
            break  
        else:
            print("Ação inválida.")

def menu_conta_poupanca():
    """Menu para a Conta Poupança"""
    while True:
        print("""
 _________|=========================|__________
|         |   MENU CONTA POUPANÇA   |          |
|         |=========================|          |
|                                              |
| [ 1 ] Depósito                               |
| [ 2 ] Consultar saldo                        |
| [ 3 ] Aplicar rendimento                     |
| [ 4 ] Voltar ao menu princilpal              |
|                                              |
================================================""")
        
        acao = int(input("Escolha a ação: "))
        if acao == 1:
            valor = float(input("Valor do depósito: "))
            conta_poupanca.deposito(valor)
        elif acao == 2:
            conta_poupanca.consulta_saldo()
        elif acao == 3:
            taxa = float(input("Taxa de rendimento (%): "))
            conta_poupanca.aplicar_rendimento(taxa)
        elif acao == 4:
            break  
        else:
            print("Ação inválida.")

while opcao != 5:
    print("""
          |=========================|
|=========|     MENU PRINCIPAL      |==========|
|         |=========================|          |
|                                              |
|                                              |
| [ 1 ] Acessar conta corrente                 |
| [ 2 ] Acessar conta salário                  |
| [ 3 ] Acessar conta poupança                 |
| [ 4 ] Criar contas                           |
| [ 5 ] Encerrar programa                      |
|                                              |
================================================""")

    opcao = int(input(">>>> Qual é a sua escolha? "))
    
    if opcao == 1:
        if verificar_conta():
            menu_conta_corrente()
    elif opcao == 2:
        if verificar_conta():
            menu_conta_salario()
    elif opcao == 3:
        if verificar_conta():
            menu_conta_poupanca()
    elif opcao == 4:
        nome = input("Digite o nome do titular: ")
        conta_corrente = ContaCorrente(nome)
        conta_salario = ContaSalario(nome)
        conta_poupanca = ContaPoupanca(nome)
        print("Contas criadas com sucesso!")
    elif opcao == 5:
        print("Encerrando operações...")
    else:
        print("Opção inválida. Tente novamente.")
    print("=-=" * 15)