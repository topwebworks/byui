numbers = []
number = -1


print("Enter a list of numbers, type 0 when finished.")

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

sum = 0
largest = -1

for number in numbers:
    sum += number
    if largest < number:
        largest = number

average = sum / len(numbers)

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
