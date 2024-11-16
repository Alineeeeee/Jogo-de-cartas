import random

def cartas():
    numeracao = list(range(1, 10))
    cores = ["azul", "vermelha", "amarela", "verde"]

    baralho = []
    for numero in numeracao:
        for cor in cores:
            baralho.append((numero, cor))

    return baralho

def validacao(carta_jogo, carta_posta):
    cor_igual = carta_jogo[1] == carta_posta[1]
    numero_igual = carta_jogo[0] == carta_posta[0]
    return cor_igual or numero_igual


def play():
    print("Para começarmos o jogo, digite o nome dos jogadores: ")
    jogador1 = input("Jogador 1: ")
    jogador2 = input("Jogador 2: ")

    conjunto = cartas()
    
    random.shuffle(conjunto)

    vez_jogador1 = []
    for i in range(5):
        vez_jogador1.append(conjunto.pop())

    vez_jogador2 = []
    for i in range(5):
        vez_jogador2.append(conjunto.pop())

    carta_posta = conjunto.pop()

    jogadores = [(jogador1, vez_jogador1), (jogador2, vez_jogador2)]
    player_atual = 0

    rodada_atual = True
    fim_baralho = False
    sem_baralho = False

    while rodada_atual:
        nome, mao = jogadores[player_atual]
        print(f"É a sua vez {nome}!")
        print(f"Carta posta: {carta_posta[0]} {carta_posta[1]}")

        print("Sua mão:")
        for i, carta in enumerate(mao):
            print(f"{i}: {carta[0]} {carta[1]}")

        next = []
        for carta in mao:
            if validacao(carta, carta_posta):
                next.append(carta)

        if len(next) > 0:
            jogada_realizada = False
            while not jogada_realizada:
                try:
                    jogando = int(input(f"Jogue uma carta de (0 a {len(mao) - 1}): "))
                    carta_escolhida = mao[jogando]

                    if validacao(carta_escolhida, carta_posta):
                        carta_posta = mao.pop(jogando)
                        print(f"{nome} jogou {carta_posta[0]} {carta_posta[1]}!")
                        jogada_realizada = True
                    else:
                        print("Você escolheu uma carta inválida. Tente novamente.")
                except (ValueError, IndexError):
                    print("Entrada inválida. Digite um índice válido.")
        else:
            if len(conjunto) > 0:
                carta_monte = conjunto.pop()
                mao.append(carta_monte)
                print(f"{nome} comprou uma carta.")
            else:
                sem_baralho = True
                print("Fim do baralho, vamos descobrir o ganhador...")

        if len(mao) == 0:
            print(f"\n{nome} você ganhou, ganhará um passe de batalha.")
            rodada_atual = False
        else:
            if sem_baralho:
                mao_jogador1 = len(jogadores[0][1])
                mao_jogador2 = len(jogadores[1][1])

                if mao_jogador1 < mao_jogador2:
                    print(f"\n{jogador1} ganhou por ter menos cartas.")
                elif mao_jogador2 < mao_jogador1:
                    print(f"\n{jogador2} ganhou por ter menos cartas!")
                else:
                    print("\nEmpate, para desempatar é só fazer um x1!")
                rodada_atual = False

        if rodada_atual:
            player_atual = 1 - player_atual

play()

