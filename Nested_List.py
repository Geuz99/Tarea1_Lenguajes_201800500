if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        arr.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in arr])))[1]
    print('\n'.join([a for a,b in sorted(arr) if b == second_highest]))
