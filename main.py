import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets


#Settings for the Window and the content
class Settings():
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

    #draw all the background
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
        self.initUI()

    def initUI(self):
        # adding actions to file menu
        #self.setWindowIcon(QIcon('upv.png'))
        self.setWindowTitle("Rutas")
        self.setGeometry(100, 100, 1250, 700)

        paint_action = QtWidgets.QAction('Paint', self)
        delete_action = QtWidgets.QAction('Delete', self)
        #Menu
        self.statusBar()
        bar = self.menuBar()
        # File menu
        file_menu = bar.addMenu('File')
        file_menu.addAction(paint_action)
        file_menu.addAction(delete_action)

        self.view = QV(self)
        self.view.setGeometry(10,30,800,800)
        self.scene = QS(self)
        self.view.setScene(self.scene)
        self.view.show()

        #self.view_menu = QtWidgets.QMenu(self)
        # close_action.triggered.connect(self.close)

        # use `connect` method to bind signals to desired behavior
        #self.view_menu = QMenu(self)
        self.show()

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    b = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()