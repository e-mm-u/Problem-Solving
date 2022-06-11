if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marksList = student_marks[query_name]
    
    avg = sum(marksList)/len(marksList)
    # ________if you do not want to use built in function sum then comment the upper line and undo the comment of the block below ______________
    
    # marks = student_marks[query_name]
    # l = len(marks)
    # avg = 0
    # for i in range(l):
    #     avg += marks[i]
    # avg = avg/l
    # _____block ends here -------
    
    print("{:.2f}".format(avg))
