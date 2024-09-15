def create_hashtable(size): # returns tuple(list,list)
    keys = [None] * size
    values = [None] * size
    hashtable = (keys, values)
    return hashtable

def resize_hashtable(hashtable,size,increase): #return hashtable,size
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    current_size = len(hashtable[0])
    if increase:
        new_size = current_size * 2
    else:
        new_size = current_size // 2
    if new_size < 7:
        new_size = 7
    while not is_prime(new_size):
        if increase:
            new_size += 1
        else:
            new_size -= 1
    old_keys, old_data = hashtable
    new_hashtable = create_hashtable(new_size)
    for keys, data in zip(old_keys, old_data):
        if keys:
            for key in keys:
                put(new_hashtable, key, data[key], new_size)
    return new_hashtable


def hash_function(key,size): #returns integer (Address)
    hash_val = sum(ord(char) for char in key)
    hash_val >>= 4
    return hash_val % size

def collision_resolver(key,oldAddress,size): #returns integer (Address)
    offset = sum(ord(char) for char in key) // size
    return (offset + oldAddress) % size

def put(hashtable,key, data,size): #return hashtable,size
    keys, data_list = hashtable
    hash_val = hash_function(key, size)
    if keys[hash_val] is None:
        keys[hash_val] = [key]
        data_list[hash_val] = {key: data}
    else:
        if key not in keys[hash_val]:
            keys[hash_val].append(key)
            data_list[hash_val][key] = data
        else:
            data_list[hash_val][key] = data
            return hashtable, size
    current_load = loadFactor(hashtable, size)
    if current_load > 0.75:
        return resize_hashtable(hashtable, size, True)
    return hashtable, size

def loadFactor(hashtable,size): # returns a float - Loadfactor of hashtable
    keys, _ = hashtable
    total_slots = len(keys)
    total_items = sum(1 for slot in keys if slot is not None for _ in slot)
    return total_items / total_slots

def Update(hashtable,key, columnName, data,size,collision_path,opNumber): # returns Nothing, prints 'record Updated'
    keys, data_list = hashtable
    hash_val = hash_function(key, size)
    if keys[hash_val] is not None and key in keys[hash_val]:
        data_list[hash_val][key][columnName] = data
    else:
        if opNumber not in collision_path:
            collision_path[opNumber] = [hash_val]
        else:
            collision_path[opNumber].append(hash_val)
    return hashtable        
    
def get(hashtable,key,size,collision_path,opNumber): # returns dictionary
    keys, data_list = hashtable
    hash_val = hash_function(key, size)
    if keys[hash_val] is not None and key in keys[hash_val]:
        print(data_list[hash_val][key])
    else:
        print("Item not found")
        if opNumber not in collision_path:
            collision_path[opNumber] = [hash_val]
        else:
            collision_path[opNumber].append(hash_val)    


def delete(hashtable, key, size,collision_path,opNumber): #returns hashtable, size, prints a msg  'Item Deleted'
    keys, data_list = hashtable
    hash_val = hash_function(key, size)
    if keys[hash_val] is not None and key in keys[hash_val]:
        del data_list[hash_val][key]
        keys[hash_val].remove(key)
    else:
        if opNumber not in collision_path:
            collision_path[opNumber] = [hash_val]
        else:
            collision_path[opNumber].append(hash_val)
    return hashtable
#print(create_hashtable(7))
#print(resize_hashtable(create_hashtable(3),3,True))