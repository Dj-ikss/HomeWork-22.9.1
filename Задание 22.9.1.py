def quicksort(numbers, start, end):
    if end - start > 1:
        p = partition(numbers, start, end)
        quicksort(numbers, start, p)
        quicksort(numbers, p + 1, end)
def partition(numbers, start, end):
    pivot = numbers[start]
    i = start + 1
    j = end - 1
    while True:
        while (i <= j and numbers[i] <= pivot):
            i = i + 1
        while (i <= j and numbers[j] >= pivot):
            j = j - 1

        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        else:
            numbers[start], numbers[j] = numbers[j], numbers[start]
            return j

numbers = input('Введите целые положительные числа через пробел: ').split()
list_numbers = [int(x) for x in numbers]
if min(list_numbers) < 0:
    print('Введите положительные числа!')
    exit() #Завершаем программу, если в списке есть отрицательные числа

find_number = int(input('Введите число : '))
print('---------Преобразование введённой последовательности в список:', list_numbers)
if (min(list_numbers))>find_number or (max(list_numbers))<find_number: #вхождение в список числа
    print('Число не в списке, введите заново')
    exit() #Завершаем программу, если введённое число не всписке пользователя

numbers.append(find_number)
numbers = [int(x) for x in numbers]
quicksort(numbers, 0, len(numbers))
print('---------Сортировка списка по возрастанию элементов: ', numbers)

def binary_search(sequence, start_element, key): #бинарный поиск
    end_element = len(sequence) - 1
    while start_element <= end_element:
        middle_element = (start_element + end_element) // 2
        if sequence[middle_element] == key:
            return middle_element
        elif sequence[middle_element] < key:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    return 'Число не в списке'

sequence = numbers #число пользователя
result = binary_search(sequence=sequence, start_element=0, key=find_number)
print("----- ОТВЕТ----")
print('номер позиции элемента меньше введённого числа: ', result-1)
print('номер позиции элемента следующего за введённым числом: ', result+1)
