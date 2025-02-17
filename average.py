numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

average = sum(numbers) / len(numbers)
largest = max(numbers)
smallest = min(numbers)

print("Average: {average}")
print("Largest number: {largest}")
print("Smallest number: {smalest}")
