def reverse_sentence(sentence: str) -> str:
    # Remove leading/trailing spaces (optional)
    sentence = sentence.strip()
    
    # Split into words
    words = sentence.split()
    
    # Reverse the list of words
    words_reversed = words[::-1]
    
    # Join back into a sentence
    reversed_sentence = " ".join(words_reversed)
    
    return reversed_sentence

if __name__ == "__main__":
    inp = input("Enter a sentence: ")
    out = reverse_sentence(inp)
    print("Reversed:", out)
