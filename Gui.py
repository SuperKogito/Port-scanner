# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 02:17:24 2017
@author: SuperKogito
"""
# Define imports
import socket
import tkinter as tk
from contextlib import closing
from MessageBox import CustomBox
from ListBox import MultiColumnListbox
from tkinter import ttk, Label, Entry, LabelFrame, filedialog


class MainWindow(tk.Tk):
    """ Main window class """
    def __init__(self, title):
        super().__init__()
        xyla = [0, 0, 250, 550]
        self.ext = ''
        self.original_path = ''
        self.title(title)
        self.minsize(xyla[2], xyla[3])
        self.resizable(0, 0)
        self.configure(background='black')
        self.geometry("%dx%d+%d+%d" % (xyla[0], xyla[1], 400, 100))
        # Define bind events
        self.bind("<Control-s>", self.file_save)
        self.bind("<Control-S>", self.file_save_as)
        self.bind("<Escape>", self.quit_func)
        # Define colors
        colors = ["#0080ff", "white", "black"]
        # Define style
        ttk.Style().configure("TNotebook", background=colors[2])
        ttk.Style().map("TNotebook.Tab",
                        background=[("selected", colors[0])],
                        foreground=[("selected", colors[1])])

        self.listbox = MultiColumnListbox()
        self.frame = LabelFrame(self, text=" Input Text ", bg="black",
                                fg='white')
        self.create_entries()
        self.create_button()
        self.create_menu()
        self.mainloop()

    def create_entries(self):
        labels = ["IP adress", "Starting Port", "Ending Port"]
        self.l1 = Label(self.frame, bg="black", fg='white', text=labels[0])
        self.e1 = Entry(self.frame)
        self.l2 = Label(self.frame, bg="black", fg='white', text=labels[1])
        self.e2 = Entry(self.frame)
        self.l3 = Label(self.frame, bg="black", fg='white', text=labels[2])
        self.e3 = Entry(self.frame)
        e_list = [(self.l1, self.e1), (self.l2, self.e2), (self.l3, self.e3)]
        for element in e_list:
            element[0].pack()
            element[1].pack(padx=5, pady=5)

    def create_button(self):
        b2 = tk.Button(self.frame, text='Start', command=self.iterate)
        b2.pack(side=tk.RIGHT, padx=5, pady=5)
        b2.configure(background="black", foreground='white',
                     activebackground='#0080ff', activeforeground='white')
        self.frame.pack(expand=1, fill="both", padx=5, pady=5)

    def create_menu(self):
        self.menu = tk.Menu(self, tearoff=False)
        # Menu item File
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", underline=0, menu=self.filemenu)
        self.filemenu.add_command(label="Save", underline=1,
                                  command=self.file_save,
                                  accelerator="Ctrl+s")
        self.filemenu.add_command(label="Save As...", underline=5,
                                  command=self.file_save_as,
                                  accelerator="Ctrl+shift+s")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", underline=2,
                                  command=self.quit_func, accelerator="Esc")
        # Menu item Edit
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", underline=0, menu=self.editmenu)
        self.editmenu.add_command(label="Clear", underline=2,
                                  command=self.edit_clear)
        # Menu item Help
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", underline=0, menu=self.helpmenu)
        self.helpmenu.add_command(label="Manual", command=self.help_manual)
        # Coloring the menu
        for menu_element in (self.filemenu, self.editmenu, self.helpmenu):
            menu_element.configure(bg='black', fg='white',
                                   activebackground='#0080ff',
                                   activeforeground='white')
        self.config(menu=self.menu)
        self.menu.configure(background='black', foreground='white',
                            activebackground='#0080ff',
                            activeforeground='white')

    def quit_func(self, event=None):
        self.destroy()

    def return_data(self):
        data = ''
        for child in self.listbox.tree.get_children():
            values = self.listbox.tree.item(child)['values']
            line = values[1][:4] + ' ' + str(values[0]) + values[1][4:]
            data += line + '\n'
        return data

    def file_save(self, event=None):
        """Handle click on 'Save' menu."""
        contents = self.return_data()
        try:
            with open(self.file_name, 'w') as output_file:
                output_file.write(contents)
        except AttributeError:
            self.file_save_as()

    def file_save_as(self, event=None):
        """Handle click on 'Save as' menu."""
        data = self.return_data()
        self.write_to_file(data)

    def write_to_file(self, data):
        self.file_name = filedialog.asksaveasfilename(parent=self,
                                                      filetypes=[('Text',
                                                                 '*.txt')],
                                                      title='Save as...')
        writer = open(self.file_name, 'w')
        writer.write(data)
        print(self.file_name)
        writer.close()

    # Edit menu functions
    def edit_clear(self, event=None):
        for i in self.listbox.tree.get_children():
            self.listbox.tree.delete(i)

    def help_manual(self):
        text = ('\nThank you for using port scanner.')
        self.box = CustomBox(text)

    def check_socket(self, host, port):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((host, port)) == 0:
                self.listbox.tree.insert("", 0, text="Line 1",
                                         values=(port, "Port is open"),
                                         tags=('open',))
                self.listbox.tree.tag_configure('open', background='green')
            else:
                self.listbox.tree.insert("", 0, text="Line 1",
                                         values=(port, "Port is not open"),
                                         tags=('not_open',))
                self.listbox.tree.tag_configure('not_open', background='red')

    def iterate(self, event=None):
        ip = self.e1.get()
        starting_port = self.e2.get()
        ending_port = self.e3.get()
        self.edit_clear()

        for port in range(int(starting_port), int(ending_port)+1):
            self.check_socket(ip, port)
