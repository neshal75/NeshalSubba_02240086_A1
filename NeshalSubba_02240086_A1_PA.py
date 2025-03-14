def prime_sum(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_sum_range(start, end):
    return sum(i for i in range(start, end + 1) if prime_sum(i))




def length_converter(value, direction): # function 2
    if direction.upper() == 'M':
        return round(value * 3.28084, 2)  # Meters to Feet
    elif direction.upper() == 'F':
        return round(value / 3.28084, 2)  # Feet to Meters
    else:
            raise ValueError("Wrong input. Use 'M' to convert meters to feet or 'F' to convert feet to meters.")


def consonant_counter(text): # function 3
    """Count the number of consonants in a given string."""
    consonants = sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')
    return consonants

def Maximum_Minimun_finder(numbers): # function 4
  
    """Find the smallest and largest numbers from a list of numbers."""
    if not numbers:
        raise ValueError(" The number is not given.")
    return min(numbers), max(numbers)


def palindrome(text): # function 5
    """Check if a string is a palindrome, ignoring spaces and case."""
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def word_counter(Filename):# function 6

    word_list = ["the", "was", "and"]
    word_count = {word: 0 for word in word_list}

    try:
        with open(Filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            for word in word_list:
                word_count[word] = text.split().count(word)
    except FileNotFoundError:
        print("File not found.")
        return None
    return word_count
def main():
    while True:
        print("\nMenu: ")
        print("Select an option below:")
        print("1. Prime number sum calculator")
        print("2. Length unit converter")
        print("3. Consonant counter")
        print("4. Min-Max number finder")
        print("5. Palindrome checker")
        print("6. word counter")
        print("7. exit")
        select = input("Enter your number from (1-7): ")

        if select == '1':
            start = int(input("Enter your starting number: "))
            end = int(input("Enter your ending number: "))
            result = prime_sum_range(start, end)
            print(f" The sum of the number between {start} to {end}: {result}")

        elif select == '2':
            value = float(input("Enter your number: "))
            direction = input("Enter 'M' to convert meters to feet or 'F' to convert feet to meters.: ")
            result = length_converter(value, direction)
            print(f" Your Converted length is: {result}")

        elif select == '3':
            text = input(" Enter your text: ")
            result = consonant_counter(text)
            print(f"Number of consonants in your text is: {result}")

        elif select == '4':
            numbers = list(map(int, input("Enter numbers separated by space: ").split()))
            smallest, largest = Maximum_Minimun_finder(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")

        elif select == '5':
            text = input("Enter a text string: ")
            result = palindrome(text)
            print(f" The string of palindrome is {result}")

        elif select == '6':
            filename = input("Enter ypur file to analyze: ")
            result = word_counter(filename)
            if result:
                    for word, count in result.items():
                        print(f"{word}: {count}") 

        elif select == '7':
            print("Exit the system.")
            break

        else:
            print(" You have selceted the number which not in the option above.")

        try_again = input("\nWould you like to try another function? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Exiting the system.")
            break
            
if __name__ == "__main__":
    main()