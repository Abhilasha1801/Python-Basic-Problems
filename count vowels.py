def count_vowels_and_consonants(s: str) -> (int, int):
    vowels = set("aeiouAEIOU")
    num_vowels = 0
    num_consonants = 0
    
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        # else: ignore non-alphabet characters
    
    return num_vowels, num_consonants

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    v, c = count_vowels_and_consonants(input_str)
    print(f"Vowels = {v}, Consonants = {c}")