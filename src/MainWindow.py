# 1.Standard Modules
import sys

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# 3. Local Modules


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.curFile = ""

        self.createActions()
        self.createStatusBar()

        self.readSettings()

        # TODO: notify window for documentWasModified

    def createAction(self):

    def createStatusBar(self):

    def readSettings(self):

    def closeEvent(self, QCloseEvent):

    def open(self):

        # save unsaved changes if needed
        if self.maybeSave():
            file = QFileDialog.getOpenFileName(this)
            if file != "":
                self.loadFile(file)

    def loadFile(self, file):

        try:
            # TODO: load file

            self.curFile = file
        except Exception as e:
            print(str(e))

    def save(self):

        if self.curFile == "":
            self.saveAs()
        else:
            self.saveFile()

    def saveAs(self):

        # Configure the file dialog
        dialog = QFileDialog(self)
        dialog.setWindowModality(Qt.WindowModal)
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.accepted.connect(lambda : self.on_save_as_accepted(dialog.selectedFiles()))

        dialog.open()

    def saveFile(self):

    def on_save_as_accepted(self, files):

        self.curFile = files.first()
        self.saveFile()

def main():

    app = QApplication(sys.argv)
    app.exec()

if __name__ == "__main__":
    main()
