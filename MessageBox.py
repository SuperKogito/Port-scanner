# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:45:41 2017
@author: SuperKogito
"""
import tkinter as tk


class CustomBox(object):

    root = None

    def __init__(self, msg, dict_key=None):
        self.top = tk.Toplevel(CustomBox.root)
        self.top.geometry('%dx%d+%d+%d' % (450, 300, 300, 300))
        self.frm = tk.Frame(self.top, borderwidth=4, relief='flat', bg='black')
        self.frm.pack(fill='both', expand=True)

        strings = ['\nList of shortcuts:',
                   '   + Ctrl + S : save file',
                   '   + Escape : close window',
                   '   + Ctrl + Alt + S : save file as',
                   'This page provides a small summary of the included features.\n',
                   '*To check you PC ports use the following ip: 127.0.0.1',
                   '*To clear your scan output use the Menubar>Edit>Clear feature',
                   '*To save the output of your scan, use the Menubar>File>Save(as)']
        # Define labels
        self.create_hint_label(msg, 0)
        self.create_hint_label(strings[4], 1)
        self.create_hint_label(strings[5], 3)
        self.create_hint_label(strings[6], 4)
        self.create_hint_label(strings[7], 5)
        self.create_hint_label(strings[0], 8)
        self.create_hint_label(strings[1], 9)
        self.create_hint_label(strings[2], 10)
        self.create_hint_label(strings[3], 11)

        self.b_frm = tk.Frame(self.top, borderwidth=4, bg='black',
                              relief='flat')
        b_cancel = tk.Button(self.b_frm, text='Go Back', bg='black',
                             fg='white')
        b_cancel.configure(background="black", foreground='white',
                           activebackground='#0080ff',
                           activeforeground='white')
        b_cancel['command'] = self.top.destroy
        b_cancel.pack(side=tk.RIGHT, padx=4, pady=4)
        self.b_frm.pack(fill='both', expand=True)

    def create_hint_label(self, text, pos):
        label = tk.Label(self.frm, text=text,
                         background='black',
                         foreground="white").grid(row=pos, column=0,
                                                  sticky=tk.W)
