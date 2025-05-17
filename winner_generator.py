from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
def show_winner():
    if btn.text() == 'Alt + F4':
        window.close()
    if texxt.text() == '?':
        random_number = randint(1, 100)
        texxt.setText(str(random_number))
        text.setText('Победитель:')
        btn.setText('Alt + F4')
app = QApplication([])
window = QWidget()
window.setWindowTitle('gambling')
window.resize(400, 200)
text = QLabel('Нажми, чтобы узнать победителя')
texxt = QLabel('?')
btn = QPushButton('Сгенерировать')
btn.clicked.connect(show_winner)
v_line = QVBoxLayout()
v_line.addWidget(text, alignment= Qt.AlignCenter)
v_line.addWidget(texxt, alignment= Qt.AlignCenter)
v_line.addWidget(btn, alignment= Qt.AlignCenter)
window.setLayout(v_line)
window.show()
app.exec()