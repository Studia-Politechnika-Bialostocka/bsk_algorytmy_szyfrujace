import tkinter
from tkinter import filedialog
import pathlib
import tkinter as tk
import tkinter.ttk as ttk

from algorytmy_impl import PM, PM2, PM2_decrypt, PM_decrypt, RF1, RF2

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "algorytmy_gui.ui"


class AlgorytmyGuiApp:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.header_label = tk.Label(self.main_window)
        self.header_label.configure(font='{Bahnschrift SemiLight SemiConde} 36 {bold}', text='Block algorithms')
        self.header_label.pack(side='top')
        self.frame7 = tk.Frame(self.main_window)
        self.label1 = tk.Label(self.frame7)
        self.label1.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Input Code')
        self.label1.pack(side='left')
        self.code_input = ttk.Entry(self.frame7)
        self.code_input.configure(width='65')
        self.code_input.pack(anchor='center', fill='y', padx='10', side='left')
        self.__tkvar = tk.StringVar(value='Encrypt')
        __values = ['Decrypt']
        self.algorithm_option = tk.OptionMenu(self.frame7, self.__tkvar, 'Encrypt', *__values, command=None)
        self.algorithm_option.pack(fill='y', side='top')
        self.frame7.configure(height='200', width='200')
        self.frame7.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame8 = tk.Frame(self.main_window)
        self.label2 = tk.Label(self.frame8)
        self.label2.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Rail fence   ')
        self.label2.pack(side='left')
        self.label3 = tk.Label(self.frame8)
        self.label3.configure(text='number of levels (n)')
        self.label3.pack(side='left')
        self.rail_fence_n_input = tk.Spinbox(self.frame8)
        self.rail_fence_n_input.configure(from_='0', increment='1', justify='center', to='10')
        self.rail_fence_n_input.configure(width='2')
        self.rail_fence_n_input.delete(0, 'end')
        self.rail_fence_n_input.insert(0, '3')
        self.rail_fence_n_input.pack(fill='y', padx='10', side='left')
        self.rail_fence_run_button = tk.Button(self.frame8)
        self.rail_fence_run_button.configure(text='Run')
        self.rail_fence_run_button.pack(fill='y', ipadx='10', side='left')
        self.rail_fence_run_button.configure(command=self.rail_fence_run)
        self.frame8.configure(height='200', width='200')
        self.frame8.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame9 = tk.Frame(self.main_window)
        self.label15 = tk.Label(self.frame9)
        self.label15.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Matrix conversion a  ')
        self.label15.pack(side='left')
        self.label16 = tk.Label(self.frame9)
        self.label16.configure(text='coding key:')
        self.label16.pack(side='left')
        self.matrix_conversion_a_key_input = tk.Entry(self.frame9)
        self.matrix_conversion_a_key_input.configure(justify='center', width='15')
        self.matrix_conversion_a_key_input.delete(0, 'end')
        self.matrix_conversion_a_key_input.insert(0, '3-4-1-5-2')
        self.matrix_conversion_a_key_input.pack(fill='y', padx='10', side='left')
        self.label17 = tk.Label(self.frame9)
        self.label17.configure(text='d:')
        self.label17.pack(side='left')
        self.matrix_conversion_a_d_input = tk.Spinbox(self.frame9)
        self.matrix_conversion_a_d_input.configure(from_='0', increment='1', justify='center', to='10')
        self.matrix_conversion_a_d_input.configure(width='2')
        self.matrix_conversion_a_d_input.delete(0, 'end')
        self.matrix_conversion_a_d_input.insert(0, '5')
        self.matrix_conversion_a_d_input.pack(fill='y', padx='10', side='left')
        self.button6 = tk.Button(self.frame9)
        self.button6.configure(text='Run')
        self.button6.pack(fill='y', ipadx='10', side='left')
        self.button6.configure(command=self.matrix_conversion1_run)
        self.frame9.configure(height='200', width='200')
        self.frame9.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame10 = tk.Frame(self.main_window)
        self.label21 = tk.Label(self.frame10)
        self.label21.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Matrix conversion b  ')
        self.label21.pack(side='left')
        self.label22 = tk.Label(self.frame10)
        self.label22.configure(text='coding key:')
        self.label22.pack(side='left')
        self.matrix_conversion_b_key_input = tk.Entry(self.frame10)
        self.matrix_conversion_b_key_input.configure(justify='center', width='15')
        self.matrix_conversion_b_key_input.delete(0, 'end')
        self.matrix_conversion_b_key_input.insert(0, '3-4-1-5-2')
        self.matrix_conversion_b_key_input.pack(fill='y', padx='10', side='left')
        self.button8 = tk.Button(self.frame10)
        self.button8.configure(text='Run')
        self.button8.pack(fill='y', ipadx='10', side='left')
        self.button8.configure(command=self.matrix_conversion2_run)
        self.frame10.configure(height='200', width='200')
        self.frame10.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame1 = tk.Frame(self.main_window)
        self.label4 = tk.Label(self.frame1)
        self.label4.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Pseudo-random number generator')
        self.label4.pack(side='left')
        self.label5 = tk.Label(self.frame1)
        self.label5.configure(text='𝜑(𝑥)')
        self.label5.pack(side='left')
        self.entry1 = tk.Entry(self.frame1)
        self.entry1.configure(justify='center', width='15')
        self.entry1.delete(0, 'end')
        self.entry1.insert(0, '4-1')
        self.entry1.pack(fill='y', padx='10', side='left')
        self.button1 = tk.Button(self.frame1)
        self.button1.configure(text='Run')
        self.button1.pack(fill='y', ipadx='10', side='left')
        self.button1.configure(command=self.random_generator_run)
        self.frame1.configure(height='200', width='200')
        self.frame1.pack(anchor='w', padx='20', pady='10', side='top')
        self.frame11 = tk.Frame(self.main_window)
        self.label27 = tk.Label(self.frame11)
        self.label27.configure(font='{Bahnschrift SemiLight SemiConde} 16 {}', text='Output   ')
        self.label27.pack(side='left')
        self.code_output = ttk.Entry(self.frame11)
        self.code_output.configure(width='80')
        self.code_output.pack(anchor='center', fill='y', side='right')
        self.frame11.configure(height='200', width='200')
        self.frame11.pack(anchor='w', padx='20', pady='50', side='top')
        self.main_window.configure(height='200', width='200')
        self.main_window.geometry('640x500')

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def insert_output_code(self, code):
        self.code_output.delete(0, 'end')
        self.code_output.insert(0, code)

    def message_popup(self, title, text, type_message='info'):
        if type_message == 'info':
            tk.messagebox.showinfo(title, text)
        elif type_message == 'warning':
            tkinter.messagebox.showwarning(title, text)
        elif type_message == 'error':
            tk.messagebox.showerror(title, text)

    def rail_fence_run(self):
        code_input = self.code_input.get()
        if not code_input:
            self.message_popup('Błąd', 'Nie wprowadzono kodu!', 'warning')
            return
        rail_fence_n = self.rail_fence_n_input.get()
        if self.__tkvar.get() == 'Encrypt':
            self.insert_output_code(RF1(code_input, int(rail_fence_n)))
        else:
            self.insert_output_code(RF2(code_input, int(rail_fence_n)))

    def matrix_conversion1_run(self):
        code_input = self.code_input.get()
        if not code_input:
            self.message_popup('Błąd', 'Nie wprowadzono kodu!', 'warning')
            return

        d = int(self.matrix_conversion_a_d_input.get())
        coding_key = self.matrix_conversion_a_key_input.get()
        coding_key = [int(s) for s in coding_key.split('-')]

        if len(coding_key) != d:
            self.message_popup('Błąd', 'Ilość kolumn w kluczu musi się równać d!', 'error')
            return
        for col in coding_key:
            if col > d:
                self.message_popup('Błąd', f'Liczby w kluczu nie mogą być większe od d! ({col} > {d})', 'error')
                return
        
        if self.__tkvar.get() == 'Encrypt':
            self.insert_output_code(PM(code_input, d=d, key=coding_key))
        else:
            self.insert_output_code(PM_decrypt(code_input, d=d, key=coding_key))

    def matrix_conversion2_run(self):
        code_input = self.code_input.get()
        if not code_input:
            self.message_popup('Błąd', 'Nie wprowadzono kodu!', 'warning')
            return

        coding_key = self.matrix_conversion_a_key_input.get()
        if self.__tkvar.get() == 'Encrypt':
            self.insert_output_code(PM2(code_input, coding_key))
        else:
            self.insert_output_code(PM2_decrypt(code_input, coding_key))

    def random_generator_run(self):
        input_key = self.entry1.get()
        key = [int(s) for s in input_key.split('-') if int(s) != 1]
        generated_code = ""
        state = 6
        for _ in range(128):
            generated_code += str(state & 1)
            print(state & 1, end='')
            for i in key:
                newbit = state ^ (state >> i - 1)
            newbit = newbit & 1
            state = (state >> 1) | (newbit << 3)

        self.insert_output_code(generated_code*100)



if __name__ == '__main__':
    app = AlgorytmyGuiApp()
    app.run()
