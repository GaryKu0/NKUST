total = 0
score = 0
scores = []
while score != -1:
    score = int(input("Enter Score: "))
    if score == -1:
        break
    # array of scores and corresponding letter grades
    total += score
    scores.append(score)
print("共有"+str(len(scores))+"位學生")
print("本班總成績:"+str(total)+",平均為"+str(total/len(scores))+"分")
# print all value in scores
print("全部成績:", scores)
