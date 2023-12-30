import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QVBoxLayout, QPushButton, QInputDialog, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5 import QtCore, uic
from PyQt5.QtGui import QIcon
import pandas as pd
from render import renderer
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class VolumeRenderingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.ui = uic.loadUi('design_ui.ui', self)
        self.setWindowTitle("Volume Rendering for DICOM Files")
        self.setWindowIcon(QIcon("3d-rendering-icon.png"))
        
        # Create a QLabel
        self.label = QLabel(self)

        # Create a QIcon
        icon_path = "3d-rendering-icon.png"  # Replace with the path to your icon file
        icon = QIcon(icon_path)

        # Set the pixmap for the QLabel using the QIcon
        pixmap = icon.pixmap(300, 300)  # Specify the desired size (32x32 in this example)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        self.load_ui_elements()


    def load_ui_elements(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.label)
        
        load_button = QPushButton("Load DICOM", self)
        load_button.clicked.connect(self.upload_file)
        layout.addWidget(load_button)

    def upload_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("DICOM Files (*.dcm)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                iso_value, ok = QInputDialog.getInt(self, 'Set ISO Value', 'Enter ISO Value:')
                if ok:
                    renderer(iso_value)
           
    
        
    
    
    

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = VolumeRenderingApp()
    mainWin.show()
    sys.exit(app.exec())