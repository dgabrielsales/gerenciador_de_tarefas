import random

class Carta:
    def __init__(self, nome, ataque, defesa):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
    
    def __str__(self):
        return f"{self.nome} (ATK: {self.ataque} | DEF: {self.defesa} )"


class CartaCura(Carta):
    def __init__(self, nome, cura):
        super().__init__(nome, ataque=0, defesa=0)
        self.cura = cura
    
    def __str__(self):
        return f"{self.nome}( Poção de cura +{self.cura})"

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 10
        self.mao = []

    def comprar_carta(self, baralho, quantidade=3):
        self.mao = random.sample(baralho, quantidade)
    
    def escolher_carta(self):
        print(f"Cartas de {self.nome}")
        for i, carta in enumerate(self.mao):
            print(f"{i}: {carta}")
        escolha = int(input(f"{self.nome}, escohla uma carta (0-{len(self.mao)-1}): "))
        return self.mao.pop(escolha)
    

class Jogo():
    def __init__(self):
        self.baralho = self.criar_baralho()
        self.jogador1 =  Jogador("Jogador 1")
        self.jogador2 = Jogador("Jogador 2")


    def criar_baralho(self):
      return [
        Carta("Mago de Fogo", 4.5, 2.5),
        Carta("Rei Goblin", 6.1, 4.5),
        Carta("Rei do Reino Dark", 7.1, 4.1),
        Carta("Peão Ataque", 3, 2),
        Carta("Morteiros 45", 3.9, 1),
        Carta("Arqueira de Longo Alcance", 4, 1),
        Carta("Dragão de Gelo", 8.2, 6.3),
        Carta("Lobisomem da Lua Cheia", 5.7, 4.8),
        Carta("Cavaleiro da Aurora", 6.5, 7.0),
        Carta("Assassino Sombrio", 7.8, 3.2),
        Carta("Fênix Renascida", 5.5, 5.5),
        Carta("Gigante de Pedra", 4.8, 9.1),
        Carta("Bruxa do Pantano", 6.7, 3.9),
        Carta("Paladino Sagrado", 7.5, 8.0),
        Carta("Espadachim Veloz", 5.2, 4.0),
        Carta("Necromante dos Ossos", 6.8, 3.5),
        Carta("Troll da Montanha", 7.3, 6.7),
        Carta("Sereia Encantadora", 4.7, 5.2),
        Carta("Golem de Cristal", 5.9, 8.5),
        Carta("Arcano das Runas", 8.0, 4.3),
        CartaCura("Poção de Vida", 3),
        CartaCura("Poção de Vida Suprema", 10),
    ]


  
    def calcular_dano(self, atacante, defensor):
        dano = atacante.ataque - defensor.defesa
        return max(dano, 0)
    

    def rodar(self):
        while self.jogador1.vida > 0 and self.jogador2.vida > 0:
            self.jogador1.comprar_carta(self.baralho)
            self.jogador2.comprar_carta(self.baralho)

            carta1 = self.jogador1.escolher_carta()
            carta2 = self.jogador2.escolher_carta()
            
            if isinstance(carta1, CartaCura):
                  self.jogador1.vida += carta1.cura
                  dano1 = 0  # Não causa dano
            else:
                 dano1 = self.calcular_dano(carta1, carta2)

            

            if isinstance(carta2, CartaCura):
                  self.jogador2.vida += carta2.cura
                  dano2 = 0
            else:
                  dano2 = self.calcular_dano(carta2, carta1)

            print(f"\n{self.jogador1.nome} jogou: {carta1}")
            print(f"{self.jogador2.nome} jogou: {carta2}")

            dano1 = self.calcular_dano(carta1, carta2)
            dano2 = self.calcular_dano(carta2, carta1)

            self.jogador2.vida -= dano1
            self.jogador1.vida -= dano2

            print(f"{self.jogador1.nome} causou {dano1:.1f} de dano!")
            print(f"{self.jogador2.nome} causou {dano2:.1f} de dano!")

            print(f"\n💙 Vida {self.jogador1.nome}: {self.jogador1.vida:.1f}")
            print(f"💙 Vida {self.jogador2.nome}: {self.jogador2.vida:.1f}")

        self.declarar_vencedor()

    def declarar_vencedor(self):
        if self.jogador1.vida > self.jogador2.vida:
            print(f"\n🎉 {self.jogador1.nome} venceu!")
        elif self.jogador2.vida > self.jogador1.vida:
            print(f"\n🎉 {self.jogador2.nome} venceu!")
        else:
            print("\n⚖️ Empate!")

if __name__ == "__main__":
    jogo = Jogo()
    jogo.rodar()
