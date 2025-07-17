class story:
    def __init__(self):
        self.player_name = None
        self.warrior_occup = "Guerreiro"
        self.mage_occup = "Mago"
        self.cleric_occup = "Clérigo"
        self.land_name = "Earhardt"

    def introduce_game(self):
        print("Olá, humano, eu sou a Samantha, aquela que governa a linha tênue entre o seu mundo e os diversos\noutros espalhados neste vasto universo.")
        print("Antes de tudo, como você se chama?")
        self.player_name = input("Digite o seu nome: ")
        print(f"Certo, prazer em te conhecer {self.player_name}. Enfim, vamos ao que interessa, onde você irá desembarcar: {self.land_name}!")

        return (self.player_name)