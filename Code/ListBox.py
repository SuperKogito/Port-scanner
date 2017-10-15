# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 02:00:22 2017
@author: SuperKogito
"""
from tkinter import ttk, LabelFrame


class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self):
        self.tree = None
        # the test data ...
        self.list_header = ['Port', 'Status']
        self.item_list = [('', '')]
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self):
        container = LabelFrame(text=" Output Text ", bg="black", fg='white')
        container.pack(expand=1, fill="both", padx=5, pady=5)
        # create a treeview with dual scrollbars
        ttk.Style().configure("Treeview", background="black",
                              foreground="white", fieldbackground="black")
        self.tree = ttk.Treeview(columns=self.list_header, show="headings")
        self.tree.column('Port', width=0)
        self.tree.column('Status', width=40)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container,
                       padx=5, pady=5)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in self.list_header:
            self.tree.heading(col, text=col.title())
        for item in self.item_list:
            self.tree.insert('', 'end', values=item)
