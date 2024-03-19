
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() # unpacks the first token as name and the rest as line.
        scores = list(map(float, line))
        student_marks[name] = scores # creating a dictionary with key = name, and values = scores (list)
    query_name = input()
    
    query_marks = list(student_marks[query_name]) # extracting the list from student_marks that matches the name in query_name
    query_avg = sum(query_marks) / len(query_marks)
    
    print('%.2f'% query_avg) #print with two decimal points behind ('%.2f'%)
