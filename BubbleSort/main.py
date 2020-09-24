Da_Vinci = {"Name": "The Da Vinci Code", "Date": 2003}
Harry_Potter = {"Name": "Harry Potter and the philosopher's stone", "Date": 1997}
Angels_and_Demons = {"Name": "Angels and Demons", "Date": 2000}
books = [Da_Vinci, Harry_Potter, Angels_and_Demons]


def create_list_of_dates_and_sort(array):
    n = len(array)
    while 1 < n:
        for i in range(n - 1):
            j = i + 1
            if array[i]["Date"] > array[j]["Date"]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
        return (array)


def pretty_print(array):
    for x in array:
        print(x["Name"], ":", x["Date"])


def main():
    sort = create_list_of_dates_and_sort(books)
    pretty_print(sort)


main()