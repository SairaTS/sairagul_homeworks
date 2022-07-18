class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def info(self):
        print(f"All info: \nTitle: {self.title} \nModel: {self.model} \nWeight: {self.weight} \nHorsepower: {self.hp} \nNewton-meters: {self.nm} \nMax speed: {self.max_speed} \nColor: {self.color} ")

    def start_engine(self):
        return f'{self.title}, {self.model} engine started'

    def stop_engine(self):
        return f'{self.title}, {self.model} engine stoped\n'
