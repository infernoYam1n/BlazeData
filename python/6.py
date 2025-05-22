def main():
    print("Python Concepts Demonstration\n")
    
    # ----- Basic User Input -----
    name = input("What's your name? ")
    print(f"Hello, {name}! Let's explore Python concepts.")
    
    # Try-except for error handling with input
    try:
        age = int(input("Enter your age: "))
        print(f"In 10 years, you'll be {age + 10} years old.")
    except ValueError:
        print("That's not a valid age!")
    
    # ----- Conditional Statements -----
    print("\n----- CONDITIONALS -----")
    
    # Simple if-elif-else
    score = input("Enter a test score (0-100): ")
    try:
        score = int(score)
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid score!")
    
    # ----- Loops -----
    print("\n----- LOOPS -----")
    
    # For loop with range
    print("Counting with for loop:")
    for i in range(1, 6):
        print(i, end=" ")
    print()
    
    # While loop with break
    print("\nWhile loop with break:")
    counter = 0
    while True:
        counter += 1
        print(counter, end=" ")
        if counter >= 5:
            break
    print()
    
    # For loop with list comprehension
    print("\nList comprehension:")
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")
    
    # ----- Data Structures -----
    print("\n----- DATA STRUCTURES -----")
    
    # Lists
    fruits = ["apple", "banana", "cherry"]
    print(f"List: {fruits}")
    fruits.append("dragonfruit")
    print(f"After append: {fruits}")
    
    # Dictionary
    person = {
        "name": name,
        "location": input("\nWhere are you from? "),
        "languages": ["Python", "JavaScript"]
    }
    print(f"Dictionary: {person}")
    
    # Sets
    colors = {"red", "green", "blue", "red"}  # Duplicates are removed
    print(f"Set (no duplicates): {colors}")
    
    # ----- Advanced Concepts -----
    print("\n----- ADVANCED CONCEPTS -----")
    
    # Functions with default parameters and docstrings
    def calculate_total(items, tax_rate=0.1):
        """
        Calculate total price including tax.
        
        Args:
            items (list): List of prices
            tax_rate (float): Tax rate as decimal
        
        Returns:
            float: Total price with tax
        """
        subtotal = sum(items)
        return subtotal * (1 + tax_rate)
    
    # Lambda function
    print("Lambda function:")
    double = lambda x: x * 2
    print(f"Double 5: {double(5)}")
    
    # Map and filter
    print("\nMap and filter:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Map
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squared: {squared}")
    
    # Filter
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # List comprehension equivalents
    squared_comp = [x**2 for x in numbers]
    evens_comp = [x for x in numbers if x % 2 == 0]
    
    # ----- Classes -----
    print("\n----- CLASSES -----")
    
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance
            
        def deposit(self, amount):
            self.balance += amount
            return self.balance
            
        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient funds!")
                return False
            self.balance -= amount
            return self.balance
            
        def __str__(self):
            return f"{self.owner}'s account. Balance: ${self.balance}"
    
    # Create and use a class instance
    account = BankAccount(name, 100)
    print(account)
    account.deposit(50)
    print(f"After deposit: {account}")
    account.withdraw(25)
    print(f"After withdrawal: {account}")
    
    # ----- Context Managers -----
    print("\n----- CONTEXT MANAGERS -----")
    
    try:
        filename = "sample_file.txt"
        with open(filename, "w") as f:
            f.write(f"Hello, {name}!\n")
            f.write("This file was created by a Python program.")
        print(f"Successfully wrote to {filename}")
        
        print("\nReading from file:")
        with open(filename, "r") as f:
            content = f.read()
            print(content)
    except IOError as e:
        print(f"File error: {e}")
    
    print("\nThank you for exploring Python concepts!")

if __name__ == "__main__":
    main()