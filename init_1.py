print("Welcome to my init program.")

class Bike:
    def __init__(self, colour, frame_material, tire_size):
        self.colour = colour
        self.frame_material = frame_material
        self.tire_size = tire_size
        
    def brake(self):
        print("Braking!")

red_bike = Bike('Red', 'Carbon fiber', '14 inches')
blue_bike = Bike('Blue', 'Steel', '15 inches')

print(red_bike.colour)
print(red_bike.frame_material)
print(red_bike.tire_size)
print('\n')
print(blue_bike.colour)
print(blue_bike.frame_material)
print(blue_bike.tire_size)
print('\n')
red_bike.brake()
print('\n')
blue_bike.brake()
