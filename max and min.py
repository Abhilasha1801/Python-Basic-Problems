def find_max_and_min(arr):
    if not arr:
        raise ValueError("Array must contain at least one element")
    
    max_num = arr[0]
    min_num = arr[0]
    
    for x in arr[1:]:
        if x > max_num:
            max_num = x
        if x < min_num:
            min_num = x
    
    return max_num, min_num

if __name__ == "__main__":
    arr = [2, 8, 1, 16, 5]
    max_val, min_val = find_max_and_min(arr)
    print(f"Max = {max_val}, Min = {min_val}")
