try: 

    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    div = n1 / n2
    print(f"A divisão de {n1} por {n2} é igual a {div:.2f}")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

except (ValueError, TypeError) as e:
    print(f"Você deve digitar um número. - {e}")