if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x = student_marks[query_name]
    count=0
    for i in x:
        count+=i
    count = float(count)
    final_ans = count/3
    print("%.2f" % final_ans)