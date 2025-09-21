def is_only_digits(s: str) -> bool:
    return s.isdigit()

if __name__ == "__main__":
    inp = input("Enter a string: ")
    if is_only_digits(inp):
        print("Yes")
    else:
        print("No")
