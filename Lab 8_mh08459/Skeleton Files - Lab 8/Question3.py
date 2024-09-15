
def quick_sort_rectangles(array, low, high, column_number):
  if low < high:
            pi = partition_mid(array,low,high,column_number)
            print(array)
            quick_sort_rectangles(array,low,pi-1,column_number)
            quick_sort_rectangles(array,pi+1,high,column_number)


def partition(array, low, high, column_number):
    pivot=low
    i=low+1
    for j in range(low+1,high+1):
        if array[j][column_number]<= array[pivot][column_number]:
            array[i],array[j]=array[j],array[i]
            i= i + 1


    array[pivot],array[i-1]=array[i-1],array[pivot]
    pivot=i-1
    return pivot


def partition_mid(array,low, high, column_number):
    pivot= low
    array[low],array[pivot]=array[pivot],array[low]
    return (partition(array,low,high,column_number))   


# Testing
rectangle_records  = [{"ID":"Rect1","Length": 40 ,"Breadth": 25 ,"Color":"red"} , {"ID":"Rect2","Length":30 ,"Breadth": 20 ,"Color":"blue"} , {"ID":"Rect3","Length": 70 ,"Breadth": 45 ,"Color":"green"} , {"ID":"Rect4","Length": 20 ,"Breadth": 10 ,"Color":"purple"}]
quick_sort_rectangles(rectangle_records, 0, len(rectangle_records)-1, "Length")

# Should print:
# [{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}]
# [{'ID': 'Rect4', 'Length': 20, 'Breadth': 10, 'Color': 'purple'}, {'ID': 'Rect2', 'Length': 30, 'Breadth': 20, 'Color': 'blue'}, {'ID': 'Rect1', 'Length': 40, 'Breadth': 25, 'Color': 'red'}, {'ID': 'Rect3', 'Length': 70, 'Breadth': 45, 'Color': 'green'}]