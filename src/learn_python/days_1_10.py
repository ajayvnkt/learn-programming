#!/usr/bin/env python3
"""
Python Learning Program - Days 1-10
A comprehensive 30-day Python learning journey with executable examples
"""

# =============================================================================
# DAY 1: Python Basics - Variables, Data Types, and Print Statements
# =============================================================================

def day1_basics():
    """Day 1: Introduction to Python basics"""
    print("=== DAY 1: Python Basics ===")
    
    # Variables and data types
    name = "Python Learner"  # String
    age = 25  # Integer
    height = 5.9  # Float
    is_student = True  # Boolean
    
    # Print statements with enhanced comments
    print(f"Hello, {name}!!")  # Expected: Hello, Python Learner!!
    print(f"Age: {age}, Height: {height}, Student: {is_student}")  # Expected: Age: 25, Height: 5.9, Student: True
    
    # Type checking - shows the data type of each variable
    print(f"Type of name: {type(name)}")  # Expected: Type of name: <class 'str'>
    print(f"Type of age: {type(age)}")  # Expected: Type of age: <class 'int'>
    print(f"Type of height: {type(height)}")  # Expected: Type of height: <class 'float'>
    print(f"Type of is_student: {type(is_student)}")  # Expected: Type of is_student: <class 'bool'>

# =============================================================================
# DAY 2: Numbers and Math Operations
# =============================================================================

def day2_numbers():
    """Day 2: Working with numbers and math operations"""
    print("\n=== DAY 2: Numbers and Math ===")
    
    # Basic arithmetic operations
    a = 10
    b = 3
    
    print(f"Addition: {a} + {b} = {a + b}")  # Expected: Addition: 10 + 3 = 13
    print(f"Subtraction: {a} - {b} = {a - b}")  # Expected: Subtraction: 10 - 3 = 7
    print(f"Multiplication: {a} * {b} = {a * b}")  # Expected: Multiplication: 10 * 3 = 30
    print(f"Division: {a} / {b} = {a / b}")  # Expected: Division: 10 / 3 = 3.3333333333333335
    print(f"Floor Division: {a} // {b} = {a // b}")  # Expected: Floor Division: 10 // 3 = 3 (integer division)
    print(f"Modulus: {a} % {b} = {a % b}")  # Expected: Modulus: 10 % 3 = 1 (remainder)
    print(f"Exponentiation: {a} ** {b} = {a ** b}")  # Expected: Exponentiation: 10 ** 3 = 1000
    
    # Math functions - importing math module for advanced operations
    import math
    print(f"Square root of {a}: {math.sqrt(a)}")  # Expected: Square root of 10: 3.1622776601683795
    print(f"Absolute value of -{a}: {abs(-a)}")  # Expected: Absolute value of -10: 10
    print(f"Round 3.7: {round(3.7)}")  # Expected: Round 3.7: 4
# =============================================================================
# DAY 3: Strings and String Methods
# =============================================================================

def day3_strings():
    """Day 3: String manipulation and methods"""
    print("\n=== DAY 3: Strings ===")
    
    # String creation
    greeting = "Hello, World!"
    name = "Python"
    
    # String methods - demonstrates various string operations
    print(f"Original: {greeting}")  # Expected: Original: Hello, World!
    print(f"Uppercase: {greeting.upper()}")  # Expected: Uppercase: HELLO, WORLD!
    print(f"Lowercase: {greeting.lower()}")  # Expected: Lowercase: hello, world!
    print(f"Title case: {greeting.title()}")  # Expected: Title case: Hello, World!
    print(f"Length: {len(greeting)}")  # Expected: Length: 13
    print(f"Replace: {greeting.replace('World', name)}")  # Expected: Replace: Hello, Python!
    print(f"Split: {greeting.split(', ')}")  # Expected: Split: ['Hello', 'World!']
    
    # String formatting - three different ways to format strings
    print(f"f-string: Hello, {name}!")  # Expected: f-string: Hello, Python!
    print("format(): Hello, {}!".format(name))  # Expected: format(): Hello, Python!
    print("Old style: Hello, %s!" % name)  # Expected: Old style: Hello, Python!
    
    # String slicing - extracting parts of strings using indices
    print(f"First 5 characters: {greeting[:5]}")  # Expected: First 5 characters: Hello
    print(f"Last 6 characters: {greeting[-6:]}")  # Expected: Last 6 characters: World!
    print(f"Characters 2-5: {greeting[2:5]}")  # Expected: Characters 2-5: llo

# =============================================================================
# DAY 4: Lists and List Methods
# =============================================================================

def day4_lists():
    """Day 4: Working with lists"""
    print("\n=== DAY 4: Lists ===")
    
    # Creating lists - different types of lists
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "orange"]
    mixed = [1, "hello", 3.14, True]
    
    print(f"Numbers: {numbers}")  # Expected: Numbers: [1, 2, 3, 4, 5]
    print(f"Fruits: {fruits}")  # Expected: Fruits: ['apple', 'banana', 'orange']
    print(f"Mixed: {mixed}")  # Expected: Mixed: [1, 'hello', 3.14, True]
    
    # List methods - modifying lists in place
    numbers.append(6)  # Add to end
    print(f"After append(6): {numbers}")  # Expected: After append(6): [1, 2, 3, 4, 5, 6]
    
    numbers.insert(0, 0)  # Insert at index
    print(f"After insert(0, 0): {numbers}")  # Expected: After insert(0, 0): [0, 1, 2, 3, 4, 5, 6]
    
    numbers.remove(3)  # Remove first occurrence
    print(f"After remove(3): {numbers}")  # Expected: After remove(3): [0, 1, 2, 4, 5, 6]
    
    popped = numbers.pop()  # Remove and return last element
    print(f"Popped: {popped}, List: {numbers}")  # Expected: Popped: 6, List: [0, 1, 2, 4, 5]
    
    # List slicing - extracting parts of lists
    print(f"First 3: {numbers[:3]}")  # Expected: First 3: [0, 1, 2]
    print(f"Last 2: {numbers[-2:]}")  # Expected: Last 2: [4, 5]
    print(f"Every 2nd: {numbers[::2]}")  # Expected: Every 2nd: [0, 2, 4]
    
    # List comprehension - creating new lists from existing ones
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")  # Expected: Squares: [1, 4, 9, 16, 25]

# =============================================================================
# DAY 5: Tuples and Sets
# =============================================================================

def day5_tuples_sets():
    """Day 5: Tuples and Sets"""
    print("\n=== DAY 5: Tuples and Sets ===")
    
    # Tuples (immutable) - cannot be changed after creation
    coordinates = (3, 4)
    person = ("Alice", 25, "Engineer")
    
    print(f"Coordinates: {coordinates}")  # Expected: Coordinates: (3, 4)
    print(f"Person: {person}")  # Expected: Person: ('Alice', 25, 'Engineer')
    print(f"X coordinate: {coordinates[0]}")  # Expected: X coordinate: 3
    print(f"Name: {person[0]}")  # Expected: Name: Alice
    
    # Tuple unpacking - assigning tuple elements to variables
    x, y = coordinates
    name, age, job = person
    print(f"Unpacked: x={x}, y={y}")  # Expected: Unpacked: x=3, y=4
    print(f"Unpacked: name={name}, age={age}, job={job}")  # Expected: Unpacked: name=Alice, age=25, job=Engineer
    
    # Sets (unique elements) - automatically removes duplicates
    numbers = {1, 2, 3, 4, 5, 5, 4}  # Duplicates removed
    print(f"Set: {numbers}")  # Expected: Set: {1, 2, 3, 4, 5}
    
    # Set operations - mathematical set operations
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    
    print(f"Set1: {set1}")  # Expected: Set1: {1, 2, 3, 4}
    print(f"Set2: {set2}")  # Expected: Set2: {3, 4, 5, 6}
    print(f"Union: {set1 | set2}")  # Expected: Union: {1, 2, 3, 4, 5, 6} (all elements from both sets)
    print(f"Intersection: {set1 & set2}")  # Expected: Intersection: {3, 4} (common elements)
    print(f"Difference: {set1 - set2}")  # Expected: Difference: {1, 2} (elements in set1 but not set2)
    print(f"Symmetric difference: {set1 ^ set2}")  # Expected: Symmetric difference: {1, 2, 5, 6} (elements in either set but not both)

# =============================================================================
# DAY 6: Dictionaries
# =============================================================================

def day6_dictionaries():
    """Day 6: Working with dictionaries"""
    print("\n=== DAY 6: Dictionaries ===")
    
    # Creating dictionaries - key-value pairs
    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York",
        "occupation": "Engineer"
    }
    
    print(f"Person: {person}")  # Expected: Person: {'name': 'Alice', 'age': 25, 'city': 'New York', 'occupation': 'Engineer'}
    print(f"Name: {person['name']}")  # Expected: Name: Alice
    print(f"Age: {person.get('age', 'Unknown')}")  # Expected: Age: 25 (get() returns default if key not found)
    
    # Dictionary methods - accessing different parts of the dictionary
    print(f"Keys: {list(person.keys())}")  # Expected: Keys: ['name', 'age', 'city', 'occupation']
    print(f"Values: {list(person.values())}")  # Expected: Values: ['Alice', 25, 'New York', 'Engineer']
    print(f"Items: {list(person.items())}")  # Expected: Items: [('name', 'Alice'), ('age', 25), ('city', 'New York'), ('occupation', 'Engineer')]
    
    # Adding/updating - modifying dictionary contents
    person["email"] = "alice@example.com"
    person["age"] = 26
    print(f"Updated: {person}")  # Expected: Updated: {'name': 'Alice', 'age': 26, 'city': 'New York', 'occupation': 'Engineer', 'email': 'alice@example.com'}
    
    # Dictionary comprehension - creating new dictionaries from expressions
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"Squares dict: {squares_dict}")  # Expected: Squares dict: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# =============================================================================
# DAY 7: If Statements and Conditionals
# =============================================================================

def day7_conditionals():
    """Day 7: Conditional statements"""
    print("\n=== DAY 7: Conditionals ===")
    
    age = 20
    score = 85
    
    # Basic if-else - decision making based on conditions
    if age >= 18:
        print("You are an adult")  # Expected: You are an adult (since age=20 >= 18)
    else:
        print("You are a minor")
    
    # Multiple conditions - elif chain for multiple possibilities
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"  # This will execute since 85 >= 80
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Score: {score}, Grade: {grade}")  # Expected: Score: 85, Grade: B
    
    # Logical operators - combining conditions with and/or
    is_student = True
    has_id = True
    
    if is_student and has_id:
        print("Access granted")  # Expected: Access granted (both conditions are True)
    elif is_student or has_id:
        print("Partial access")
    else:
        print("Access denied")
    
    # Ternary operator - compact if-else in one line
    status = "Eligible" if age >= 18 else "Not eligible"
    print(f"Status: {status}")  # Expected: Status: Eligible

# =============================================================================
# DAY 8: For Loops
# =============================================================================

def day8_for_loops():
    """Day 8: For loops and iteration"""
    print("\n=== DAY 8: For Loops ===")
    
    # Basic for loop - iterating through a list
    fruits = ["apple", "banana", "orange"]
    print("Fruits:")  # Expected: Fruits:
    for fruit in fruits:
        print(f"  - {fruit}")  # Expected:   - apple\n  - banana\n  - orange
    
    # For loop with range - generating numbers in a sequence
    print("Numbers 1-5:")  # Expected: Numbers 1-5:
    for i in range(1, 6):
        print(f"  {i}")  # Expected:   1\n  2\n  3\n  4\n  5
    
    # For loop with enumerate - getting both index and value
    print("Fruits with index:")  # Expected: Fruits with index:
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")  # Expected:   0: apple\n  1: banana\n  2: orange
    
    # For loop with dictionary - iterating through key-value pairs
    person = {"name": "Alice", "age": 25, "city": "NYC"}
    print("Person details:")  # Expected: Person details:
    for key, value in person.items():
        print(f"  {key}: {value}")  # Expected:   name: Alice\n  age: 25\n  city: NYC
    
    # Nested loops - loop inside another loop
    print("Multiplication table (2x2):")  # Expected: Multiplication table (2x2):
    for i in range(1, 3):
        for j in range(1, 3):
            print(f"  {i} x {j} = {i * j}")  # Expected:   1 x 1 = 1\n  1 x 2 = 2\n  2 x 1 = 2\n  2 x 2 = 4
    
    n=3
    print("Multiplication table (1x3):")  # Expected: Multiplication table (1x3):
    for i in range(1, n):
            print(f"  {i} x {n} = {i * n}")
            n+=1

# =============================================================================
# DAY 9: While Loops
# =============================================================================

def day9_while_loops():
    """Day 9: While loops"""
    print("\n=== DAY 9: While Loops ===")
    
    # Basic while loop - repeats while condition is True
    count = 0
    print("Countdown:")  # Expected: Countdown:
    while count < 5:
        print(f"  Count: {count}")  # Expected:   Count: 0\n  Count: 1\n  Count: 2\n  Count: 3\n  Count: 4
        count += 1
    
    # While loop with condition - continues until condition becomes False
    number = 10
    print(f"Halving {number}:")  # Expected: Halving 10:
    while number > 1:
        print(f"  {number}")  # Expected:   10\n  5\n  2
        number = number // 2
    
    # While loop with break - exits loop when condition is met
    print("Finding first even number:")  # Expected: Finding first even number:
    numbers = [1, 3, 5, 6, 7, 9]
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            print(f"  Found even number: {numbers[index]} at index {index}")  # Expected:   Found even number: 6 at index 3
            break
        index += 1
    
    # While loop with continue - skips current iteration and continues
    print("Printing odd numbers 1-10:")  # Expected: Printing odd numbers 1-10:
    num = 1
    while num <= 10:
        if num % 2 == 0:
            num += 1
            continue  # Skip even numbers
        print(f"  {num}")  # Expected:   1\n  3\n  5\n  7\n  9
        num += 1

# =============================================================================
# DAY 10: Functions
# =============================================================================

def day10_functions():
    """Day 10: Functions and function parameters"""
    print("\n=== DAY 10: Functions ===")
    
    # Basic function - defining and calling a simple function
    def greet(name):
        return f"Hello, {name}!"
    
    print(greet("Alice"))  # Expected: Hello, Alice!
    
    # Function with multiple parameters - functions that take multiple arguments
    def add_numbers(a, b):
        return a + b
    
    print(f"5 + 3 = {add_numbers(5, 3)}")  # Expected: 5 + 3 = 8
    
    # Function with default parameters - parameters with default values
    def greet_with_title(name, title="Mr./Ms."):
        return f"Hello, {title} {name}!"
    
    print(greet_with_title("Smith"))  # Expected: Hello, Mr./Ms. Smith!
    print(greet_with_title("Johnson", "Dr."))  # Expected: Hello, Dr. Johnson!
    
    # Function with variable arguments - *args collects positional arguments
    def sum_all(*args):
        return sum(args)
    
    print(f"Sum of 1,2,3,4,5: {sum_all(1, 2, 3, 4, 5)}")  # Expected: Sum of 1,2,3,4,5: 15
    
    # Function with keyword arguments - **kwargs collects keyword arguments
    def create_person(**kwargs):
        return kwargs
    
    person = create_person(name="Alice", age=25, city="NYC")
    print(f"Person: {person}")  # Expected: Person: {'name': 'Alice', 'age': 25, 'city': 'NYC'}
    
    # Lambda functions - anonymous functions defined with lambda keyword
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")  # Expected: Square of 5: 25
    
    # Higher-order function - function that takes another function as argument
    def apply_operation(x, operation):
        return operation(x)
    
    result = apply_operation(3, lambda x: x * 2)
    print(f"Double of 3: {result}")  # Expected: Double of 3: 6

# =============================================================================
# COMPREHENSIVE PROBLEM: Student Grade Manager
# This problem uses ALL concepts from Days 1-10
# =============================================================================

def comprehensive_problem_student_grade_manager():
    """
    COMPREHENSIVE PROBLEM: Student Grade Manager
    
    This problem demonstrates all concepts learned in Days 1-10:
    - Day 1: Variables, Data Types, Print Statements
    - Day 2: Numbers and Math Operations
    - Day 3: Strings and String Methods
    - Day 4: Lists and List Methods
    - Day 5: Tuples and Sets
    - Day 6: Dictionaries
    - Day 7: If Statements and Conditionals
    - Day 8: For Loops
    - Day 9: While Loops
    - Day 10: Functions
    
    Problem: Create a system to manage student grades, calculate statistics,
    and generate reports.
    """
    print("\n" + "=" * 70)
    print("🎓 COMPREHENSIVE PROBLEM: Student Grade Manager")
    print("=" * 70)
    
    # Day 1 & 2: Variables, Data Types, Numbers, Math Operations
    school_name = "Python Learning Academy"  # String variable
    current_semester = 1  # Integer variable
    passing_grade = 60.0  # Float variable
    is_active = True  # Boolean variable
    
    print(f"\n📚 School: {school_name}")  # Day 1: Print statement with f-string
    print(f"📅 Semester: {current_semester}, Passing Grade: {passing_grade}%")
    print(f"Status: {'Active' if is_active else 'Inactive'}")
    
    # Day 3: Strings and String Methods
    def format_student_name(name):
        """Format student name using string methods"""
        formatted = name.strip().title()  # Remove spaces, title case
        return formatted
    
    # Day 4: Lists - Store student names and grades
    students = []  # List to store student dictionaries
    subject_names = ["Mathematics", "Science", "English", "History"]  # List of subjects
    
    # Day 6: Dictionaries - Store student information
    def add_student(name, student_id, grades):
        """
        Add a student with their grades
        Uses: Dictionaries, Lists, Functions
        """
        student = {
            "name": format_student_name(name),  # Day 3: String method
            "id": student_id,
            "grades": grades,  # List of grades
            "total_points": sum(grades),  # Day 2: Math - sum
            "average": round(sum(grades) / len(grades), 2),  # Day 2: Math operations
            "passed": True  # Will be updated based on condition
        }
        
        # Day 7: Conditionals - Check if student passed
        if student["average"] >= passing_grade:  # Day 7: If statement
            student["passed"] = True
            student["status"] = "Passed"
        else:
            student["passed"] = False
            student["status"] = "Failed"
        
        students.append(student)  # Day 4: List append method
        return student
    
    # Day 8: For Loops - Add multiple students
    print("\n📝 Adding Students:")
    student_data = [
        ("alice smith", "S001", [85, 92, 78, 88]),
        ("bob jones", "S002", [45, 52, 48, 50]),
        ("carol white", "S003", [95, 98, 92, 96]),
        ("david brown", "S004", [65, 70, 68, 72])
    ]
    
    for name, student_id, grades in student_data:  # Day 8: For loop with unpacking
        student = add_student(name, student_id, grades)
        print(f"  ✅ {student['name']} (ID: {student['id']}) - Average: {student['average']}% - {student['status']}")
    
    # Day 9: While Loops - Process students until we find all passing students
    print("\n🔍 Finding Passing Students:")
    passing_students = []
    index = 0
    while index < len(students):  # Day 9: While loop
        student = students[index]
        if student["passed"]:  # Day 7: Conditional
            passing_students.append(student["name"])
        index += 1
    
    print(f"  Passing Students ({len(passing_students)}): {', '.join(passing_students)}")
    
    # Day 5: Tuples and Sets - Calculate unique grade ranges
    print("\n📊 Grade Statistics:")
    
    # Day 5: Sets - Find unique grade ranges
    grade_ranges = set()  # Day 5: Set
    for student in students:  # Day 8: For loop
        avg = student["average"]
        if avg >= 90:
            grade_ranges.add("A (90-100)")  # Day 5: Set add
        elif avg >= 80:
            grade_ranges.add("B (80-89)")
        elif avg >= 70:
            grade_ranges.add("C (70-79)")
        elif avg >= 60:
            grade_ranges.add("D (60-69)")
        else:
            grade_ranges.add("F (Below 60)")
    
    print(f"  Grade Ranges Present: {sorted(grade_ranges)}")  # Day 4: List sorted
    
    # Day 2: Math Operations - Calculate class statistics
    def calculate_class_statistics():
        """Calculate overall class statistics"""
        if not students:  # Day 7: Conditional check
            return None
        
        all_averages = [student["average"] for student in students]  # Day 4: List comprehension
        
        # Day 2: Math Operations
        class_average = round(sum(all_averages) / len(all_averages), 2)
        highest_avg = max(all_averages)
        lowest_avg = min(all_averages)
        
        # Day 7: Conditionals - Determine class performance
        if class_average >= 80:
            performance = "Excellent"
        elif class_average >= 70:
            performance = "Good"
        elif class_average >= 60:
            performance = "Average"
        else:
            performance = "Needs Improvement"
        
        return {
            "class_average": class_average,
            "highest": highest_avg,
            "lowest": lowest_avg,
            "performance": performance,
            "total_students": len(students)  # Day 4: List length
        }
    
    stats = calculate_class_statistics()  # Day 10: Function call
    print(f"\n📈 Class Statistics:")
    print(f"  Total Students: {stats['total_students']}")
    print(f"  Class Average: {stats['class_average']}%")
    print(f"  Highest Average: {stats['highest']}%")
    print(f"  Lowest Average: {stats['lowest']}%")
    print(f"  Overall Performance: {stats['performance']}")
    
    # Day 6: Dictionary Methods - Generate detailed report
    print("\n📋 Detailed Student Report:")
    for student in students:  # Day 8: For loop
        print(f"\n  Student: {student['name']} (ID: {student['id']})")
        print(f"    Grades: {student['grades']}")  # Day 4: List
        
        # Day 8: For loop with enumerate
        for idx, grade in enumerate(student['grades']):  # Day 8: Enumerate
            subject = subject_names[idx]  # Day 4: List indexing
            letter_grade = "A" if grade >= 90 else "B" if grade >= 80 else "C" if grade >= 70 else "D" if grade >= 60 else "F"
            print(f"      {subject}: {grade}% ({letter_grade})")
        
        print(f"    Total Points: {student['total_points']}")
        print(f"    Average: {student['average']}%")
        print(f"    Status: {student['status']}")
    
    # Day 10: Functions with multiple features
    def find_top_students(limit=2):
        """Find top N students by average"""
        sorted_students = sorted(students, key=lambda x: x['average'], reverse=True)  # Day 10: Lambda
        return sorted_students[:limit]
    
    top_students = find_top_students(2)  # Day 10: Function call
    print(f"\n🏆 Top 2 Students:")
    for rank, student in enumerate(top_students, 1):  # Day 8: For loop with enumerate
        print(f"  {rank}. {student['name']}: {student['average']}%")
    
    print("\n" + "=" * 70)
    print("✅ Comprehensive Problem Complete!")
    print("=" * 70)

# =============================================================================
# COMPREHENSIVE PROBLEM 2: Library Book Management System
# Another complete example using all concepts from Days 1-10
# =============================================================================

def comprehensive_problem_library_books():
    """
    COMPREHENSIVE PROBLEM 2: Library Book Management System
    
    This is another complete example demonstrating all concepts from Days 1-10:
    - Day 1: Variables, Data Types, Print Statements
    - Day 2: Numbers and Math Operations
    - Day 3: Strings and String Methods
    - Day 4: Lists and List Methods
    - Day 5: Tuples and Sets
    - Day 6: Dictionaries
    - Day 7: If Statements and Conditionals
    - Day 8: For Loops
    - Day 9: While Loops
    - Day 10: Functions
    
    Problem: Create a library system to manage books, track checkouts,
    and generate reports.
    """
    print("\n" + "=" * 70)
    print("📚 COMPREHENSIVE PROBLEM 2: Library Book Management System")
    print("=" * 70)
    
    # Day 1: Variables and Data Types
    library_name = "Python City Library"  # String
    library_id = 1001  # Integer
    max_books_per_person = 5  # Integer
    late_fee_per_day = 0.50  # Float
    is_open = True  # Boolean
    
    print(f"\n🏛️  Library: {library_name} (ID: {library_id})")
    print(f"📋 Max Books: {max_books_per_person}, Late Fee: ${late_fee_per_day}/day")
    print(f"Status: {'Open' if is_open else 'Closed'}")
    
    # Day 4: Lists to store books and members
    books = []  # List of book dictionaries
    members = []  # List of member dictionaries
    
    # Day 3: String Methods - Format book titles
    def format_book_title(title):
        """Format book title using string methods"""
        return title.strip().title()  # Remove spaces, title case
    
    # Day 6: Dictionaries + Day 10: Functions
    def add_book(title, author, isbn, total_copies=1):
        """
        Add a book to library inventory
        Uses: Dictionaries, Lists, Functions, String Methods
        """
        book = {
            "title": format_book_title(title),  # Day 3: String methods
            "author": format_book_title(author),
            "isbn": str(isbn),  # Day 1: Type conversion
            "total_copies": total_copies,
            "available_copies": total_copies,
            "checked_out": 0  # Day 2: Numbers
        }
        books.append(book)  # Day 4: List append
        return book
    
    # Day 8: For Loops - Add multiple books
    print("\n📚 Adding Books to Library:")
    book_data = [
        ("python programming", "john smith", "978-1234567890", 3),
        ("data structures", "jane doe", "978-0987654321", 2),
        ("algorithms", "bob wilson", "978-1122334455", 4),
        ("machine learning", "alice brown", "978-5566778899", 2)
    ]
    
    for title, author, isbn, copies in book_data:  # Day 8: For loop with unpacking
        book = add_book(title, author, isbn, copies)
        print(f"  ✅ '{book['title']}' by {book['author']} - {book['available_copies']} copies available")
    
    # Day 6: Dictionaries - Member information
    def add_member(name, member_id):
        """Add a library member"""
        member = {
            "name": format_book_title(name),
            "id": member_id,
            "books_checked_out": [],  # Day 4: List
            "total_books": 0,
            "late_fees": 0.0  # Day 2: Float
        }
        members.append(member)
        return member
    
    # Day 8: For Loops - Add members
    print("\n👥 Adding Library Members:")
    member_data = [
        ("alice johnson", "M001"),
        ("david lee", "M002"),
        ("sarah kim", "M003")
    ]
    
    for name, member_id in member_data:  # Day 8: For loop
        member = add_member(name, member_id)
        print(f"  ✅ {member['name']} (ID: {member['id']})")
    
    # Day 7: Conditionals + Day 10: Functions - Checkout book
    def checkout_book(member_id, book_title):
        """Checkout a book for a member"""
        # Day 8: For loops - Find member
        member = None
        for m in members:
            if m["id"] == member_id:
                member = m
                break
        
        if not member:  # Day 7: Conditional
            return f"❌ Member {member_id} not found"
        
        # Day 8: For loops - Find book
        book = None
        for b in books:
            if b["title"].lower() == book_title.lower():  # Day 3: String method
                book = b
                break
        
        if not book:  # Day 7: Conditional
            return f"❌ Book '{book_title}' not found"
        
        # Day 7: Conditionals - Check availability
        if book["available_copies"] <= 0:
            return f"❌ '{book['title']}' is not available"
        
        if member["total_books"] >= max_books_per_person:  # Day 7: Conditional
            return f"❌ {member['name']} has reached the limit of {max_books_per_person} books"
        
        # Day 4: List methods - Add to checked out list
        from datetime import datetime  # For tracking dates
        checkout_record = {
            "book_title": book["title"],
            "isbn": book["isbn"],
            "checkout_date": datetime.now().strftime("%Y-%m-%d"),
            "due_date": "14 days"  # Simplified
        }
        
        member["books_checked_out"].append(checkout_record)  # Day 4: List append
        member["total_books"] += 1  # Day 2: Math operation
        book["available_copies"] -= 1  # Day 2: Math operation
        book["checked_out"] += 1
        
        return f"✅ {member['name']} checked out '{book['title']}'"
    
    # Day 9: While Loop - Process checkouts
    print("\n📖 Processing Book Checkouts:")
    checkout_queue = [
        ("M001", "Python Programming"),
        ("M002", "Data Structures"),
        ("M001", "Algorithms"),
        ("M003", "Machine Learning")
    ]
    
    queue_index = 0  # Day 1: Variable
    while queue_index < len(checkout_queue):  # Day 9: While loop
        member_id, book_title = checkout_queue[queue_index]
        result = checkout_book(member_id, book_title)
        print(f"  {result}")
        queue_index += 1  # Day 2: Increment
    
    # Day 5: Sets - Find unique authors
    print("\n✍️  Library Authors:")
    authors = set()  # Day 5: Set
    for book in books:  # Day 8: For loop
        authors.add(book["author"])  # Day 5: Set add
    
    for author in sorted(authors):  # Day 4: List sorted
        print(f"  • {author}")
    
    # Day 2: Math Operations - Calculate statistics
    def calculate_library_statistics():
        """Calculate library-wide statistics"""
        total_books = sum(book["total_copies"] for book in books)  # Day 2: Sum, Day 8: For loop
        total_checked_out = sum(book["checked_out"] for book in books)  # Day 2: Sum
        total_available = sum(book["available_copies"] for book in books)
        utilization_rate = (total_checked_out / total_books * 100) if total_books > 0 else 0  # Day 2: Math
        
        return {
            "total_books": total_books,
            "total_checked_out": total_checked_out,
            "total_available": total_available,
            "utilization_rate": round(utilization_rate, 2)  # Day 2: Round
        }
    
    stats = calculate_library_statistics()  # Day 10: Function call
    print(f"\n📊 Library Statistics:")
    print(f"  Total Books: {stats['total_books']}")
    print(f"  Checked Out: {stats['total_checked_out']}")
    print(f"  Available: {stats['total_available']}")
    print(f"  Utilization Rate: {stats['utilization_rate']}%")
    
    # Day 8: For Loops with enumerate - Generate detailed report
    print(f"\n📋 Detailed Member Report:")
    for idx, member in enumerate(members, 1):  # Day 8: Enumerate
        print(f"\n  {idx}. {member['name']} (ID: {member['id']})")
        print(f"     Books Checked Out: {member['total_books']}")
        
        if member['books_checked_out']:  # Day 7: Conditional
            for book_record in member['books_checked_out']:  # Day 8: Nested for loop
                print(f"       • {book_record['book_title']} (Due: {book_record['due_date']})")
        else:
            print(f"       (No books currently checked out)")
    
    # Day 10: Lambda Functions - Sort books by popularity
    print(f"\n🔥 Most Popular Books:")
    sorted_books = sorted(books, key=lambda x: x['checked_out'], reverse=True)  # Day 10: Lambda
    for rank, book in enumerate(sorted_books[:3], 1):  # Day 8: For loop, enumerate
        print(f"  {rank}. '{book['title']}' - {book['checked_out']} checkouts")
    
    print("\n" + "=" * 70)
    print("✅ Comprehensive Problem 2 Complete!")
    print("=" * 70)

# =============================================================================
# TODO PROBLEM: Simple Inventory Management System
# Implement this problem yourself to test your knowledge!
# =============================================================================

def todo_problem_inventory_management():
    """
    TODO PROBLEM: Simple Inventory Management System
    
    Your task: Implement an inventory management system that tracks products,
    their quantities, and prices. Use ALL concepts from Days 1-10.
    
    REQUIREMENTS:
    ------------
    1. Store Information (Day 1):
       - Create variables for: store_name (string), store_location (string),
         store_id (integer), is_open (boolean)
       - Print store information
    
    2. Product Management:
       - Create a list to store products (Day 4)
       - Each product should be a dictionary with: name, price, quantity (Day 6)
       - Use string methods to format product names (Day 3)
    
    3. Functions to Implement (Day 10):
       a) add_product(name, price, quantity)
          - Creates a product dictionary
          - Adds it to the products list
          - Returns success message
       
       b) update_quantity(name, new_quantity)
          - Finds product by name (use for loop - Day 8)
          - Updates quantity (use conditionals - Day 7)
          - Returns success/error message
       
       c) calculate_total_value()
          - Iterates through all products (Day 8: for loop)
          - Calculates: price * quantity for each (Day 2: math)
          - Returns total inventory value
       
       d) find_products_by_price_range(min_price, max_price)
          - Uses for loop to iterate products (Day 8)
          - Uses conditionals to check price range (Day 7)
          - Returns list of matching products
       
       e) generate_report()
          - Prints all products (Day 8: for loop)
          - Shows total value (Day 2: math)
          - Identifies low stock items (Day 7: conditionals)
          - Shows products sorted by price (Day 4: sorted)
    
    4. Testing:
       - Add these products:
         * "Laptop", $999.99, Quantity: 5
         * "Mouse", $19.99, Quantity: 50
         * "Keyboard", $49.99, Quantity: 8
         * "Monitor", $299.99, Quantity: 12
       - Update Mouse quantity to 45
       - Calculate and display total inventory value
       - Find products between $20 and $300
       - Generate complete report
    
    CONCEPTS TO USE:
    ---------------
    - Day 1: Variables, data types, print statements
    - Day 2: Math operations (multiplication, addition)
    - Day 3: String methods (strip, title, lower)
    - Day 4: Lists (append, indexing, sorted)
    - Day 5: Sets (optional: for tracking categories)
    - Day 6: Dictionaries (creating, accessing, updating)
    - Day 7: Conditionals (if/elif/else)
    - Day 8: For loops (iterate through lists)
    - Day 9: While loops (optional: for processing updates)
    - Day 10: Functions (define and call functions)
    """
    print("\n" + "=" * 70)
    print("📦 TODO PROBLEM: Simple Inventory Management System")
    print("=" * 70)
    
    print("""
    ⚠️  YOUR TASK: Implement the inventory management system below!
    
    📝 STEP-BY-STEP GUIDE:
    ---------------------
    
    Step 1: Create Store Variables (Day 1)
    ---------------------------------------
    store_name = "Tech Store"        # String
    store_location = "123 Main St"   # String
    store_id = 5001                  # Integer
    is_open = True                   # Boolean
    
    Print: Store name, location, and status
    
    Step 2: Create Products List (Day 4)
    ------------------------------------
    products = []  # Empty list to store product dictionaries
    
    Step 3: Implement add_product() Function (Days 3, 4, 6, 10)
    -----------------------------------------------------------
    def add_product(name, price, quantity):
        # Format name using string methods (Day 3: .strip().title())
        # Create product dictionary (Day 6):
        #   {"name": formatted_name, "price": price, "quantity": quantity}
        # Append to products list (Day 4: .append())
        # Return success message
    
    Step 4: Implement update_quantity() Function (Days 6, 7, 8, 10)
    ----------------------------------------------------------------
    def update_quantity(name, new_quantity):
        # Loop through products (Day 8: for loop)
        # Find product by name (Day 7: if statement)
        # Update quantity (Day 6: dictionary update)
        # Return success message or "Product not found"
    
    Step 5: Implement calculate_total_value() Function (Days 2, 8, 10)
    -------------------------------------------------------------------
    def calculate_total_value():
        # Initialize total = 0 (Day 1: variable)
        # Loop through products (Day 8: for loop)
        # For each product: total += price * quantity (Day 2: math)
        # Return total
    
    Step 6: Implement find_products_by_price_range() Function (Days 7, 8, 10)
    --------------------------------------------------------------------------
    def find_products_by_price_range(min_price, max_price):
        # Create empty list for results (Day 4)
        # Loop through products (Day 8: for loop)
        # Check if price is in range (Day 7: if statement with and)
        # Append matching products to results (Day 4: .append())
        # Return results list
    
    Step 7: Implement generate_report() Function (Days 3, 4, 7, 8, 10)
    --------------------------------------------------------------------
    def generate_report():
        # Print header with store name (Day 1: print)
        # Loop through products (Day 8: for loop)
        # Print each product's details (Day 6: dictionary access)
        # Calculate and print total value (call calculate_total_value())
        # Find low stock items (Day 7: if quantity < 10)
        # Sort products by price (Day 4: sorted(products, key=lambda...))
        # Print sorted list
    
    Step 8: Test Your Implementation
    ---------------------------------
    # Add products
    add_product("Laptop", 999.99, 5)
    add_product("Mouse", 19.99, 50)
    add_product("Keyboard", 49.99, 8)
    add_product("Monitor", 299.99, 12)
    
    # Update quantity
    update_quantity("Mouse", 45)
    
    # Calculate total
    total = calculate_total_value()
    print(f"Total Inventory Value: ${total}")
    
    # Find products in price range
    results = find_products_by_price_range(20, 300)
    print(f"Products between $20-$300: {results}")
    
    # Generate report
    generate_report()
    
    💡 HINTS:
    --------
    - Use .strip().title() to format product names
    - Use dictionary.get() for safe access
    - Use f-strings for formatted output
    - Check if list is empty: if not products:
    - Sort: sorted(products, key=lambda x: x['price'])
    
    🎯 EXPECTED OUTPUT:
    ------------------
    Store: Tech Store (ID: 5001)
    Location: 123 Main St
    Status: Open
    
    ✅ Added product: Laptop
    ✅ Added product: Mouse
    ✅ Added product: Keyboard
    ✅ Added product: Monitor
    
    ✅ Updated Mouse quantity to 45
    
    Total Inventory Value: $15999.55
    
    Products between $20-$300:
    [{'name': 'Keyboard', 'price': 49.99, ...}, {'name': 'Monitor', ...}]
    
    Inventory Report:
    - Laptop: $999.99 x 5 = $4999.95
    - Mouse: $19.99 x 45 = $899.55
    ...
    Low Stock Items: Laptop (5)
    """)
    
    # =====================================================================
    # TODO: WRITE YOUR IMPLEMENTATION BELOW
    # =====================================================================
    
    # TODO Step 1: Create store information variables
    # store_name = "Tech Store"
    # store_location = "123 Main St"
    # store_id = 5001
    # is_open = True
    
    # TODO Step 2: Create empty list for products
    # products = []
    
    # TODO Step 3: Implement add_product function
    # def add_product(name, price, quantity):
    #     # Format the name using .strip().title()
    #     # Create product dictionary
    #     # Append to products list
    #     # Return success message
    #     pass
    
    # TODO Step 4: Implement update_quantity function
    # def update_quantity(name, new_quantity):
    #     # Loop through products
    #     # Find matching product by name
    #     # Update quantity
    #     # Return success or error message
    #     pass
    
    # TODO Step 5: Implement calculate_total_value function
    # def calculate_total_value():
    #     # Initialize total to 0
    #     # Loop through products
    #     # Add price * quantity to total
    #     # Return total
    #     pass
    
    # TODO Step 6: Implement find_products_by_price_range function
    # def find_products_by_price_range(min_price, max_price):
    #     # Create empty result list
    #     # Loop through products
    #     # Check if price is in range
    #     # Append matching products
    #     # Return results
    #     pass
    
    # TODO Step 7: Implement generate_report function
    # def generate_report():
    #     # Print header
    #     # Loop through and print all products
    #     # Print total value
    #     # Find and print low stock items
    #     # Print sorted products
    #     pass
    
    # TODO Step 8: Test your implementation
    # Print store information
    # Add all 4 products
    # Update Mouse quantity
    # Calculate and print total value
    # Find products in price range
    # Generate full report
    
    print("\n" + "=" * 70)
    print("💡 TODO: Implement all the functions above!")
    print("📚 Review the Student Grade Manager example for reference.")
    print("🚀 Good luck with your implementation!")
    print("=" * 70)

# =============================================================================
# TEST CLASSES FOR DAYS 1-10
# =============================================================================

class TestDay1:
    """Test class for Day 1 basics"""
    
    def test_variables(self):
        """Test variable assignments"""
        name = "Test"
        age = 30
        assert isinstance(name, str)
        assert isinstance(age, int)
        print("✓ Day 1 variables test passed")

class TestDay2:
    """Test class for Day 2 numbers"""
    
    def test_math_operations(self):
        """Test math operations"""
        assert 2 + 3 == 5
        assert 10 / 2 == 5
        assert 2 ** 3 == 8
        print("✓ Day 2 math test passed")

class TestDay3:
    """Test class for Day 3 strings"""
    
    def test_string_methods(self):
        """Test string methods"""
        text = "Hello World"
        assert text.upper() == "HELLO WORLD"
        assert text.lower() == "hello world"
        assert len(text) == 11
        print("✓ Day 3 strings test passed")

class TestDay4:
    """Test class for Day 4 lists"""
    
    def test_list_operations(self):
        """Test list operations"""
        numbers = [1, 2, 3]
        numbers.append(4)
        assert numbers == [1, 2, 3, 4]
        assert numbers[0] == 1
        print("✓ Day 4 lists test passed")

class TestDay5:
    """Test class for Day 5 tuples and sets"""
    
    def test_tuples_sets(self):
        """Test tuples and sets"""
        coord = (1, 2)
        assert coord[0] == 1
        
        numbers = {1, 2, 2, 3}
        assert len(numbers) == 3
        print("✓ Day 5 tuples/sets test passed")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def run_days_1_10():
    """Run all examples for days 1-10"""
    print("🐍 PYTHON LEARNING PROGRAM - DAYS 1-10 🐍")  # Expected: 🐍 PYTHON LEARNING PROGRAM - DAYS 1-10 🐍
    print("=" * 50)  # Expected: ==================================================
    
    # Run all day functions
    day1_basics()
    day2_numbers()
    day3_strings()
    day4_lists()
    day5_tuples_sets()
    day6_dictionaries()
    day7_conditionals()
    day8_for_loops()
    day9_while_loops()
    day10_functions()
    
    # Run comprehensive problems (demonstrates all concepts)
    comprehensive_problem_student_grade_manager()
    comprehensive_problem_library_books()
    
    # Show TODO problem for self-practice
    todo_problem_inventory_management()
    
    print("\n" + "=" * 50)
    print("🧪 RUNNING TESTS...")  # Expected: 🧪 RUNNING TESTS...
    
    # Run all tests - executing test cases for each day
    test_day1 = TestDay1()
    test_day1.test_variables()  # Expected: ✓ Day 1 variables test passed
    
    test_day2 = TestDay2()
    test_day2.test_math_operations()  # Expected: ✓ Day 2 math test passed
    
    test_day3 = TestDay3()
    test_day3.test_string_methods()  # Expected: ✓ Day 3 strings test passed
    
    test_day4 = TestDay4()
    test_day4.test_list_operations()  # Expected: ✓ Day 4 lists test passed
    
    test_day5 = TestDay5()
    test_day5.test_tuples_sets()  # Expected: ✓ Day 5 tuples/sets test passed
    
    print("\n✅ All tests passed! Days 1-10 completed successfully!")  # Expected: ✅ All tests passed! Days 1-10 completed successfully!

if __name__ == "__main__":
    run_days_1_10()
