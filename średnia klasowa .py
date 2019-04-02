lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

def average(numbers):#srednia
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):#srednia wiersza
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests#srednia wazona

def get_letter_grade(score):#system oceniania
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"

def get_class_average(class_list):#srednia klasowa
  results = []
  for student in class_list:
    results.append(get_average(student))#przypisanie studenta do klasy
  return average(results)#odwolanie sie do wyniku przypisana i srdniej klasowej

students = [lloyd, alice, tyler]

print get_class_average(students)#wydruk sredniej klasowej
print get_letter_grade(get_class_average(students))#wyruk oceny dla srednij klasowej