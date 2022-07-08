class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'{self.title}, {self.model} engine started')

    def stop_engine(self):
        print(f'{self.title}, {self.model} engine stoped\n')

    def info(self):
        print(f"All info: \nTitle: {self.title} \nModel: {self.model} \nWeight: {self.weight} \nHorsepower: {self.hp} \nNewton-meters: {self.nm} \nMax speed: {self.max_speed} \nColor: {self.color} ")

bmw = Car('BMW', 1500, 100, 1500, 150, 150, 'black')
bmw.start_engine()
bmw.stop_engine()
bmw.info()

print()
hyundai = Car('hyundai', 'Santa fe', 2500, 185, 0, 185, 'white')
hyundai.start_engine()
hyundai.stop_engine()
hyundai.info()



