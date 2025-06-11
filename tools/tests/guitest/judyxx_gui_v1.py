import sys
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Judy Test UI")
    window.resize(400, 300)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
