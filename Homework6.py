#Работа со словарями
#Персонажи StarWars и их возраст
my_dict = {"Anakin Skywalker": 23, "Darth Vader": 60}
print(my_dict)
print(my_dict.get("Anakin Skywalker"))
print(my_dict.get("Obi-Wan Kenobi"))
my_dict = {"Anakin Skywalker": 23, "Darth Vader": 60, "Yoda": 666, "Chubaka": 35}
print(my_dict)
print(my_dict.pop("Darth Vader"))
print(my_dict)