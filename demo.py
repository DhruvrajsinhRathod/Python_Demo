my_dict = {
    "name": "John",
    "age": 30,
    "height": 6.1,
    "is_student": False,
    "grades": [90, 85, 95],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zipcode": "12345"
    }
}

my_dict["age"] = 31
print(my_dict)

# clear(): Removes all items from the dictionary.
# copy(): Returns a shallow copy of the dictionary.
# fromkeys(keys[, value]): Returns a new dictionary with keys from iterable keys and values set to value.
# get(key[, default]): Returns the value for key if key is in the dictionary, else default.
# items(): Returns a new view of the dictionary's items (key-value pairs).
# keys(): Returns a new view of the dictionary's keys.
# values(): Returns a new view of the dictionary's values.
# pop(key[, default]): Removes and returns the value associated with key. If key is not found, default is returned if given, otherwise KeyError is raised.
# popitem(): Removes and returns an arbitrary (key, value) pair from the dictionary. Raises KeyError if the dictionary is empty.
# update([other]): Updates the dictionary with the key-value pairs from other, overwriting existing keys if present.
# setdefault(key[, default]): If key is in the dictionary, return its value. If not, insert key with a value of default and return default.
# contains(key): Returns True if key is in the dictionary, False otherwise. (This method is usually called using the in operator.)