# These functions have been generated with the help of ChatGPT

def reduce_to_single_digit(num):
    # Reduce to single digit or master number
    while num > 9 and num not in [11, 22, 33]:
        num = sum(int(digit) for digit in str(num))
    return num

def calculate_life_path_number(dob):
    # Extract day, month, and year
    year = dob.year
    month = dob.month
    day = dob.day

    # Sum all digits of the date
    total_sum = sum(int(digit) for digit in f"{year}{month}{day}")

    # Reduce to a single digit or master number
    return reduce_to_single_digit(total_sum)

def calculate_destiny_number(full_name):
    # The Destiny Number in numerology is derived from a person’s full name at birth.

    # Pythagorean numerology chart
    numerology_chart = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }

    # Remove spaces and convert to uppercase
    full_name = full_name.replace(" ", "").upper()

    # Convert each letter to its numerical value
    letter_values = [
        numerology_chart[char] for char in full_name if char in numerology_chart
    ]

    # Sum all values
    total = sum(letter_values)

    destiny_number = reduce_to_single_digit(total)

    return destiny_number



