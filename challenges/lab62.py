farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

farm_names = []
farm_names_message = ""

# Get farm farm names
for farm in farms:
    farm_names.append(farm["name"]) 
    farm_names_message += farm["name"] + ", "
farm_names_message = farm_names_message[:-2]
    

answer = input(f"choose a farm ({farm_names_message})\n>").lower()

# Print animals
for farm in farms:
    if farm["name"].lower() == answer:
        print(farm["agriculture"])
        break
