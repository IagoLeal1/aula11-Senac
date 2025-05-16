print('=== CAIXA ELETRÔNICO ===')

try: 

    saldo = 1000
    saque = float(input("Digite o valor do saque: "))

except ValueError as e:
    print(f"Você deve digitar um número. - {e}")

else:
    if saque < 0:
        if saldo >= saque:
            saldo -= saque
        elif saque > saldo:
            print("Você não tem saldo suficiente.")
            print(f"Seu saldo é de R$ {saldo:.2f}")
        else:
            print(f"Seu saldo é de R$ {saldo:.2f}")

finally:
    print(f"Seu saldo é de R$ {saldo:.2f}")
    print("Fim do programa.")