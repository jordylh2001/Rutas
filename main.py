import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets
import numpy as np
# Settings for the Window and the content
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QMenu, QPushButton, QLabel


class Settings:
    WIDTH = 20
    HEIGHT = 15
    NUM_BLOCKS_X = 40
    NUM_BLOCKS_Y = 20


class QS(QtWidgets.QGraphicsScene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        width = Settings.NUM_BLOCKS_X * Settings.WIDTH
        height = Settings.NUM_BLOCKS_Y * Settings.HEIGHT
        self.setSceneRect(0, 0, width, height)
        self.setItemIndexMethod(QtWidgets.QGraphicsScene.NoIndex)


class QV(QtWidgets.QGraphicsView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # draw all the background
    def drawBackground(self, painter, rect):
        gr = rect.toRect()
        start_x = gr.left() + Settings.WIDTH - (gr.left() % Settings.WIDTH)
        start_y = gr.top() + Settings.HEIGHT - (gr.top() % Settings.HEIGHT)
        painter.save()
        painter.setPen(QtGui.QColor(60, 70, 80).lighter(90))
        painter.setOpacity(0.7)

        for x in range(start_x, gr.right(), Settings.WIDTH):
            painter.drawLine(x, gr.top(), x, gr.bottom())

        for y in range(start_y, gr.bottom(), Settings.HEIGHT):
            painter.drawLine(gr.left(), y, gr.right(), y)

        painter.restore()

        super().drawBackground(painter, rect)


class Main(QtWidgets.QMainWindow):
    opc = 0
    obj = 0
    green = [0, 0]
    red = [0, 0]
    wall = np.array([[]])

    def __init__(self):
        super().__init__()
        self.view = None
        self.initUI()

    def mousePressEvent(self, QMouseEvent):
        global opc, obj
        pos = QMouseEvent.pos()
        color = ""
        
        if opc == 1:
            if obj == 1:
                color = "green"
            if obj == 2:
                color = "Red"
            if obj == 3:
                color = "Wall"

        if opc == 2:
            if obj == 1:
                color = "Green"
            if obj == 2:
                color = "Red"
            if obj == 3:
                color = "Wall"
            # print(color)
        print("Press", QMouseEvent.pos())

    def initUI(self):
        # adding actions to file menu
        # self.setWindowIcon(QIcon('upv.png'))
        self.setWindowTitle("Rutas")
        self.setGeometry(100, 100, 1250, 850)

        # pintar
        label1 = QLabel(self)
        label1.setText("Paint")
        label1.setGeometry(880, 100, 100, 30)
        button1 = QPushButton("Green", self)
        button1.setGeometry(850, 150, 100, 30)
        button1.clicked.connect(self.paintGreen)
        button2 = QPushButton("Red", self)
        button2.setGeometry(850, 250, 100, 30)
        button2.clicked.connect(self.paintRed)
        button3 = QPushButton("Wall", self)
        button3.setGeometry(850, 350, 100, 30)
        button3.clicked.connect(self.paintWall)

        # borrar
        label2 = QLabel(self)
        label2.setText("Delete")
        label2.setGeometry(1030, 100, 100, 30)
        button4 = QPushButton("Green", self)
        button4.setGeometry(1000, 150, 100, 30)
        button4.clicked.connect(self.deleteGreen)
        button5 = QPushButton("Red", self)
        button5.setGeometry(1000, 250, 100, 30)
        button5.clicked.connect(self.deleteRed)
        button6 = QPushButton("Wall", self)
        button6.setGeometry(1000, 350, 100, 30)
        button6.clicked.connect(self.deleteWall)

        # Boton de busqueda
        button7 = QPushButton("Buscar", self)
        button7.setGeometry(930, 450, 100, 30)
        button7.clicked.connect(self.search)

        self.view = QV(self)
        self.view.setGeometry(10, 30, 800, 800)
        self.scene = QS(self)
        self.view.setScene(self.scene)
        self.view.show()

        self.view_menu = QtWidgets.QMenu(self)
        # paint_action.triggered.connect(self.close)

        # use `connect` method to bind signals to desired behavior
        self.view_menu = QMenu(self)
        self.show()


    def paintGreen(self):
        global opc, obj
        opc = 1
        obj = 1
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        painter.drawRect(1200, 15, 1000, 200)
        # print("pressed")

    def paintRed(self):
        global opc, obj
        opc = 1
        obj = 2
        # print("pressed")

    def paintWall(self):
        global opc, obj
        opc = 1
        obj = 3
        # print("pressed")

    # Delete
    def deleteGreen(self):
        global opc, obj
        opc = 2
        obj = 1
        # print("pressed")

    def deleteRed(self):
        global opc, obj
        opc = 2
        obj = 2
        # print("pressed")

    def deleteWall(self):
        global opc, obj
        opc = 2
        obj = 3
        # print("pressed")

    def search(self):
        print("start to search")


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    b = Main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
