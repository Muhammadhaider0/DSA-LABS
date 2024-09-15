from Question4 import *

def main(to_put,to_delete,to_get,size): # returns tuple(list,hash table)
    # Create the hash table
    hashtable = create_hashtable(size)

    # Putting key-value pairs into the hash table
    for key, value in to_put:
        put(hashtable, key, value, size)

    # Deleting keys from the hash table
    for key in to_delete:
        delete(hashtable, key, size)

    # Get values associated with keys from the hash table
    desired_values = []
    for key in to_get:
        value = get(hashtable, key, size)
        if value is not None:
            desired_values.append(value)

    return ((desired_values, hashtable))


if __name__ == "__main__":
    size = 5
    to_put = [(1 ,2) ,(" key "," value")]
    to_delete = [1]
    to_get = [" key "]
    print(main (to_put , to_delete , to_get , size))
    # Shoud print ([' value '], ([None, '#', None, ' key ', None], [None, '#', None, ' value ', None]))