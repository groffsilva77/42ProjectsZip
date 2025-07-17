from storyline import story
from combat import combate

game_story = story()
game_story.introduce_game()
print(f"Se prepare, {game_story.player_name}, você entrará em combate!")

meu_hp = 100
meu_atk = 20
goblin_hp = 50
goblin_atk = 10

meu_hp, goblin_hp = combate(meu_hp, meu_atk, goblin_hp, goblin_atk, "Goblin")

if meu_hp > 0:
    print("\nParabéns, você venceu a batalha!")
else:
    print("\nGame Over.")