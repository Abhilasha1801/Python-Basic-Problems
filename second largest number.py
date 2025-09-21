def second_largest(nums):
    if len(nums) < 2:
        return None  # Or raise an error, since there's no “second largest”

    largest = None
    second_largest = None

    for x in nums:
        # Initialize
        if largest is None or x > largest:
            # Found new largest => old largest becomes second
            if largest != x:  # To avoid duplicates
                second_largest = largest
            largest = x
        elif x != largest:
            # x is less than largest; check if it's bigger than current second_largest
            if (second_largest is None) or (x > second_largest):
                second_largest = x

    return second_largest

if __name__ == "__main__":
    arr = [10, 20, 4, 45, 99]
    result = second_largest(arr)
    print("Second largest is:", result)  # Output: 45
