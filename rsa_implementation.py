from random import random


def generate_public_private_key(p, q):
    print(p, q)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_gcd(a, b):
    x, old_x = 0, 1
    y, old_y = 1, 0

    while b != 0:
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y


def choose_random_number(totient):
    while True:
        e = random.randrange(2, totient)

        if gcd(e, totient) == 1:
            return e


def generate_key():
    rand1 = random.randint(100, 300)
    rand2 = random.randint(100, 300)

    file = open("prime.txt", "r")
    lines = file.read().splitlines()
    file.close()

    prime1 = int(lines[rand1])
    prime2 = int(lines[rand2])

    n = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)
    e = choose_random_number(totient)

    gcd, x, y = extended_gcd(e, totient)

    if x < 0:
        d = x + totient
    else:
        d = x

    f_public = open("public_key.txt", "w")
    f_public.write(str(n) + "\n")
    f_public.write(str(e) + "\n")
    f_public.close()

    f_private = open("private_key.txt", "w")
    f_private.write(str(n) + "\n")
    f_private.write(str(d) + "\n")
    f_private.close()


def encrypt_rsa(text, key):
    text2 = bytearray()
    text2.extend(map(ord, text))

    result = [power_mod(el, *key) for el in text2]
    result2 = "".join(map(chr, result))
    return result


def decrypt_rsa(text, key):
    result_codes = [power_mod(el, *key) for el in text]
    result = "".join(map(chr, result_codes))
    return result


def power_mod(base, exp, mod):
    if mod == 1:
        return 0
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            res = res * base % mod
        exp = exp >> 1
        base = (base ** 2) % mod
    return res


def encrypt_file(public_key, file_name):
    key = tuple(
        [int(el) for el in public_key.replace("(", "").replace(")", "").split(",")]
    )
    f = open(file_name, "r")
    file_content = f.read()
    f.close()
    result = encrypt_rsa(file_content, key)
    result = " ".join([str(el) for el in result])
    create_file(result, "encrypted_message.txt")
    return result


def decrypt_file(private_key, file_name):
    key = tuple(
        [int(el) for el in private_key.replace("(", "").replace(")", "").split(",")]
    )
    f = open(file_name, "r")
    file_content = f.read()
    file_content = [int(el) for el in file_content.split(" ")]
    f.close()
    create_file(decrypt_rsa(file_content, key), "decrypted_message.txt")
    return True


def create_file(content, file_name):
    f = open(file_name, "w")
    f.write(content)
    f.close()
