def generate_public_private_key(p, q):
    print(p, q)

def encrypt_file(file_name):
    f = open(file_name, 'r')
    file_content = f.read()
    f.close()
    print(file_content)
    create_encrypted_file(file_content)


def create_encrypted_file(content):
    f = open('encrypted_message.txt', 'w')
    f.write(content)
    f.close()
