saldo = 200
saque = 159

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
