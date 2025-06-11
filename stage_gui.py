from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QMovie
import sys

class StageGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JudyXX Stage")
        self.setGeometry(100, 100, 800, 600)

        # Background animation
        self.bg_label = QLabel(self)
        self.bg_movie = QMovie("assets/scenes/whiteboard_idle.gif")
        self.bg_label.setMovie(self.bg_movie)
        self.bg_movie.start()
        self.bg_label.lower()

        # Avatar animation
        self.avatar = QLabel(self)
        self.avatar_movie = QMovie("assets/avatars/judy_idle.gif")
        self.avatar.setMovie(self.avatar_movie)
        self.avatar_movie.start()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.bg_label)
        layout.addWidget(self.avatar)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StageGUI()
    window.show()
    sys.exit(app.exec_())
