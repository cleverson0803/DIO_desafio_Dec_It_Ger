from abc import ABC, abstractmethod
from datetime import datetime


# Decorador para logar transações
def log_transacao(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        tipo_transacao = func.__name__
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{data_hora} - Transação: {tipo_transacao}')
        return result
    return wrapper


class ContaIterador:
    def __init__(self, contas):
        self._contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._contas):
            conta = self._contas[self._index]
            self._index += 1
            return conta
        else:
            raise StopIteration


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self.transacoes:
            if tipo_transacao is None or transacao['tipo'] == tipo_transacao:
                yield transacao


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @log_transacao
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False
        elif valor > 0:
            self._saldo -= valor
            self._historico.adicionar_transacao({'tipo': 'saque', 'valor': valor, 'data_hora': datetime.now()})
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

    @log_transacao
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao({'tipo': 'deposito', 'valor': valor, 'data_hora': datetime.now()})
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False


# Exemplo de uso

# Criando clientes
cliente1 = PessoaFisica("João Silva", "1990-01-01", "123.456.789-00", "Rua A, 123")
cliente2 = PessoaFisica("Maria Santos", "1985-05-05", "987.654.321-00", "Rua B, 456")

# Criando contas
conta1 = Conta.nova_conta(cliente1, "0001")
conta2 = Conta.nova_conta(cliente2, "0002")

# Adicionando contas aos clientes
cliente1.adicionar_conta(conta1)
cliente2.adicionar_conta(conta2)

# Realizando transações
conta1.depositar(1000)
conta1.sacar(500)
conta2.depositar(1500)
conta2.sacar(300)

# Gerando relatório de transações da conta1
print("\nRelatório de todas as transações da conta1:")
for transacao in conta1.historico.gerar_relatorio():
    print(transacao)

print("\nRelatório de saques da conta1:")
for transacao in conta1.historico.gerar_relatorio('saque'):
    print(transacao)

# Iterando sobre as contas do banco
banco = [conta1, conta2]
conta_iterador = ContaIterador(banco)

print("\nIterando sobre as contas do banco:")
for conta in conta_iterador:
    print(f"Conta: {conta.numero}, Saldo: {conta.saldo}, Cliente: {conta.cliente.nome}")
