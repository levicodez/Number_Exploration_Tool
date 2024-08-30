name = input("Enter your name: ")
print(f"Hello, {name}! Let's explore your favorite numbers:")

numbers = []
numbers.append(int(input("Enter your first favorite number: ")))
numbers.append(int(input("Enter your second favorite number: ")))
numbers.append(int(input("Enter your third favorite number: ")))

even_odd_list = []
for num in numbers:
    if num % 2 == 0:
        even_odd_list.append((num, "even"))
    else:
        even_odd_list.append((num, "odd"))

for num, status in even_odd_list:
    print(f"The number {num} is {status}.")

print("\nHere's your favorite numbers and their squares:")
for num in numbers:
    print(f"The number {num} and its square: ({num}, {num**2})")

sum_of_numbers = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {sum_of_numbers}")

is_prime = True
if sum_of_numbers <= 1:
    is_prime = False
else:
    for i in range(2, int(sum_of_numbers**0.5) + 1):
        if sum_of_numbers % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Wow, {sum_of_numbers} is a prime number!")
else:
    print(f"{sum_of_numbers} is not a prime number, but it's still special!")
