arr = [42, 7, 89, 13, 56, 2, 74, 31, 95, 18, 63, 5, 81, 27, 49, 11, 68, 36, 92, 24, 53]
n = len(arr)
count = 0

for i in range(n):
    m = i
    count += 1
    for j in range(i+1, n):
        count += 1
        if arr[j] < arr[m]:
            m = j
    arr[i], arr[m] = arr[m], arr[i]

print(f"\nМассив: {arr}\n\n"
      f"Количество итераций: {count}\n")