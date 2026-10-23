scores = [45,70,85,30,90,55]
total = 0
pass_score = 0
fail_score = 0

for score in scores:
    total += score
    if score < 40:
        fail_score += 1
    else:
        pass_score +=1

average = total/ len(scores)

print("Total: ", total)
print("Average: ",average)
print("Pass_Score: ",pass_score)
print("Fail_Score: ",fail_score)

count = 1
while count <= 5:
    print(count)
    count += 1

new_score = [70,85,60,90,45]

total = 0
for score1 in new_score:
    total += score1

average = total / len(new_score)

print("Total ",total)
print("Average ",average)

