import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

# Settings for the Window and the content
from PyQt5.QtWidgets import QMenu, QAction


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

    def initUI(self):
        # adding actions to file menu
        # self.setWindowIcon(QIcon('upv.png'))
        self.setWindowTitle("Rutas")
        self.setGeometry(100, 100, 1250, 700)

        # Menu
        self.statusBar()
        bar = self.menuBar()
        fileMenu = bar.addMenu('Actions')

        #Paint
        paint_menu = QMenu('Paint', self)
        paint_action1 = QAction('Green', self)
        paint_action2 = QAction('Red', self)
        paint_action3 = QAction('Wall', self)
        paint_menu.addAction(paint_action1)
        paint_menu.addAction(paint_action2)
        paint_menu.addAction(paint_action3)

        #Delete
        delete_menu = QMenu('Delete', self)
        delete_action1 = QAction('Green', self)
        delete_action2 = QAction('Red', self)
        delete_action3 = QAction('Wall', self)
        delete_menu.addAction(delete_action1)
        delete_menu.addAction(delete_action2)
        delete_menu.addAction(delete_action3)

        fileMenu.addMenu(paint_menu)
        fileMenu.addMenu(delete_menu)

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


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    b = Main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
