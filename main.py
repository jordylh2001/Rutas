import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

# Settings for the Window and the content
from PyQt5.QtWidgets import QMenu, QAction, QPushButton, QLabel


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

    def __init__(self):
        super().__init__()
        self.view = None
        self.initUI()

    def mousePressEvent(self, QMouseEvent):
        print("Press", QMouseEvent.pos())

    def initUI(self):
        # adding actions to file menu
        # self.setWindowIcon(QIcon('upv.png'))
        self.setWindowTitle("Rutas")
        self.setGeometry(100, 100, 1250, 850)

        # pintar
        label1 = QLabel(self)
        label1.setText("Paint")
        label1.setGeometry(880,100,100,30)
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
        label2.setGeometry(1030,100,100,30)
        button4 = QPushButton("Green", self)
        button4.setGeometry(1000, 150, 100, 30)
        button4.clicked.connect(self.deleteGreen)
        button5 = QPushButton("Red", self)
        button5.setGeometry(1000, 250, 100, 30)
        button5.clicked.connect(self.deleteRed)
        button6 = QPushButton("Wall", self)
        button6.setGeometry(1000, 350, 100, 30)
        button6.clicked.connect(self.deleteWall)
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
        print("pressed")

    def paintRed(self):
        print("pressed")

    def paintWall(self):
        print("pressed")

    # Delete
    def deleteGreen(self):
        print("pressed")

    def deleteRed(self):
        print("pressed")

    def deleteWall(self):
        print("pressed")


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    b = Main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
