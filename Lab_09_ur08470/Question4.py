from Question3 import *

def delete(hashtable, key, size):
    hashvalue = hash_function(key, size)
    if hashtable[0][hashvalue] != key:
        # If key not found at the initial hashvalue, we need to resolve collision
        while hashtable[0][hashvalue] != key:
            newhash = collision_resolver(hashvalue, size, 1)
            # Place tombstone '#' at index newhash in both key and value lists of hashtable
            hashtable[0][newhash] = '#'
            hashtable[1][newhash] = '#'
            if key> size:
                break
    else:
        # If key is found at the initial hashvalue, place tombstone '#' at that index
        hashtable[0][hashvalue] = '#'
        hashtable[1][hashvalue] = '#'

if __name__ == "__main__":
    H = create_hashtable(10)
    put(H,5,3,10)
    delete(H,5,10)
    print(H)
    # Should print ([None, None, None, None, None, '#', None, None, None, None], [None, None, None, None, None, '#', None, None, None, None])