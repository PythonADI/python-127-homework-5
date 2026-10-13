def countdown(start, step=1):
    while start >=1:
        print(start)
        start = start - step

countdown(3)
print("---")
countdown(10, 3)