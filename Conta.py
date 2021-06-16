class Conta:
    def __init__(self, numero, titular, saldo, limite):
        #print("Construindo um objeto... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite



conta = Conta(123, "Yara", 55.5, 1000)
conta1 = Conta(321, "Fabio", 1000, 50)
print(conta.titular)
print(conta1.titular)