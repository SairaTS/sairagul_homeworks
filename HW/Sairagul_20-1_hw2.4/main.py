from cars.get_car_info import get_car_info

first_car = get_car_info('BMW', 1500, 100, 1500, 150, 150, 'black')
print(first_car.info())
print(first_car.start_engine())
print(first_car.stop_engine())
