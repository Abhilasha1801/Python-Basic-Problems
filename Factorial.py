def factorial(n: int) -> int:
    """
    Returns the factorial of a non-negative integer n using recursion.
    If n < 0, raises ValueError.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Base case: 0! = 1, 1! = 1
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print("Error:", e)
