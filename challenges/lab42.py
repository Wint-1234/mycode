#!/usr/bin/python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[-1]}!")

# Printing using trial
eyes = trial[2]["goggles"]
googles = trial[2]["eyes"]
nothing = trial[-1]
print(f"My {eyes}! The {googles} do {nothing}!")

# Printing using nightmare 
eyes2 = nightmare[0]["user"]["name"]["first"]
googles2 = nightmare[0]["kumquat"]
nothing2 = nightmare[0]["d"]
print(f"My {eyes2}! The {googles2} do {nothing2}!")
