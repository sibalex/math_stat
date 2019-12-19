def square(number):
  """
  this function returns a square of a number
  """
  result = number ** 2
  return result

# print(square(5))

my_res = square(10)
# print(my_res)

# help(square)

def square_2():
  user_input = int(input('Введите число'))
  result = user_input ** 2
  return result

# print(square_2())

# print(power(4))

def square_3(number):
  result = number ** 2
  print(result)
  return

# print(square_3(4))


number = 3


def square_2():
  number = 5
  power = 6
  return number ** power

# print(number ** power)

my_func = lambda x, y: x+y

# print(my_func(5, 6))

students_list = [
    {"name": "Василий", "surname": "Теркин", "sex": "мужчина", "program_exp": True, "grade": [8, 8, 9, 10, 9], "exam": 9},
    {"name": "Мария", "surname": "Павлова", "sex": "женщина", "program_exp": False, "grade": [7, 8, 9, 7, 9], "exam": 8},
    {"name": "Ирина", "surname": "Андреева", "sex": "женщина", "program_exp": True, "grade": [10, 9, 8, 10, 10], "exam": 10},
    {"name": "Татьяна", "surname": "Сидорова", "sex": "женщина", "program_exp": False, "grade": [7, 8, 8, 9, 8],"exam": 8},
    {"name": "Иван", "surname": "Васильев", "sex": "мужчина", "program_exp": True, "grade": [9, 8, 9, 6, 9], "exam": 10},
    {"name": "Роман", "surname": "Золотарев", "sex": "мужчина", "program_exp": False, "grade": [8, 9, 9, 6, 9], "exam": 10}
]

def get_average_grades(students):
  sum_average_hw = 0
  sum_average_ex = 0
  for student in students:
    sum_average_hw += sum(student['grade']) / len(student['grade'])
    sum_average_ex += student['exam']
  print('Средняя оценка за ДЗ по группе: ', round(sum_average_hw / len(students), 2))
  print('Средняя оценка за экзамен по группе: ', round(sum_average_ex / len(students), 2))  

# get_average_grades(students_list)

def get_average_grades_by_exp(students, exp=True):
  sum_average_hw = 0
  sum_average_ex = 0
  student_counter = 0
  for student in students:
    if student['program_exp'] == exp:
      sum_average_hw += sum(student['grade']) / len(student['grade'])
      sum_average_ex += student['exam']
      student_counter += 1
  if exp == True:
    print('Средняя оценка за ДЗ у студентов с опытом: ', round(sum_average_hw / student_counter, 2)) 
    print('Средняя оценка за экзамен у студентов с опытом: ', round(sum_average_ex / student_counter, 2)) 
  else:
    print('Средняя оценка за ДЗ у студентов без опыта: ', round(sum_average_hw / student_counter, 2)) 
    print('Средняя оценка за экзамен у студентов без опыта: ', round(sum_average_ex / student_counter, 2))    

# get_average_grades_by_exp(students_list)
# get_average_grades_by_exp(students_list, exp=False)

def main():
  while True:
    user_input = input('Введите команду: ')
    if user_input == '1':
      get_average_grades(students_list)
    elif user_input == '2':
      get_average_grades_by_exp(students_list)
    elif user_input == '3':
      get_average_grades_by_exp(students_list, exp=False)
    elif user_input == 'q':
      print('До свидания!')
      break

main()