import random

def cartas(): #função para criação do baralho
    numeracao = list(range(1, 10)) #uma lista que contém cartas de 0 a 9
    cores = ["azul", "vermelha", "amarela", "verde"] #lista com 4 cores

    baralho = [] #lista na qual serão inseridos os dados que o for alimentar(com append) quando percorrer numeração e cores
    for numero in numeracao:
        for cor in cores:
            baralho.append((numero, cor))

    return baralho

def validacao(carta_jogo, carta_posta): #aqui temos a função para validar a jogada dos jogadores, comparando a cor e o número
    cor_igual = carta_jogo[1] == carta_posta[1]
    numero_igual = carta_jogo[0] == carta_posta[0]
    return cor_igual or numero_igual #cor igual ou o número, não precisa ser os dois 


def play(): #aqui temos a função principal que definirá a lógica do jogo, inicialmente solicita o nome dos jogadores
    print("Para começarmos o jogo, digite o nome dos jogadores: ")
    jogador1 = input("Jogador 1: ")
    jogador2 = input("Jogador 2: ")

    conjunto = cartas() #aqui nós chamamos a função cartas(com todas informações de numeração e cores)
    random.shuffle(conjunto) #utilizamos shuffle(método random) para embaralhar as cartas na variável conjunto

    vez_jogador1 = [] #cria uma lista para armazenar cartas
    for i in range(5): #cartas armazenadas de 0 a 4
        vez_jogador1.append(conjunto.pop()) #remove do conjunto a última carta e adiciona na lista(no final) vez_jogador1 

    vez_jogador2 = []
    for i in range(5):
        vez_jogador2.append(conjunto.pop())

    carta_posta = conjunto.pop() #aqui temos a variável(carta_posta) que recebe a última carta do conjunto(definido por pop)

    jogadores = [(jogador1, vez_jogador1), (jogador2, vez_jogador2)] #temos uma lista com duas tuplas, para armazenar nome e mão do jogador
    player_atual = 0

    rodada_atual = True
    fim_baralho = False
    sem_baralho = False

    while rodada_atual: #while executará enquanto existir cartas no monte ou cartas na mão dos jogadores
        nome, mao = jogadores[player_atual]
        print(f"É a sua vez {nome}!")
        print(f"Carta posta: {carta_posta[0]} {carta_posta[1]}") #aqui temos o índice 0 = número e indíce 1 = cor, definido na função inicial cartas
        print("Sua mão:")

        for i, carta in enumerate(mao): #usei enumerate (função) para retornar o índice e a cor que a ele corresponde 
            print(f"{i}: {carta[0]} {carta[1]}") #mostra a mão do jogador

        next = []
        for carta in mao:
            if validacao(carta, carta_posta): #chama a função validação(que compara a carta do jogador com a carta_posta da mesa)
                next.append(carta) #adiciona essa carta na lista next para seguirmos o jogo

        if len(next) > 0: #utilizamos len para saber o tamanho da lista e assim compararmos se ainda tem cartas
            jogada_realizada = False
            while not jogada_realizada: #aqui temos um laço while que executará enquanto o jogador não realizar uma jogada válida
                try:
                    jogando = int(input(f"Jogue uma carta de (0 a {len(mao) - 1}): "))
                    carta_escolhida = mao[jogando] #aqui temos uma variável que recebe a carta que o jogador escolheu, de acordo com o índice

                    if validacao(carta_escolhida, carta_posta):
                        carta_posta = mao.pop(jogando) # aqui vamos adicionar a carta da mesa a última carta que o jogador escolheu
                        print(f"{nome} jogou {carta_posta[0]} {carta_posta[1]}!")
                        jogada_realizada = True
                    else:
                        print("Você escolheu uma carta inválida. Tente novamente.")
                except (ValueError, IndexError):
                    print("Entrada inválida. Digite um índice válido.")
        else:
            if len(conjunto) > 0:
                carta_monte = conjunto.pop() #aqui a variável carta_monte recebe a última carta de conjunto
                mao.append(carta_monte) #adiciona a última carta do monte na mão do jogador da vez
                print(f"{nome} comprou uma carta.")
            else:
                sem_baralho = True 
                print("Fim do baralho, vamos descobrir o ganhador...")

        if len(mao) == 0: #pegamos a mão do jogador atual e vemos se tem alguma carta nela
            print(f"\n{nome} você ganhou, ganhará um passe de batalha.")
            rodada_atual = False
        else:
            if sem_baralho:
                mao_jogador1 = len(jogadores[0][1]) #pega o tamanho da lista do jogador 1
                mao_jogador2 = len(jogadores[1][1]) #pega o tamanho da lista do jogador 2

                if mao_jogador1 < mao_jogador2:
                    print(f"\n{jogador1} ganhou por ter menos cartas.")
                elif mao_jogador2 < mao_jogador1:
                    print(f"\n{jogador2} ganhou por ter menos cartas!")
                else:
                    print("\nEmpate, para desempatar é só fazer um x1!")
                rodada_atual = False
                #nesse penúltimo bloco, temos as comparações para verificar o ganhador ou se deu empate
        if rodada_atual:
            player_atual = 1 - player_atual #aqui temos a alternância de jogador, quando o player atual for 0, é o primeiro jogador que está jogando.
                                            #assim, 1 - 0 = 1, fazendo a troca para o segundo jogador
play() #chamamos a função para a mesma executar e iniciar o jogo

