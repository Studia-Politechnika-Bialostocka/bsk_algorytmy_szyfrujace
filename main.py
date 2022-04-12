import pathlib
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pygubu

from rsa_implementation import generate_public_private_key, encrypt_rsa, decrypt_rsa, create_file

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "rsa_algorytm_gui.ui"


def message_popup(title, text, type_message='info'):
    if type_message == 'info':
        tk.messagebox.showinfo(title, text)
    elif type_message == 'warning':
        tk.messagebox.showwarning(title, text)
    elif type_message == 'error':
        tk.messagebox.showerror(title, text)


class RsaAlgorytmGuiApp:
    def __init__(self, master=None):
        self.filename = None
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('main_window', master)
        builder.connect_callbacks(self)
        self.builder.get_variable('p_var').set(11)
        self.builder.get_variable('q_var').set(13)
        self.builder.get_variable('public_key_var').set('(7, 143)')
        self.builder.get_variable('private_key_var').set('(223, 143)')

    def run(self):
        self.mainwindow.mainloop()

    def generate_public_private_key_call(self):
        p = int(self.builder.get_variable('p_var').get())
        q = int(self.builder.get_variable('q_var').get())
        generate_public_private_key(p, q)
        self.insert_output_text('Generated keys')
        message_popup('Generated keys', 'Generated keys')

    def encrypt_message_call(self):
        public_key = self.builder.get_variable('public_key_var').get()
        key = tuple([int(el) for el in public_key.replace('(', '').replace(')', '').split(',')])
        message = self.builder.get_variable('message_var').get()
        result = encrypt_rsa(message, key)
        self.insert_output_text(result)

    def decrypt_message_call(self):
        private_key = self.builder.get_variable('private_key_var').get()
        key = tuple([int(el) for el in private_key.replace('(', '').replace(')', '').split(',')])
        message = [int(el) for el in self.builder.get_variable('message_var').get().split(' ')]
        result = decrypt_rsa(message, key)
        self.insert_output_text(result)

    def select_file_call(self):
        filename = filedialog.askopenfilename(title='Select an image')
        if filename:
            self.filename = filename
            self.insert_output_text(filename)

        pass

    def encrypt_file_call(self):
        if self.filename is None:
            message_popup('No file selected', 'No file selected')
            return
        else:
            public_key = self.builder.get_variable('public_key_var').get()
            key = tuple([int(el) for el in public_key.replace('(', '').replace(')', '').split(',')])
            f = open(self.filename, 'r')
            message = f.read()
            f.close()
            result = encrypt_rsa(message, key)
            # convert list to string
            result = ' '.join([str(el) for el in result])
            self.insert_output_text(result)
            create_file(result, "encrypted_message.txt")
            message_popup('Encrypted file', 'Encrypted file')

    def decrypt_file_call(self):
        if self.filename is None:
            message_popup('No file selected', 'No file selected')
            return
        else:
            private_key = self.builder.get_variable('private_key_var').get()
            key = tuple([int(el) for el in private_key.replace('(', '').replace(')', '').split(',')])
            f = open(self.filename, 'r')
            message = f.read()
            message = [int(el) for el in message.split(" ")]
            f.close()
            result = decrypt_rsa(message, key)
            self.insert_output_text(result)
            create_file(result, "decrypted_message.txt")
            message_popup('Decrypted file', 'Decrypted file')



        pass

    def insert_output_text(self, text):
        if not text:
            message_popup('No text', 'No text')
        print(text)
        self.builder.get_variable('output_var').set(text)


if __name__ == '__main__':
    app = RsaAlgorytmGuiApp()
    app.run()
