def hash_function(key,size):
    # if key is integer
    if isinstance(key, int):
        index = key % size 
        return index
    #if is a string
    elif isinstance(key, str):
        # Calculate the sum of unicode/ascii values of each letter in the string

        ascii_sum = sum(ord(char) for char in key)
        index = ascii_sum % size
        # Return the index by taking modulus with the size
        return index
    else:
        raise ValueError("Unsupported key type")
    

def collision_resolver(key,size, iteration):
    previous_hash = key
    new_hash = (previous_hash + iteration) % size
    return new_hash
if __name__ == "__main__":
    print(hash_function(5,10)) # Should print 5
    print(hash_function("Hello", 10)) # Should print 0
    print(collision_resolver(hash_function("Hello", 10),10,2)) # Should print 2