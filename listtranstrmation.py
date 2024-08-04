grades_list = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades_list.sort()
print(grades_list)

def Average(grades_list):
    return sum(grades_list) / len(grades_list)

grades_list = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average = Average(grades_list)

print("Average of the list =", round(average, 2))