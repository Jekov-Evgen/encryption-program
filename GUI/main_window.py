from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from Logic.logics import encryptionAlgorithm
from GUI.style import CONST_MAIN_WINDOW, CONST_POP_WINDOW
from PyQt6.QtWidgets import QMainWindow, QLabel, QFileDialog, QMessageBox, QPushButton, QVBoxLayout, QWidget

def pop_window(title_window : str, text_window : str):
    window = QMessageBox()
    window.setWindowIcon(QIcon("image\icon.webp"))
    window.setStyleSheet(CONST_POP_WINDOW)
    window.setWindowTitle(title_window)
    window.setText(text_window)
    window.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шифратор текста")
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.setWindowIcon(QIcon("image\icon.webp"))
        self.work = encryptionAlgorithm()
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        greet = QLabel(text="Приветсвуем выберите нужный файл и операцию")
        
        encryption = QPushButton(text="Зашифровать файл")
        encryption.clicked.connect(self.cipher)
        
        decryption = QPushButton(text="Расшифровать файл")
        decryption.clicked.connect(self.decipher)
        
        control_UI.addWidget(greet, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(encryption)
        control_UI.addWidget(decryption)
        
        central_widget.setLayout(control_UI)
        self.setCentralWidget(central_widget)
        self.show()
        
    def cipher(self):
        try:
            path = QFileDialog.getOpenFileName(self, 
                                               "Выберите файл для шифровки", 
                                               "", 
                                               "Текстовые файлы (*.txt)")
            
            self.work.encryption(path[0])
            pop_window("Успех", "Успешная шифровка")
        except:
            pop_window("Ошибка", "Скорее всего проблема с файлом")
            
    def decipher(self):
        try:
            path = QFileDialog.getOpenFileName(self, 
                                               "Выберите файл для шифровки", 
                                               "", 
                                               "Текстовые файлы (*.txt)")
            
            self.work.decryption(path[0])
            pop_window("Успех", "расшифровка")
        except:
            pop_window("Ошибка", "Скорее всего проблема с файлом")