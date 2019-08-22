# 1.Standard Modules
import sys

# 2. Extension Modules
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# 3. Local Modules
from AudioReader import AudioReader

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.curFile = ""
        self.workingAudio = None

        self.createActions()
        self.createStatusBar()

        self.readSettings()

        # TODO: notify window for documentWasModified

    def createActions(self):
        """ Creates actions for the menu bar.

        This method overrides the base method.

        """

        # Create menu bar if not existing
        file_menu = self.menuBar().addMenu("File")

        open_action = QAction("Open", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.setStatusTip("Open an existing audio")
        open_action.triggered.connect(self.open)

        save_action = QAction("Save", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.setStatusTip("Save the current working audio")
        save_action.triggered.connect(self.save)

        save_as_action = QAction("Save As...", self)
        save_as_action.setShortcut(QKeySequence.SaveAs)
        save_as_action.setStatusTip("Save the current working audio as a new file")
        save_as_action.triggered.connect(self.saveAs)

        quit_action = QAction("Exit", self)
        quit_action.setShortcut(QKeySequence.Quit)
        quit_action.setStatusTip("Exit the program")
        quit_action.triggered.connect(self.quit)

        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(save_as_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

    def createStatusBar(self):

        # Creates the status bar if not existing and shows a message
        self.statusBar().showMessage("ready")

    def readSettings(self):
        return

    def closeEvent(self, QCloseEvent):
        """ Triggered when the user attempts to close the window, and warn the user about unsaved changes.

        This method overrides the base method.

        """

        pass

    def open(self):

        # save unsaved changes if needed
        if self.maybeSave():
            file = QFileDialog.getOpenFileName(self)
            if file != "":
                self.loadFile(file[0])

    def loadFile(self, file):

        try:
            ar = AudioReader()
            self.workingAudio = ar.read(file)

            self.curFile = file
        except Exception as e:
            msg = QMessageBox()
            msg.setWindowModality(Qt.WindowModal)
            msg.setText(str(e))
            msg.exec_()

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
        return

    def maybeSave(self):
        # TODO: implement isModified() when there is audio
        # if (!isModified())
        #     return True
        return True

    def quit(self):
        self.close()
        return

    def on_save_as_accepted(self, files):

        self.curFile = files.first()
        self.saveFile()

def main():

    app = QApplication(sys.argv)
    QCoreApplication.setOrganizationName("Gordon Poon")
    QCoreApplication.setApplicationName("Audio Pitch Moderator")

    main_window = MainWindow()
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()
