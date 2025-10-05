# % means remainder
# Method 1 recursion for failed login attempts. (Not recommended for production code)
# If someone keeps entering wrong passwords many times, this can cause a stack overflow or crash in larger programs.

# username = "admin"
# password = "1234"

# fail_count = 0
# primes=[]

# def account_check():
#     global fail_count

#     username_input = input("Enter username: ")
#     password_input = input("Enter password: ")

#     if username_input == username and password_input == password:
#         number_input = int(input("Enter a number: "))
        
#         def check_prime(number_input):
#             for i in range(2, number_input):
#                 if number_input % i == 0:
#                     return False
#             return True
        
#         primes.clear()
#         for num in range(2, number_input + 1):
#             if check_prime(num):
#                 primes.append(num)

#         print("Prime numbers between 2 and", number_input, "are:", primes)
#         return
#     else:
#         fail_count += 1
#         if fail_count == 3:
#             print("Account locked")
#             quit()
#         else:
#             print("Incorrect username or password. Try again.")
#             account_check()


# account_check()

# ----------------------------------------------------------------------------------------------

# Method 2 using a loop for failed login attempts. (Recommended for production code) No recursion.

username = "admin"
password = "1234"

primes=[]
fail_count = 0

while fail_count < 3:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    if username_input == username and password_input == password:
        number_input = int(input("Enter a number: "))
        
        def check_prime(number_input):
            for i in range(2, number_input):
                if number_input % i == 0:
                    return False
            return True
        
        # Declare the function outside for memory purposes 

        # primes.clear()
        # number_input + 1 (to include the number itself if it's prime)
        for num in range(2, number_input + 1):
            #if the number is prime, add it to the list of primes
            if check_prime(num):
                primes.append(num)

        print("Prime numbers between 2 and", number_input, "are:", primes)
        break
    else:
        fail_count += 1
        if fail_count == 3:
            print("Account locked")
            quit()
        else:
            print("Incorrect username or password. Try again.")