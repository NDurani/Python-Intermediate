import pandas
import random

# nums = [1, 2, 3]
# new_list = [n + 1 for n in nums]
# print(new_list)
#
# name = "Durani"
# new_string = [c for c in name]
# print(new_string)

# num_list = [n * 2 for n in range(1, 5)]
# print(num_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
#
# cap_list = [name.upper() for name in names if len(name) >= 5]
# print(cap_list)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in nums]
# print(squared_numbers)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# even_nums = [num for num in nums if num % 2 == 0]
# print(even_nums)

# file1 = pandas.read_csv("file1.txt")
# file1_column = file1["3"].tolist()
# file2 = pandas.read_csv("file2.txt")
# file2_column = file2["3"].tolist()
#
# result = [num for num in file1_column if num in file2_column]
# result.insert(0, 3)
# print(result)

# with open("file1.txt", "r") as file1:
#     file_1 = file1.readlines()
#     with open("file2.txt", "r") as file2:
#         file_2 = file2.readlines()
#         result = [int(num) for num in file_1 if num in file_2]
#         print(result)

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
#
# student_scores = {student: random.randint(10, 100) for student in names}

# passed = {student: score for student, score in student_scores.items() if score >= 50}
# print(passed)
# passed = {student: student_scores[student] for student in student_scores if student_scores[student] >= 50}
# print(passed)

# sentence = "what is the Airspeed Velocity of an unladen swallow?"
# # word_list = sentence.split()
#
# result = {word: len(word) for word in sentence.split()}
# print(result)

my_dict = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

result = {day: temp_c * 9/5 + 32 for day,temp_c in my_dict.items()}
print(result)