from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen

class HeartbeatWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pulse = 0
        self.increasing = True
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_pulse)
        self.timer.start(50)  # 20 FPS

    def update_pulse(self):
        if self.increasing:
            self.pulse += 5
            if self.pulse >= 100:
                self.increasing = False
        else:
            self.pulse -= 5
            if self.pulse <= 0:
                self.increasing = True
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        size = min(self.width(), self.height())
        radius = size / 4 + (self.pulse / 10)  # Pulse effect

        painter.setPen(QPen(QColor(255, 0, 0)))
        painter.setBrush(QColor(255, 0, 0, 150))
        center = self.rect().center()
        painter.drawEllipse(center, radius, radius)
