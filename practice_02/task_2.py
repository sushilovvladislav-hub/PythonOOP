class Monster:
    def __init__(self, name):
        self.name = name

    # Ошибка: вместо ссылки на экземпляр (self) был указан обычный аргумент
    # def introduce(name): 
        # print(f"Я {self.name}, и я хочу кушать!")
    
    def introduce(self): 
        print(f"Я {self.name}, и я хочу кушать!")

m = Monster("Упырь")
m.introduce()
