#!/usr/bin/python3

import requests
import pprint

URL = "https://www.anapioficeandfire.com/api/characters/"

# get list of books character appears in
def get_list_books_for_char(got_list):
    house_names = []  
    for entry in got_list:
        got_json_obj = requests.get(entry).json() 
        house_names.append(got_json_obj.get("name"))  
    return house_names 

def main():
        ## Ask user for input and get JSON info from API
        got_char = input("Pick a number between 1 and 1000 to return info on a GoT character!\n\t>" )
        got_response = requests.get(URL + got_char).json()

        print("\nThis character belongs to the following houses:")
        for entry in get_list_books_for_char(got_response.get("allegiances")):
            print(f"\t{entry}")

        print("This character appears in the following books:")
        for entry in get_list_books_for_char(got_response.get("books")):
            print(f"\t{entry}")

if __name__ == "__main__":
    main()
