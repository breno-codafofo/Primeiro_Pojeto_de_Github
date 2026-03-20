class Conta():
    def __init__(self,saldo):
        self._saldo = saldo # atributo protegido
c = Conta(100)
print(c._saldo) # funciona, porém é considerado má prática