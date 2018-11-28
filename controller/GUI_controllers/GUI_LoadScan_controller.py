from tkinter import *
from tkinter.filedialog import askopenfilename
from view import LoadScan_UI
from view import main_frame
from model import ModelClassifier
from os import path


class LoadScan_controller:

    """
        The Chequing or savings GUI controller.
        It creates the Chequing or savings UI
        Contains functions that the UI's buttons will use.

        decides which account is subjected to the option of withdraw or deposit
    """


    def __init__(self, master):
        self.master = master
        self.img = './view/BCIT_Logo.png'
        self.classifier = ''


        main_frame.current_frame = LoadScan_UI(self.master, self.img)
        main_frame.current_frame.Open_but.config(command=lambda: self.openFile())
        main_frame.current_frame.classify_but.config(command=lambda: self.output_classifier())
        main_frame.current_frame.show_but.config(command=lambda: self.show_mesh())
        main_frame.current_frame.can_but.config(command=lambda: self.Exit())

    def openFile(self):
        filename = askopenfilename(initialdir=path.join(path.dirname(path.realpath(".")), "pyscan/model/scans"), title="Select a file")
        fname = filename.split('/')
        main_frame.current_frame.log_File_Path.set(fname[-1])
        main_frame.current_frame.Data_listbox.insert(END, "Loading file: {}".format(fname[-1]))
        self.classifier = ModelClassifier(filename)

    def output_classifier(self):
        fname = self.classifier.filename.split('/')
        main_frame.current_frame.Data_listbox.insert(END, "Processing...")
        self.classifier.classify()
        main_frame.current_frame.Data_listbox.insert(END, "{0} is a {1:.2f}% match!".format(self.classifier.results[0], self.classifier.results[1]))
        self.classifier.show_histogram(self.classifier.existing_data, self.classifier.data, self.classifier.results[0])

    def show_mesh(self):
        self.classifier.mesh_object.show()

    def Exit(self):
        from .GUI_LoadGet_controller import LoadGet_controller
        LoadGet_controller(self.master)


if __name__ == "__main__":
    root = Tk()
    frame = CorS_UI(root)
    ui = LoadGet_controller(root)
    mainloop()
