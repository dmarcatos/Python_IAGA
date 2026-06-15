while True:
    n = 0
    while (((n % 2) == 0) or (n <= 0)) and (n != -1):
        n = int(input("Tamanho da matriz (um número positivo e ímpar, -1 para encerrar) ? "))

    if (n == -1):
        break

    meio = n // 2
    print()
    for i in range (n):
        for j in range (n):
            if i == meio and j == meio:
                valor = "0"

            elif i == j and i < meio:
                valor = "1"

            elif i + j == n - 1 and i < meio:
                valor = "2"

            elif i == j and i > meio:
                valor = "3"

            elif i + j == n - 1 and i > meio:
                valor = "4"

            elif i < j and i < meio and i + j < n:
                valor = "→"

            elif i < j and i + j >= n:
                valor = "↓"

            elif i > j and i > meio and i + j >= n:
                valor = "←"

            else:
                valor = "↑"

            print(f" {valor} ", end="")
        print()
    print()