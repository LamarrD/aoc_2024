# Write a helper to get the input from Advent of Code's website
import requests
import os

def get_input_from_aoc():
    day = input("Enter the day: ")
    url = f"https://adventofcode.com/2024/day/{day}/input"
    cookie = os.getenv("AOC_COOKIE")
    aoc_input = requests.get(url, cookies={"session": cookie})

    # Create a new folder for each day if it doesn't exist
    if not os.path.exists(f"day{day}"):
        os.makedirs(f"day{day}")

    with open(f"day{day}/input.txt", "w") as f:
        f.write(aoc_input.text)
    
    print(f"Input for day {day} saved in day{day}/input.txt")
