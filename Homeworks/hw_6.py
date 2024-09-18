def bubble_sort(list_of_numbers):
    position = 0
    last_number = len(list_of_numbers) - 1
    while last_number != 0:
        if list_of_numbers[position] > list_of_numbers[position + 1]:
            list_of_numbers[position], list_of_numbers[position + 1] = list_of_numbers[position + 1], list_of_numbers[position]
        position += 1
        if position == last_number:
            position = 0
            last_number -= 1
            continue
    return list_of_numbers


def selection_sort(list_of_numbers):
    for number_index in range(len(list_of_numbers) - 1):
        minimal_number = float("inf")
        for num in list_of_numbers[number_index + 1:]:
            if num < minimal_number:
                minimal_number = num
        minimal_number_index = list_of_numbers.index(minimal_number)
        if minimal_number < list_of_numbers[number_index]:
            list_of_numbers[number_index], list_of_numbers[minimal_number_index] = minimal_number, list_of_numbers[number_index]
    return list_of_numbers


print(bubble_sort([4, 7, 2, 9, 5, 3]))
print(selection_sort([6, 2, 9, 8, 4, 5]))


def binary_search(Val, A):
    N = len(A)
    ResultOK = False
    First = 0
    Last = N - 1
    while True:
        if First < Last:
            Middle = round((First + Last) / 2)
            if Val == A[Middle]:
                First = Middle
                Last = First
                ResultOK = True
                Pos = Middle
            else:
                if Val > A[Middle]:
                    First = Middle + 1
                else:
                    Last = Middle - 1
        else:
            if ResultOK == True:
                print("Элемент найден")
                print(Pos)
            else:
                print("Элемент не найден")
            break


binary_search(3, [4, 9, 2, 5, 3, 6, 7, 8])