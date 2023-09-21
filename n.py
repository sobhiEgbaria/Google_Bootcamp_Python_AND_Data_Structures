def subArrayExists(arr, n):
    for i in range(n):
        # Starting point of the subarray and
        # sum is initialized with the first element of subarray
        sum = arr[i]
        if sum == 0:
            return True
        for j in range(i + 1, n):
            # We are finding the sum till the jth index
            # starting from the ith index
            sum += arr[j]
            if sum == 0:
                return True
    return False


# Driver's code
if __name__ == "__main__":
    arr = [1, 2, 3, -1, -1, -2, 1, 7, 8, 9]
    N = len(arr)

    # Function call
    if subArrayExists(arr, N):
        print("Found a subarray with 0 sum")
    else:
        print("No Such Sub Array Exists!")
