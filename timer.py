from timeit import default_timer as timer
n = 0 #number of people

while True:
    i = input()
    if i == "enter":
        start = timer()
        n += 1
    elif i == "exit":
        end = timer()
        n -= 1
        break
print(int(end - start)) #seconds