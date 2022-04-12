def task():
    n_list = []
    n = int(input("Enter x value: "))
    for i in range(n):
        y = int(input("Enter the numbers: "))
        if y > 0 and y <= 10:
            n_list.append(y)
    for x in range(0, len(n_list)):
            if n_list[x] % 2 == 0:
                print("Even: ",n_list[x])
            else:
                print("Odd: ",n_list[x])
task()