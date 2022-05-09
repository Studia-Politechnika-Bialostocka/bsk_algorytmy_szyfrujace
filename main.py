import os
import pathlib
import tkinter as tk
from tkinter import filedialog
import pygubu

from rsa_implementation import generate_public_private_key, encrypt_rsa, decrypt_rsa, create_file, decrypt_file, \
    encrypt_file, getKeys

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
        self.message = None
        self.private_key = None
        self.public_key = None
        self.filename = None
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('main_window', master)
        builder.connect_callbacks(self)
        self.builder.get_variable('p_var').set(11)
        self.builder.get_variable('q_var').set(13)

    def run(self):
        self.mainwindow.mainloop()

    def generate_public_private_key_call(self):
        p = int(self.builder.get_variable('p_var').get())
        q = int(self.builder.get_variable('q_var').get())
        pub_key, private_key = getKeys(p, q)
        self.builder.get_variable('public_key_var').set(pub_key)
        self.builder.get_variable('private_key_var').set(private_key)
        self.insert_output_text('Generated keys')
        message_popup('Generated keys', 'Generated keys')

    def encrypt_message_call(self):
        self.validate_input_message() and self.update_variables()
        key = tuple([int(el) for el in self.public_key.replace('(', '').replace(')', '').split(',')])
        message = self.builder.get_variable('message_var').get()
        result = encrypt_rsa(message, key)
        self.insert_output_text(result)

    def decrypt_message_call(self):
        self.validate_input_message() and self.update_variables()
        key = tuple([int(el) for el in self.private_key.replace('(', '').replace(')', '').split(',')])
        message = [int(el) for el in self.builder.get_variable('message_var').get().split(' ')]
        result = decrypt_rsa(message, key)
        self.insert_output_text(result)

    def select_file_call(self):
        filename = filedialog.askopenfilename(title='Select an image')
        if filename:
            self.filename = filename
            self.insert_output_text(filename)

    def encrypt_file_call(self):
        if not self.file_exists():
            return
        self.update_variables()
        result = encrypt_file(self.public_key, self.filename)
        if result is not None:
            message_popup('Encrypted file', 'Encrypted file')
            self.open_file("encrypted_message.txt")

    def decrypt_file_call(self):
        if not self.file_exists():
            return
        self.update_variables()
        result = decrypt_file(self.private_key, self.filename)
        if result is not None:
            message_popup('Decrypted file', 'Decrypted file')
            self.open_file("decrypted_message.txt")

    def insert_output_text(self, text):
        if not text:
            message_popup('No output text', 'No output text')
        print(text)
        self.builder.get_variable('output_var').set(text)

    def validate_input_message(self):
        message = self.builder.get_variable('message_var').get()
        if not message:
            message_popup('No message', 'No message')
            return False
        return True

    def update_variables(self):
        self.public_key = self.builder.get_variable('public_key_var').get()
        self.private_key = self.builder.get_variable('private_key_var').get()
        self.message = self.builder.get_variable('message_var').get()
        self.builder.get_variable('output_var').set('')

    def file_exists(self):
        if self.filename is None:
            message_popup('No file selected', 'No file selected')
            return False
        else:
            return True

    def open_file(self, filename=None):
        if self.file_exists():
            if filename is None:
                filename = self.filename
            os.startfile(filename)


if __name__ == '__main__':
    app = RsaAlgorytmGuiApp()
    app.run()
