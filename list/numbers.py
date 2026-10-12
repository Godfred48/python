numbers = []
print("Enter a list of numbers. Type 0 when finished")
while True:
    number = int(input("Enter number:"))
    if number == 0:
        break
    else:
        numbers.append(number)

print("")
sum = 0
for num in numbers:
    sum += num
print(f"The sum is {sum}")

average = sum / len(numbers)
print(f"The average is: {average}")

# largest = 0
# for num in numbers:
#     if num > largest:
#         largest = num
numbers.sort()
largest = numbers[-1] # picks up the last value 
print(f"The largest number is {largest}")

for i in numbers:
    if "-" in numbers:
        continue

print(f"The smallest positive number is:{i}")



