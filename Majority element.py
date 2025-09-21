def majority_element(nums):
    # Phase 1: find a candidate
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    # Phase 2 (optional if you know majority always exists): verify
    # This ensures the found candidate actually appears > n/2 times
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None  # or raise an error, or some “no majority” indicator

if __name__ == "__main__":
    arr = [3,3,4,2,3,3,5]
    result = majority_element(arr)
    if result is not None:
        print("Majority element is:", result)
    else:
        print("No majority element exists")
