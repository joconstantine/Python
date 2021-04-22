from data import people, plants_list, plants_dict

# people = []

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

# print([plants_dict[plant].plant_type for plant in plants_dict])
if any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
    print("This dict contains grass")
else:
    print("No grasses in this dict")

if any([plants_dict[key].plant_type == "Cactus" for key in plants_dict]):
    print("This dict contains cactus")
else:
    print("No cacti in this dict")
