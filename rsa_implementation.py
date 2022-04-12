def generate_public_private_key(p, q):
    print(p, q)

def encrypt_file(file_name):
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()
    print(file_content)
    create_file(file_content, 'encrypted_' + file_name)

def decrypt_file(file_name):
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()
    print(file_content)
    create_file(file_content, 'decrypted_' + file_name)

def create_file(content, file_name):
    f = open(file_name, 'w')
    f.write(content)
    f.close()
