books = {"The Da Vinci Code": 2003,
         "Harry Potter and the philosopher's stone": 1997,
         "Angels and Demons": 2000}


def bubble_sort(array):
    n = len(array)
    while 1 < n:
        for i in range(n - 1):
            j = i + 1
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
        return(array)


def create_list_of_dates_and_sort():
    value_list = list(books.values()) #creates_list_from_dates
    sorted_list = bubble_sort(value_list) #Sorts_list_of_dates
    return sorted_list


def for_date_print_book(sorted):
    for x in sorted:
        for key, value in books.items():
            if value == x:
                print(key, ":", value)


def main():
    sort = create_list_of_dates_and_sort()
    for_date_print_book(sort)

main()

