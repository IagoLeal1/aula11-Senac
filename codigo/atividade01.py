try:

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    total = n1 + n2

except ValueError as e:
    print(f"Você deve digitar um número. - {e}")

else:
    if 0 <= n1 <= 10 and 0 <= n2 <= 10:
        media = total / 2
        print(f"A média de {n1} e {n2} é igual a {media:.2f}")
        if media >= 6:
            print("Aprovado")
        else:
            print("Reprovado")
    elif n1 < 0 or n2 < 0:
        print("Você deve digitar números positivos.")
    else:
        print("Você deve digitar números entre 0 e 10.")
finally:
    print("Fim do programa.")