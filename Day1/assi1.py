students = [
    {"name"  : "Aung Aung", "age" : 21, "study_hours" : 2, "Python_score" : 82},
    {"name"  : "Myo Myo", "age" : 23, "study_hours" : 4, "Python_score" : 95},
    {"name"  : "Hla Hla", "age" : 22, "study_hours" : 1, "Python_score" : 66},
    {"name"  : "Su Su", "age" : 20, "study_hours" : 2, "Python_score" : 77},
    {"name"  : "Thet Thet", "age" : 24, "study_hours" : 1, "Python_score" : 55}
]
fixed_grade = ("Excellent","Good","Pass","Fail")




def classify_grade(score):
    if score == 0 or score > 100:
        return "Invalid Scores"
    elif score >= 80:
        return fixed_grade[0]
    elif score  >= 60:
        return fixed_grade[1]
    elif score >= 40:
        return fixed_grade[2]
    else:
        return fixed_grade[3]

def calculate_average(score):
    average = sum(score)/ len(score)
    return average


def count_passed(score_list):
    number_of_pass = 0
    
    for score in score_list:
        if score >= 40:
            number_of_pass += 1
            
    return number_of_pass 

def count_failed(score_list):
   
    number_of_fail = 0
    for score in score_list:
        if score <= 40:
            number_of_fail += 1
        
    return number_of_fail 

def top_student(pairs_list):
    # Start by assuming the first pair is the best
    best_student_name = pairs_list[0][0]
    highest_score = pairs_list[0][1]
    
    # Loop through each pair to find the maximum score
    for pair in pairs_list:
        current_name = pair[0]
        current_score = pair[1]
        
        if current_score > highest_score:
            highest_score = current_score
            best_student_name = current_name
            
    # Return only the name of the top person
    return best_student_name




for scores in students:

    print(f"Name: {scores["name"]} \n Age: {scores["age"]} \n Study Hours: {scores["study_hours"]} \n Scores: {scores["Python_score"]}")
    #name = scores["name"]
    score = scores["Python_score"]
    #print(score)
    print(classify_grade(score))
    #print(type(scores["Python_score"]))
    
# 1. Safely collect all Python scores using .get()
python_scores = [student.get("Python_score") for student in students if student.get("Python_score") is not None]
print(python_scores)
print("Total Student: ",len(python_scores))
print("Average Score: ",calculate_average(python_scores))
print("Higest: ",max(python_scores))
print("Lowest: ",min(python_scores))
# 2. Pass the entire list to your function
print("Passed Students: ",count_passed(python_scores))
print("Failed Students: ",count_failed(python_scores))
#print("Top Student: ",top_student(python_scores))
name_list= [student.get("name") for student in students if student.get("name") is not None]
print(name_list)
name_score = list(zip(name_list,python_scores))
print(name_score)
print("Top Student: ",top_student(name_score))












    


     


    