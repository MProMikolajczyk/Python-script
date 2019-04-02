#liczenie sumy
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  count=0
  for grades in scores:
    count+=grades
  return count

print grades_sum(grades)

#liczenie sredniej za pomoca funkcji w funkcji
def grades_average(grades_input):
    average=grades_sum(grades_input)/float(len(grades_input)) #odolanie do zbiru z ktorego sie kozysta
    return average

print grades_average(grades)