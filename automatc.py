# import pypandoc

# # Generate 1000 Python coding problems (non-DSA)
# sections = [
#     ("Basics & I/O", 100),
#     ("Conditions", 100),
#     ("Loops", 150),
#     ("Strings", 150),
#     ("Lists", 150),
#     ("Tuples, Sets, Dicts", 150),
#     ("Functions", 100),
#     ("File Handling", 50),
#     ("Exception Handling", 50),
#     ("OOP", 100)
# ]

# problems = []
# count = 1

# for section, total in sections:
#     problems.append(f"\n## {section}\n")
#     for i in range(total):
#         if section == "Basics & I/O":
#             text = f"{count}. Take input from user and perform a basic operation (addition/subtraction/multiplication/division) based on user choice."
#         elif section == "Conditions":
#             text = f"{count}. Write a program that checks a condition using if-elif-else and prints an appropriate message."
#         elif section == "Loops":
#             text = f"{count}. Use a loop to generate and print a numeric or pattern sequence without using any DSA concepts."
#         elif section == "Strings":
#             text = f"{count}. Write a program that performs a string operation (reverse, count characters, check palindrome, replace, split, etc.)."
#         elif section == "Lists":
#             text = f"{count}. Perform an operation on a list (sum, max, min, remove duplicates, sort, filter values, etc.)."
#         elif section == "Tuples, Sets, Dicts":
#             text = f"{count}. Use tuple/set/dictionary to store data and perform retrieval, update, or traversal operations."
#         elif section == "Functions":
#             text = f"{count}. Create a function that solves a small task (prime check, factorial, average of numbers, etc.)."
#         elif section == "File Handling":
#             text = f"{count}. Write a program that reads from or writes to a file and processes the content."
#         elif section == "Exception Handling":
#             text = f"{count}. Write a program that handles an exception using try-except-finally."
#         elif section == "OOP":
#             text = f"{count}. Create a class and object to model a real-world entity and perform operations using methods."
#         problems.append(text)
#         count += 1

# # Add references
# references = """
# \n\n---
# ## References (Reputable Sources)

# 1. Python Official Documentation – Tutorial: https://docs.python.org/3/tutorial/
# 2. Python Built-in Functions: https://docs.python.org/3/library/functions.html
# 3. W3Schools Python Exercises: https://www.w3schools.com/python/python_exercises.asp
# 4. Real Python – Python Basics and Practice: https://realpython.com/
# """

# content = "# 1000 Python Coding Problems (Without DSA)\n\n" + "\n".join(problems) + references

# # Convert to txt using pypandoc
# output_path = "/mnt/data/python_1000_coding_problems.txt"
# pypandoc.convert_text(content, 'plain', format='md', outputfile=output_path, extra_args=['--standalone'])

# output_path


from fpdf import FPDF


pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)


with open("python_practice.txt", "r", encoding="utf-8") as f:
   for line in f:
       pdf.multi_cell(0, 8, line)


pdf.output("Python_Practice_Questions.pdf")