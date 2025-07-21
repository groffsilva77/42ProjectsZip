from storyline import introduce_game

class Character:
    def __init__(self, name, hp, atk, defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.skills = {}
        self.occup = "Desconhecida"

    def recieve_dmg(self, dmg):
        final_dmg = max(0, dmg - self.defence)
        self.hp -= final_dmg
        print(f"{self.player_name} recebeu {final_dmg} de dano. HP restante: {self.hp}")
        return self.HP

    def_attack(self, target):
        print(f)