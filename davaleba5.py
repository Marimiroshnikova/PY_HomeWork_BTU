# დავალება 5
#
# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
# 2. დაამატე ერთი სტატიკური მეთოდი.
# 3. დაამატე ორი კლასის მეთოდი.
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის პარამეტრი.
# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
# 6. დაამატე __repr__ magic მეთოდი
# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.


# class Transport:
#     max_speed = 0
#     capacity = 0
#     color = ""
#     category = ""
#
#     def __init__(self, name, manufacturer, year, color):
#         self.name = name
#         self.manufacturer = manufacturer
#         self.year = year
#         self.color = color
#
#     @staticmethod
#     def light_color(color):
#         return color.lower() == "green"
#
#     @classmethod
#     def set_max_speed(cls, speed):
#         cls.max_speed = speed
#
#     @classmethod
#     def set_capacity(cls, capacity):
#         cls.capacity = capacity
#
#     def move(self):
#         return f"{self.name} is moving."
#
#     def wash(self):
#         return f"{self.name} is being washed."
#
#     def __repr__(self):
#         return (f"{self.name} manufactured by {self.manufacturer}, {self.year} Color: {self.color}")
#
#
# car = Transport("Tesla Model S", "Tesla", 2023, "Red")
# bus = Transport("MAN Bus", "MAN", 2024, "Blue")
# bike = Transport("Biks R1", "Biks", 2019, "Green")
# plane = Transport("Boeing 941", "Boeing", 2017, "White")
# train = Transport("Kukushka", "GR", 1960, "Red")
#
# Transport.set_max_speed(280)
# Transport.set_capacity(300)
#
# print(car.move())
# print(bike.wash())
# print(plane)
# print(f"Max speed set for all transports: {Transport.max_speed}")
# print(f"Capacity set for all transports: {Transport.capacity}")
