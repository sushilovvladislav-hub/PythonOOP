class Monster:
    def __init__(self, name="Неизвестная тварь", hp=100, dmg=10):
        self.name = name
        self.hp = hp
        self.dmg = dmg

        print(f"Монстр: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")
        print()

m1_atr = input().split()
m1 = Monster(m1_atr[0], int(m1_atr[1]), int(m1_atr[2]))

m2_atr = input().split()
m2 = Monster(m2_atr[0], int(m2_atr[1]), int(m2_atr[2]))
