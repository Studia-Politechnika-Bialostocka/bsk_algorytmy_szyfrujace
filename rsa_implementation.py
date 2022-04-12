import array


def generate_public_private_key(p, q):
    print(p, q)


def encrypt_rsa(text, key):
    text2 = bytearray()
    text2.extend(map(ord, text))

    result = [power_mod(el, *key) for el in text2]
    result2 = ''.join(map(chr, result))
    return result


def decrypt_rsa(text, key):
    result_codes = [power_mod(el, *key) for el in text]
    result = ''.join(map(chr, result_codes))
    return result


def power_mod(base, exp, mod):
    if mod == 1:
        return 0
    res = 1
    base = base % mod
    while (exp > 0):
        if (exp % 2 == 1):
            res = res * base % mod
        exp = exp >> 1
        base = (base ** 2) % mod
    return res


def encrypt_file(public_key, file_name):
    key = tuple([int(el) for el in public_key.replace('(', '').replace(')', '').split(',')])
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()
    result = encrypt_rsa(file_content, key)
    result = ' '.join([str(el) for el in result])
    create_file(result, 'encrypted_message.txt')
    return result


def decrypt_file(private_key, file_name):
    key = tuple([int(el) for el in private_key.replace('(', '').replace(')', '').split(',')])
    f = open(file_name, 'r')
    file_content = f.read()
    file_content = [int(el) for el in file_content.split(" ")]
    f.close()
    create_file(decrypt_rsa(file_content, key), 'decrypted_message.txt')
    return True


def create_file(content, file_name):
    f = open(file_name, 'w')
    f.write(content)
    f.close()
