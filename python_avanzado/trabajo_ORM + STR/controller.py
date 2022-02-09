from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import tkinter

import sqlite3
from sqlite3 import Error

from vista import Ventana


class Controller:
    """
    Clase Controller, esta destinado a instanciar la clase ventana
    """

    def __init__(self, root):
        """
        Metodo Init de la Clase Controller
        """
        self.root_controller = root
        obj = Ventana(self.root_controller)


if __name__ == "__main__":
    root = Tk()
    objeto = Controller(root)
    root.mainloop()
