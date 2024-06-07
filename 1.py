```python
# This program checks if a number is prime
 
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False  # 1 and numbers less than 1 are not prime
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False  # If n is divisible by any number from 2 to sqrt(n), it's not prime
    return True  # If no divisor found, n is prime
 
def get_user_input():
    """Get user input for a number"""
    return int(input("Enter a number: "))
 
def display_result(number, is_prime):
    """Display whether the number is prime or not"""
    if is_prime:
        print(number, "is prime.")
    else:
        print(number, "is not prime.")
 
def main():
    """Main function"""
    number = get_user_input()  # Get user input
    prime = is_prime(number)   # Check if the number is prime
    display_result(number, prime)  # Display the result
 
if __name__ == "__main__":
    main()
```
 
Explanation:
 
- **Short Functions**: Each function has a clear and concise purpose, making the code easier to read and understand.
 
- **Comments**:
  - `""" ... """`: Docstrings explain the purpose of each function.
  - Comments inside functions explain the logic or purpose of specific parts of the code.
 
- **Benefits of Short Functions**:
  - **Readability**: Functions are easier to read and comprehend.
  - **Modularity**: Functions can be reused and tested independently.
  - **Debugging**: Easier to pinpoint issues in smaller, focused functions.
  - **Maintainability**: Changes can be made to individual functions without affecting others.
 
Keeping functions short and focused improves code readability, maintainability, and makes it easier to collaborate with others.
