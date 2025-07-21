from occup import Character

class enemy:
    def __init__(self, enemy_name, hp, atk, defence):
        self.enemy_name = enemy_name
        self.hp = hp
        self.atk = atk
        self.defence = defence
        self.skills = {}

    def recieve_dmg(self, dmg):
        final_dmg = max(0, dmg - self.defence)
        self.hp -= final_dmg
        print(f"{self.enemy_name} recebeu {final_dmg} de dano. Seu HP restante é: {self.hp}")
        return self.hp

    def attack(self, target):
        print(f"{self.enemy_name} ataca {target.player_name}")
        target.recieve_dmg(self.atk)