def greet():
    print("Hello From Beauty")
greet()

def greet_student(name):
    print(f"Hello {name}! Welcome")

greet_student("Htet")
greet_student("Myat")
greet_student("Noe")

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores)

scores = [70,80,90,38,99]
calculate_average(scores)
result = calculate_average(scores)
print(result)

def calculate_total(scores):
    if len(scores) == 0:
        return 0
    else:
        return sum(scores)

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    else:
        return sum(scores)/len(scores)

def classify_grade(score):
    if score <= 0 or score >= 100:
        print("Invalid Scores")
    if score >= 80:
        print("Excellent")
    elif score >= 60:
        print("Good")
    elif score >= 40:
        print("Pass")
    else:
        print("Fail")

def count_passed(scores):
    if len(scores) == 0:
        return 0
    else:
        pass_count = 0
        for score in scores:
            #print(score)
            if score >= 40:
                pass_count += 1
        return pass_count

print(calculate_total(scores))
print(calculate_average(scores))
for score in scores:
    classify_grade(score)
print(count_passed(scores))

scores_list = [55,80,35,90,65]
scores_list.append(75)
print(scores_list)

scores_list[1] = 85
print(scores_list)

print("Higest ",max(scores_list))
print("Lowest ",min(scores_list))
average = sum(scores_list)/len(scores_list)

for score in scores_list:
    if score >= 80:
        print(score)

student = {
    "name" : "Su Su",
    "age"  : 20,
    "score": 88,
    "pass" : True
}
print(student["name"])
print(student["score"])

students = [
    {"name" : "Hla Hla", "score" : 85},
    {"name" : "Myo Myo", "score" : 92},
    {"name" : "Aung Aung", "score" : 35}
]
for student_lis_dic in students:
    print(student_lis_dic["name"], student_lis_dic["score"])