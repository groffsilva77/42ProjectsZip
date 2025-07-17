def combate(player_hp, player_atk, enemy_hp, enemy_atk, enemy_name):
    print(f"\n--- Batalha contra {enemy_name} ---")
    while player_hp > 0 and enemy_hp > 0:
        print(f"\nSeu HP: {player_hp} | HP do {enemy_name}: {enemy_hp}")

        print("Sua vez de atacar!")
        enemy_hp -= player_atk
        print(f"Você causou {player_atk} de dano ao {enemy_name}!")
        if enemy_hp <= 0:
            print(f"Você derrotou o {enemy_name}!")
            break

        print(f"Vez do {enemy_name} atacar!")
        player_hp -= enemy_atk
        print(f"O {enemy_name} causou {enemy_atk} de dano a você!")
        if (player_hp <= 0):
            print("Você foi derrotado... Às vezes recuar é a melhor opção")
            break

    return player_hp, enemy_hp