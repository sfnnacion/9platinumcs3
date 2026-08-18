# ACTIVITY 3: IMPLEMENTING SELECTION STRUCTURE - CHINESE ZODIAC SIGNS

# REQUIREMENTS
- Ask the user to enter their birth year with a baseline year of 1900.
- Validate the user input to ensure it is not earlier than 1900
- Display an appropriate error message and stop the program if an invalid year is entered.
- Determine the correct Chinese Zodiac Sign based on a 12-year repeating cycle.

## SOURCE CODE 
def main():
    baseline_year = 1900
    zodiac = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    try:
        birth_year = int(input("Enter your birth year: "))
    except ValueError:
        print("Invalid input. Enter a valid integer year.")
        return

    if birth_year < baseline_year:
        print("Invalid year, it should not be earlier than 1900")
        return

    index = (birth_year - baseline_year) % 12
    zodiac = zodiac[index]

    print(f"Your Chinese Zodiac Sign is: {zodiac}")

if __name__ == "__main__":
    main()