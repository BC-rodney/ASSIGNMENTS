my_numbers = []
total = 0
average = 0
for place in range(20):
    number = int(input(f"Enter number {place + 1}: "))
    my_numbers.append(number)
    total += number

print(my_numbers)

print(f"Total = {total}")
average = total/20
print(f"Average = {average}")



