list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_i = 0

for i in range(1, len(list_numbers)):
    if list_numbers[i] > list_numbers[max_i]:
        max_i=i

max = list_numbers[max_i]
list_numbers[max_i] = list_numbers[-1]
list_numbers[-1] = max

print(list_numbers)
