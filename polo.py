my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
def max_key_in_dict(a):
    keys = []
    for i in a:
         if a[i] is not None:
            keys.append(max_key_in_dict(a[i]))
    else:
        keys.append(i)
        return max(keys)