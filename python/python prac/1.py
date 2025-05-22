# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 

# biggest_diff([10, 3, 5, 6]) → 7
# biggest_diff([7, 2, 10, 9]) → 8
# biggest_diff([2, 10, 7, 2]) → 8

def biggest_diff(nums):
    return max(nums) - min(nums)
def main():
    a = input("Enter numbers separated by spaces: ")
    
    try:
        nums = [int(x) for x in a.split()]
        
        if len(nums) < 1:
            print("Please enter at least one number.")
        else:
            # Calculate and display the result
            result = biggest_diff(nums)
            print(f"The largest difference is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by spaces.")

if __name__ == "__main__":
    main()


