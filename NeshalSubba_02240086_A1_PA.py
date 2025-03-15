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
        """convert the feet to meter or meter to the feet """
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
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

import requests # function 6
"""help to count the word present in the sentence"""
def Word_count(text_file_url):
    response = requests.get(text_file_url)
    text = response.text.lower()
    wlist = ['was', 'and', 'the']
    word= {word: text.count(word) for word in wlist}
    return word
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
        """Displays a menu for various utilities and prompts user input."""

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
            Your_Url = input(" Insert your text's URL: ").strip()
            try:
                result = Word_count(Your_Url)
                print(f" Your word count is: {result}")
            except requests.exceptions.RequestException as e:
                print(f"invalid input, the error is detected: {e}")
            
        elif select == '7':
            print("Exit the system.")
            break
        
        else:
            print(" You have selceted the number which not in the option above.")

        try_again = input("\nWould you like to try another function? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Exiting the system.")
            break
        """Implements a menu-driven system offering various utilities like sum
        of prime numbers within a range, length conversion from meters to feet
         and vice versa, consonant counting from a text, finding the minimum and
        maximum of a set of numbers, checking palindromes, and word counting from
        a URL, while continuously asking for input from the user until the exit option
        is selected and offering exception handling wherever necessary"""
        
        
if __name__ == "__main__":
    main()
   

