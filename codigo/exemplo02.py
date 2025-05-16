try:

    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    resultao = n1 / n2

except Exception as e:
    print(f"Erro - {e}")

else:
    print(f"A divisão de {n1} por {n2} é igual a {resultao:.2f}")

finally:
    print("Fim do programa.")