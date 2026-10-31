
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def factorial(n):
    if n < 0:
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))


def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)
    return n >= 0 and total == n


while True:
    print("\n===== NUMBER UTILITY TOOLKIT =====")
    print("1. Even or Odd")
    print("2. Prime Number")
    print("3. Factorial")
    print("4. Reverse Number")
    print("5. Palindrome Check")
    print("6. Sum of Digits")
    print("7. Armstrong Number")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "8":
        print("Thank you!")
        break

    if choice not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Invalid choice!")
        continue

    try:
        n = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if choice == "1":
        if n % 2 == 0:
            print(n, "is Even")
        else:
            print(n, "is Odd")

    elif choice == "2":
        print(n, "is Prime" if is_prime(n)
              else "is not Prime")

    elif choice == "3":
        result = factorial(n)
        if result is None:
            print("Factorial is not defined for negative integers.")
        else:
            print("Factorial =", result)

    elif choice == "4":
        print("Reversed number =", reverse_number(n))

    elif choice == "5":
        print("Palindrome" if is_palindrome(n)
              else "Not a palindrome")

    elif choice == "6":
        print("Sum of digits =", digit_sum(n))

    elif choice == "7":
        print("Armstrong number" if is_armstrong(n)
              else "Not an Armstrong number")
