import re
def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_strings = [
        "racecar",
        "RaceCar",
        "A man, a plan, a canal, Panama!",
        "hello",
        "12321",
        "12345"
    ]
    for s in test_strings:
        print(f"\"{s}\" ->", "Yes" if is_palindrome(s) else "No")