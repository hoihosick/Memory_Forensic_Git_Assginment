def main():
    
def bubble_sort(arr):
    a = arr[:]  # 원본 보존
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:  # 조기 종료
            break
    return a


if __name__ == "__main__":
    main()