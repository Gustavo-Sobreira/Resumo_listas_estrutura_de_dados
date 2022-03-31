lista = [1, 2, 3, 4]
operacao = []
saida = []
entrada = []
deseja = 1
while deseja == 1:


    repete = 0

    while repete == 0:
        repete += 1
        escolha = int(input("\033[1;32m[ 1 ] -> lista.append()\n"
                             "[ 2 ] -> lista.insert()\n"
                             "\033[1;31m[ 3 ] -> lista.pop()\n"
                             "[ 4 ] -> lista.remove()\n"
                             "\033[1;34m[ 5 ] -> lista.sort()\n"
                             "[ 6 ] -> lista.reverse()\033[m\n\n"
                             f"Dado a lista: \n{lista}\nqual alteração deseja?"))
        if escolha < 1 or escolha > 6:
            repete = 0

    print("\n")

    if escolha == 1:
        val = int(input("Qual número inteiro deseja adicionar no final da lista?"))
        lista.append(val)
        entrada.append(val)
        operacao.append(f"append({val})")
    else:
        if escolha == 2:
            pos = int(input("Qual a posição que deseja alocar o valor?"))
            val = int(input("Qual número inteiro deseja adicionar no final da lista?"))
            lista.insert(pos, val)
            entrada.append(val)
            operacao.append(f"insert({pos, val})")
        else:
            if escolha == 3:
                pos = int(input("Qual posição deseja remover? (-1 == vazio) "))
                if pos == -1:
                    saida.append(lista.pop())
                    operacao.append("pop()")

                else:
                    if pos in lista:
                        saida.append(lista.pop(pos))
                        operacao.append(f"pop({pos})")
                    else:
                        saida.append("Nada")
                        operacao.append("Inválida")
            else:
                if escolha == 4:
                    val = int(input("Qual número deseja remover? "))
                    if val in lista:
                        lista.remove(val)
                        saida.append(val)
                        operacao.append(f"remove({val})")
                    else:
                        saida.append("Nada")
                        operacao.append("Inválida")
                else:
                    if escolha == 5:
                        lista.sort()
                        operacao.append("sort()")
                    else:
                        if escolha == 6:
                            lista.reverse()
                            operacao.append("reverse()")

    print("\n\nLISTA ATUAL:\n"
          f"\033[1;33m{lista}\033[m\n\n"
          f"OPERAÇÃO ATUAL:\n"
          f"{operacao[len(operacao) -1]}\n\n"
          f"TODAS OPERAÇÕES:\n"
          f"{operacao}\n\n"
          f"TODOS ELEMENTOS REMOVIDOS:\n"
          f"\033[1;31m{saida}\033[m"
          )

    if escolha in (1, 2):
        print("\nADICIONADO AGORA\n"
              f"\033[1;32m{entrada[len(entrada) - 1]}\033[m")

    if escolha in (3, 4):
        print("\nREMOVIDO AGORA:\n"
              f"\033[1;31m{saida[len(saida) -1]}\033[m")


    deseja =+ int(input("\n\nDIGITE 1 PARA CONTINUAR O PROGRAMA\n\n"))

print(deseja)