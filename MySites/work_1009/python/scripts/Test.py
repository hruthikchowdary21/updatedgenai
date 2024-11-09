def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_between(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

# Get input from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Count and display the number of prime numbers
result = count_primes_between(start, end)
print(f"The number of prime numbers between {start} and {end} is: {result}")
