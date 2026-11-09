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

while m1.hp > 0 and m2.hp > 0:

    print(f"{m1.name} наносит удар!")
    m2.hp -= m1.dmg
    m2.hp = max(m2.hp, 0)
    print(f"У {m2.name} осталось {m2.hp} HP")

    if m2.hp == 0:
        break
    

    print(f"{m2.name} наносит удар!")
    m1.hp -= m2.dmg
    m1.hp = max(m1.hp, 0)
    print(f"У {m1.name} осталось {m1.hp} HP")


if m1.hp > 0:
    print(f"Победил {m1.name}")
else:
    print(f"Победил {m2.name}")
