#!/usr/bin/env python3

#info for marvelchars
marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

#main function 
def main():
    
    #Iterate through until user types in "Yes"
    while True:
        char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk\n>")
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy\n>")
    
        #format values 
        char_name = char_name.title()
        char_stat = char_stat.lower()
        value = marvelchars[char_name][char_stat]
    
        print(f"{char_name}'s {char_stat} is: {value.title()}")
        answer = input("Please enter \'Yes\' or \'No\' if you would like to continue\n>")
        answer = answer.title()
        
        if answer == "No": break

# Run this code
if __name__ == "__main__":
    main()
