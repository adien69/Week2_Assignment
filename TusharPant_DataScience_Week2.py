# def arithmetic_operations(a, b):
#     #Performs basic arithmetic operations on two numbers and prints the results.
#     print(f"\nResults for numbers {a} and {b}:")
#     print(f"Addition: {a} + {b} = {a + b}")
#     print(f"Subtraction: {a} - {b} = {a - b}")
#     print(f"Multiplication: {a} * {b} = {a * b}")
#     # Handle division by zero safely
#     if b != 0:
#         print(f"Division: {a} / {b} = {a / b:.2f}")
#         print(f"Modulus: {a} % {b} = {a % b}")
#     else:
#         print("Division:Cannot divide by zero!")
#         print("Modulus: Cannot perform modulus by zero!")
#     print(f"Exponentiation: {a} ** {b} = {a ** b}")


#  Main Program 
# # Get user inputs
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))

# # Call the function
# arithmetic_operations(num1, num2) 

# Task 2  
# import numpy as np   
# define a function inside the function all the operation is perfomed. 
# def analyze_list(numbers):  
#     # Basic list operation 
#     print(f"The length of list is: {len(numbers)}")  
#     print(f"The max element in list is: {max(numbers)}") 
#     print(f"The min element in list is: {min(numbers)}")   
#     # modifying the list 
#     numbers.append(12)
#     print(f"List after append: {numbers}")   
#     numbers.remove(5) 
#     print(f"List after element remove: {numbers}")   
#     # sorting of list in ascending and descending ordre.  
#     asc_sorted= sorted(numbers)
#     des_sorted = sorted(numbers,reverse = True)   
#     print(f"the ascending order list is: {asc_sorted}")  
#     print(f"the descending oreder list is: {des_sorted}") 

#     #converting list into numpy 
#     my_array= np.array(numbers)  
#     print(f"Array: {my_array}") # printing the array 
#     print(f"Mean: {np.mean(my_array):}") # printing the mean of the array 
#     print(f"Median: {np.median(my_array):}") # printing median of the array 
#     print(f"Standard Deviation: {np.std(my_array):}") # printing standard deviation. 
# numbers = [2,3,5,7,4,9,1,0,6,10]  
# analyze_list(numbers) 

# Task 3   
# printing the set using the for loop. 
# my_dictionary={"name": "ram",
#  "age":18,
#  "course":"science",
#  "marks":"94"}  
# for key, value in my_dictionary.items(): 
#      print(f"key: {key}, value: {value}")    

# #Added a new element in the dictionary    
# my_dictionary['grade'] = "A" 
# print(my_dictionary)  

# # set of unique_courses 
# unique_courses = { "python", "Data Science","AI","python"}   
# print(f"the set of unique_courses is:{unique_courses} ") 

# # set operation 
# set1 = {1,2,3} 
# set2 = {4,5,3}    
# define the function all the set operation is performed inside the function. 
# def set_operation(set1,set2):    
#    union_set = set1.union(set2)  
#    intersection_set =set1.intersection(set2) 
#    difference_set = set1.difference(set2) 
#    print(f" the union of set1 and set2: {union_set}")  
#    print(f"the intersection of set1 and set2: {intersection_set}") 
#    print(f"the diffrence of set1 and set2: {difference_set}")  
# set_operation(set1,set2)   

# Task 4 
def create_and_write_file(filename):
    #Creates a text file and writes student data into it."""
    # List of students: (Name, Course, Marks)
    students = [
        ("Alice", "Computer Science", 82),
        ("Bob", "Mathematics", 67),
        ("Charlie", "Physics", 91),
        ("Diana", "Chemistry", 74),
        ("Ethan", "Biology", 88)
    ]

    with open(filename, "w") as file:
        for name, course, marks in students:
            file.write(f"{name}, {course}, {marks}\n")

    print(f"Data successfully written to {filename}.")


def read_and_display_above_75(filename):
    #Reads the file and displays students with marks above 75.
    print("\nStudents with marks above 75:\n")

    with open(filename, "r") as file:
        for line in file:
            name, course, marks = line.strip().split(", ")
            marks = int(marks)
            if marks > 75:
                print(f"Name: {name}, Course: {course}, Marks: {marks}")


# Main Program 
filename = "student_data.txt"

# Step 1 & 2: Create and write data to the file
create_and_write_file(filename)

# Step 3: Read and display students with marks > 75
read_and_display_above_75(filename) 
