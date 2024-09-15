from Question1 import *
from Question2 import *

def put(hashtable,key, data,size):
    hashvalue = hash_function(key, size)
    if hashtable[0][hashvalue] is None:
        hashtable[0][hashvalue] = key
        hashtable[1][hashvalue] = data
    else:
        if hashtable[0][hashvalue] == key:
            hashtable[1][hashvalue] = data
        else:
            newhash = hashvalue
            iteration = 1
            while hashtable[0][newhash] is not None and hashtable[0][newhash] != key:
                newhash = collision_resolver(hashvalue, size, iteration)
                iteration += 1
            if hashtable[0][newhash] is None:
                hashtable[0][newhash] = key
                hashtable[1][newhash] = data
            else:
                hashtable[1][newhash] = data


def get(hashtable,key,size):
    start = hash_function(key, size)
    pos = start
    while hashtable[0][pos] is not None:
        if hashtable[0][pos] == key:
            return hashtable[1][pos]
        else:
            pos = collision_resolver(start, size, 1)
            if pos == start:
                break
    return None

if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    print(get(H,5,10)) # Should print 3