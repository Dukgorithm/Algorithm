def solution(table, languages, preference):
    answer = []
    new_table = sorted([list(t.split()) for t in table], key=lambda x : x[0])
    job = {n: new_table[n][0] for n in range(len(new_table))}

    for j in range(len(job)):
        total = 0
        for i in range(len(languages)):
            if languages[i] in new_table[j]:
                total += (6 - new_table[j].index(languages[i])) * preference[i]
        answer.append(total)

    print(answer)
    return job[answer.index(max(answer))]

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
["JAVA", "JAVASCRIPT"], [7, 5])) 