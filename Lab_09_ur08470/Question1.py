def create_hashtable(size): # returns tuple(list,list)
    # Create two lists of size 'size' initialized with None
    keys = [None] * size
    values = [None] * size
    # Return a tuple containing both lists
    hashtable = (keys, values)
    return hashtable

if __name__ == "__main__":
    print(create_hashtable(5))
    # Shoud print ([None, None, None, None, None], [None, None, None, None, None])