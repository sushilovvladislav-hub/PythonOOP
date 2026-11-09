class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def show_info(self):
        print(self.name)
        print(f"❤️  : {self.hp}") # два пробела между эмодзи и двоеточием, чтобы не было наложения символов
        print(f"⚔️  : {self.dmg}")

gargoyle = Monster("Горгулья", 120, 18)
gargoyle.show_info()
