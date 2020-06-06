print("========= CALCULADORA ========")
n1 = float(input("Digite o primeiro numero para operação "))
print("----" * 12)
n2 = float(input("Digite o segundo numero para operção "))
opção = 0
while opção != 5:
    print("===" * 12)
    print("""
  [1] Somar
  [2] Subtrair
  [3] Multiplicar
  [4] Dividir
  [5] Sair do programa""")
    opção = int(input("Qual opção você deseja executar ? "))

    if opção == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é igual á  {} ".format(n1, n2, soma))
    elif opção == 2:
        sub = n1 - n2
        print("A subtração entre {} e {} é igual á {}".format(n1, n2, sub))
    elif opção == 3:
        mult = n1 * n2
        print("A multiplicação entre {} e {} é igual á {} ".format(n1, n2, mult))
    elif opção == 4:
        div = n1 / n2
        print("A divisão entre {} e {} é igual á {}".format(n1, n2, div))
    elif opção == 5:
        print("Você saiu do programa volte sempre !")
    else:
        print("Opção invalida tente outro numero!")


