# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/11/2022
# Description: A function named find_median that takes as a parameter a list of numbers.
def find_median(numbers):
    numbers.sort()
    if(len(numbers) %2 == 1):
        return numbers[len(numbers)//2]
    else:
        return (numbers[len(numbers) // 2-1] + numbers[len(numbers) // 2])/2