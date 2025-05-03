import random
import keyboard

nums = list(range(1, 76))  # list of integers from 1 to 75
random.shuffle(nums)  # Shuffle the list of numbers

# Print them out one at a time
for _ in range(0, 75):
    if nums[_] <= 15:
        print("B {}".format(nums[_]))
    elif 16 <= nums[_] <= 30:
        print("I {}".format(nums[_]))
    elif 31 <= nums[_] <= 45:
        print("N {}".format(nums[_]))
    elif 46 <= nums[_] <= 60:
        print("G {}".format(nums[_]))
    elif 61 <= nums[_] <= 75:
        print("O {}".format(nums[_]))
    # time.sleep(1)
    keyboard.wait('space')
    print('Next Letter...')

print(nums)  # Tally of all numbers in the order they were called
