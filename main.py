import pathlib
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pygubu

from rsa_implementation import generate_public_private_key

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
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object('main_window', master)
        builder.connect_callbacks(self)
        self.builder.get_variable('p_var').set(7)
        self.builder.get_variable('q_var').set(11)

    def run(self):
        self.mainwindow.mainloop()

    def generate_public_private_key_call(self):
        p = int(self.builder.get_variable('p_var').get())
        q = int(self.builder.get_variable('q_var').get())
        generate_public_private_key(p, q)
        self.insert_output_text('Generated keys')
        message_popup('Generated keys', 'Generated keys')

    def encrypt_message_call(self):
        pass

    def decrypt_message_call(self):
        pass

    def select_file_call(self):
        filename = filedialog.askopenfilename(title='Select an image')
        self.insert_output_text(filename)

        pass

    def encrypt_file_call(self):
        pass

    def decrypt_file_call(self):
        pass

    def insert_output_text(self, text):
        print(text)
        self.builder.get_variable('output_var').set(text)


if __name__ == '__main__':
    app = RsaAlgorytmGuiApp()
    app.run()
