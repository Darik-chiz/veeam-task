import sys
import hashlib

# сравнение хеша
def hash_func(code, name, hash_user):

    # выбор необходимого алгоритма
    if 'md5' in code:
        hashcheck = hashlib.md5()
    elif 'sha1' in code:
        hashcheck = hashlib.sha1()
    else:
        hashcheck = hashlib.sha256()
    
    try:
        file = open(name, 'rb')
    except FileNotFoundError:
        return 'NOT FOUND'
    else:
        # расчитать хеш файла
        while True:
            data = file.read(666)
            if not data:
                break
            hashcheck.update(data)

        # сравнить с хеш из файла
        if hashcheck.hexdigest() == hash_user:
            return 'OK'
        else:
            return 'FAIL'


with open(sys.argv[1], 'r') as file:
    for line in file:
        string_array = line.split()

        name = string_array[0]
        hash_type = string_array[1]
        hash_user = string_array[2].casefold()

        file = sys.argv[2]+'/{}'.format(name)
        result = hash_func(hash_type, file, hash_user)

        print('{} '.format(name) + result)