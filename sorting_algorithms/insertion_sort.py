arr = [42, 7, 89, 13, 56, 2, 74, 31, 95, 18, 63, 5, 81, 27, 49, 11, 68, 36, 92, 24, 53]
n = len(arr)
count = 0

for i in range(1, n):
    j = i
    count += 1
    while j > 0 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
        count += 1

print(f"\nМассив: {arr}\n\n"
      f"Количество итераций: {count}\n")