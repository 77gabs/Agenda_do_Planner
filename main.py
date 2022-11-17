from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import sqlite3 as lite
from visualizar import *
import os
if not os.path.isfile("Bancodedados.db"):
    os.system("python banco.py")
