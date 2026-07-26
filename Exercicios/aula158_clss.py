from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self, agencia, num_conta, saldo):
        self._agencia = agencia
        self._num_conta = num_conta
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        return self._saldo


    @property
    def num_conta(self):
        return self._num_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @property
    def saldo_formatado(self):
        saldo = f'{self._saldo:.2f}'.replace('.', ',')
        return saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def __str__(self):
        return f'''\nAgência: {self._agencia}
Número da conta: {self._num_conta}
Saldo: R$ {self.saldo_formatado}
        '''

class ContaCorrente(Conta):
    def sacar(self, valor):
        if valor > self._saldo + 150:
            print(f'Saldo insuficiente.\nSeu saldo R$ {self.saldo_formatado}.\nVocê pode pedir até R$ 150,00 de empréstimo.')
        else:
            self._saldo -= valor
            if self._saldo < 0:
                print(f'Você resgatou um limite extra.\nValor em dívida: R$ {self.saldo_formatado}')
            else:
                print(f'Saque bem-sucedido.\nSaldo da conta: R$ {self.saldo_formatado}')
        return self._saldo

class ContaPoupanca(Conta):

    def sacar(self, valor):
        if valor > self._saldo:
            print(f'Saldo insuficiente.\nSeu saldo: R$ {self.saldo_formatado}')
        else:
            self._saldo -= valor
            print(f'Saque bem-sucedido.\nSaldo da conta: R$ {self.saldo_formatado}')
        return self._saldo

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def criar_conta(self, agencia, num_conta):
        self._agencia = agencia
        self._num_conta = num_conta
        self._saldo = 0

yasuo = ContaCorrente(10, 25, 0)
print(yasuo)



