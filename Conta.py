class Conta:
    def __init__(self, numero, titular, saldo, limite):
        #print("Construindo um objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo  = {self.saldo} do titular {self.titular}")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta1 = Conta(321, "Fabio", 1000, 50)
conta1.sacar(50)
conta1.extrato()
