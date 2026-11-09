class Zombie:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def bite(self, damage):
        self.hp -= damage
        return self.hp

butcher = Zombie("Мясник", 100)
bite_dmg = int(input("Введите силу укуса: "))
new_hp = butcher.bite(bite_dmg)
print(f"Остаток здоровья: {new_hp}")
