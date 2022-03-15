import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "algorytmy_gui.ui"


class AlgorytmyGuiApp:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.header_label = tk.Label(self.main_window)
        self.header_label.configure(font='{Bahnschrift SemiLight SemiConde} 36 {bold}', text='Algorytmy blokowe')
        self.header_label.pack(side='top')
        self.frame1 = ttk.Frame(self.main_window)
        self.code_input_label = tk.Label(self.frame1)
        self.code_input_label.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Input Code  ')
        self.code_input_label.pack(side='left')
        self.code_input = ttk.Entry(self.frame1)
        self.code_input.configure(width='80')
        self.code_input.pack(anchor='center', fill='y', side='right')
        self.frame1.configure(height='200', width='200')
        self.frame1.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame3 = tk.Frame(self.main_window)
        self.label4 = tk.Label(self.frame3)
        self.label4.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Rail fence   ')
        self.label4.pack(side='left')
        self.label5 = tk.Label(self.frame3)
        self.label5.configure(text='liczba poziomów (n)')
        self.label5.pack(side='left')
        self.rail_fence_n_input = tk.Spinbox(self.frame3)
        self.rail_fence_n_input.configure(from_='0', increment='1', justify='center', to='9')
        self.rail_fence_n_input.delete(0, 'end')
        self.rail_fence_n_input.insert(0, '3')
        self.rail_fence_n_input.pack(fill='y', padx='10', side='left')
        self.button1 = tk.Button(self.frame3)
        self.button1.configure(text='Szyfruj')
        self.button1.pack(fill='y', ipadx='10', side='left')
        self.button1.configure(command=self.rail_fence_encrypt)
        self.frame3.configure(height='200', width='200')
        self.frame3.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame4 = tk.Frame(self.main_window)
        self.label6 = tk.Label(self.frame4)
        self.label6.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Przestawienie macierzowe a  ')
        self.label6.pack(side='left')
        self.label7 = tk.Label(self.frame4)
        self.label7.configure(text='klucz kodujący')
        self.label7.pack(side='left')
        self.matrix_conversion1_input = tk.Entry(self.frame4)
        self.matrix_conversion1_input.configure(justify='center')
        self.matrix_conversion1_input.pack(fill='y', padx='10', side='left')
        self.button2 = tk.Button(self.frame4)
        self.button2.configure(text='Szyfruj')
        self.button2.pack(fill='y', ipadx='10', side='left')
        self.button2.configure(command=self.matrix_conversion1_encrypt)
        self.frame4.configure(height='200', width='200')
        self.frame4.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame5 = tk.Frame(self.main_window)
        self.label8 = tk.Label(self.frame5)
        self.label8.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Przestawienie macierzowe b  ')
        self.label8.pack(side='left')
        self.label9 = tk.Label(self.frame5)
        self.label9.configure(text='klucz kodujący')
        self.label9.pack(side='left')
        self.matrix_conversion2_input = tk.Entry(self.frame5)
        self.matrix_conversion2_input.configure(justify='center')
        self.matrix_conversion2_input.pack(fill='y', padx='10', side='left')
        self.button3 = tk.Button(self.frame5)
        self.button3.configure(text='Szyfruj')
        self.button3.pack(fill='y', ipadx='10', side='left')
        self.button3.configure(command=self.matrix_conversion2_encrypt)
        self.frame5.configure(height='200', width='200')
        self.frame5.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame6 = tk.Frame(self.main_window)
        self.label10 = tk.Label(self.frame6)
        self.label10.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Output   ')
        self.label10.pack(side='left')
        self.output_input = ttk.Entry(self.frame6)
        self.output_input.configure(width='80')
        self.output_input.pack(anchor='center', fill='y', side='right')
        self.frame6.configure(height='200', width='200')
        self.frame6.pack(anchor='w', padx='20', pady='50', side='top')
        self.main_window.configure(height='200', width='200')
        self.main_window.geometry('640x400')

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def rail_fence_encrypt(self):
        code_input = self.code_input.get()
        rail_fence_n = self.rail_fence_n_input.get()

        self.insert_code(code_input)

        pass

    def insert_code(self, code):
        self.output_input.delete(0, 'end')
        self.output_input.insert(0, code)

    def matrix_conversion1_encrypt(self):
        pass

    def matrix_conversion2_encrypt(self):
        pass


if __name__ == '__main__':
    app = AlgorytmyGuiApp()
    app.run()


