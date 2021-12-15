#!/bin/python3
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename
import sys
import argparse

class Application(tk.Frame):
    def __init__(self, master=None,entry="/home", file_flag=False):
        super().__init__(master)
        self.file_flag = file_flag
        self.entry = entry
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        if(self.file_flag==True):
            selected_usb_device = askopenfilename(initialdir = self.entry)
        else:
            selected_usb_device = askdirectory(initialdir = self.entry)
        
        print(selected_usb_device)
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Select folder')
    parser.add_argument('-e', '--entry', help='entry point folder')
    parser.add_argument('-f', '--file', help='Using file dialog.', action='store_true')
    args = parser.parse_args()

    root = tk.Tk()
    if args.entry:
        app = Application(master=root, entry=args.entry, file_flag=args.file)
    else:
        app = Application(master=root, entry="/home", file_flag=args.file)
    app.mainloop()
