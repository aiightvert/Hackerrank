cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    if n== 0:
        return []
    if n <= 1:
        return [0]
    x = [0, 1]
    for i in range(1, n-1):
        x.append(x[i] + x[i-1])
    return x


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
