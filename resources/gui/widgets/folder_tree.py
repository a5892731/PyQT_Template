from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QFileSystemModel


'''warning!

This widget need's some time to start!

'''


class TreeView(QMainWindow):
    def __init__(self, layout= None, grid_position = (0,0), rowspan = 1, columnspan = 1, enable = True):
        super().__init__()
        self.layout = layout


        self.grid_position = grid_position
        self.columnspan = columnspan
        self.rowspan = rowspan


        self.initUI()

    def initUI(self):


        # Create the tree view widget
        self.tree_view = QTreeView(self)
        self.setCentralWidget(self.tree_view)

        # Create and set the file system model for the tree view
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(QDir.currentPath()))

        '''show widget on layout'''
        #self.layout.addWidget(self.button)
        self.layout.addWidget(self.tree_view, self.grid_position[0], self.grid_position[1], self.rowspan, self.columnspan)


