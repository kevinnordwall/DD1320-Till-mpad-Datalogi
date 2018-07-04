def hashfunc( key):
    hash_sum = 0
    for pos in range(len(key)):
        if key[pos].isalpha():
            hash_sum = hash_sum + ord(key[pos])
        elif key[pos].isdigit():
            hash_sum = hash_sum + int(key[pos])
        else:
            hash_sum = hash_sum + ord(key[pos])
    return hash_sum % 16
