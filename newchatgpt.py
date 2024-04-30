
# Take a list of numbers as input
numbers_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, numbers_input.split()))

# Take the partition number
partition_number = int(input("Enter the partition number: "))

# Partition the list into sublists of the given size
sublists = []
for i in range(0, len(numbers), partition_number):
    sublist = numbers[i:i+partition_number]
    sublists.append(sublist)

# Find the largest number in each sublist and print it
for sublist in sublists:
    if sublist:
        print("Largest number in sublist:", max(sublist))
