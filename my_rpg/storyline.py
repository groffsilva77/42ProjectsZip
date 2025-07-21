class story:
    def __init__(self):
        self.player_name = None
        self.player_occup = None
        self.warrior_occup = "Guerreiro"
        self.mage_occup = "Mago"
        self.cleric_occup = "Clérigo"
        self.land_name = "Earhardt"

    def display_text_from_file(self, file_path):
        """
            Esse método tem o objetivo de ler e exibir o conteúdo de um arquivo.

            Args:
                file_path (str): É o caminho para o arquivo de texto a ser lido.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"Erro: O arquivo de história '{file_path}' não foi encontrado. Verifique o caminho.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao ler o arquivo '{file_path}': {e}")
    
    def introduce_game(self):
        self.display_text_from_file("historia/intro_samantha.txt")
        print("Antes de tudo, como você se chama?")
        self.player_name = input("Digite o seu nome: ")
        try:
            with open("historia/intro_player.txt", 'r', encoding='utf-8') as file:
                content = file.read()
                print(content.format(player_name=self.player_name, land_name=self.land_name))
        except FileNotFoundError:
            print(f"Certo, prazer em te conhecer {self.player_name}. Enfim, vamos ao que interessa, onde você irá desembarcar: {self.land_name}!")
        except Exception as e:
            print(f"Erro ao ler intro_player.txt: {e}")
            print(f"Certo, prazer em te conhecer {self.player_name}. Enfim, vamos ao que interessa, onde você irá desembarcar: {self.land_name}!")

    def choose_occup(self):
        occup_op = {
            'a': self.warrior_occup,
            'b': self.mage_occup,
            'c': self.cleric_occup
        }

        escolha_valida = False
        while not escolha_valida:
            print(f"As opções de escolha de classe são: 'a', 'b' e 'c'. Isso para '{self.warrior_occup}',\n'{self.mage_occup}' e '{self.cleric_occup}', respectivamente.")
            escolha_raw = input("Digite a letra da sua escolha: ").lower()
            if escolha_raw in occup_op:
                self.player_occup = occup_op[escolha_raw]
                print(f"Você escolheu a classe de {self.player_occup}!")
                escolha_valida = True
            else:
                print("Opção inválida. Por favor, digite 'a', 'b' ou 'c'.")
            
        return self.player_occup

        return (self.player_name)