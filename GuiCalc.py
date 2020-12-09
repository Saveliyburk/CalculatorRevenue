import func as f
from PyQt5 import QtWidgets
from gdcalc import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.zeroseven_data.valueChanged.connect(self.all_data)
        self.ui.sevenzero_data.valueChanged.connect(self.all_data)
        self.ui.holy_data.valueChanged.connect(self.all_data)
        self.ui.twochats_data.valueChanged.connect(self.all_data)
        self.ui.plaf_data.valueChanged.connect(self.all_data)
        self.ui.quality_data.valueChanged.connect(self.all_data)
        self.ui.samost_data.valueChanged.connect(self.all_data)
        self.ui.effect_data.valueChanged.connect(self.all_data)


    def all_data(self):
        zero = self.ui.zeroseven_data.value()
        seven = self.ui.sevenzero_data.value()
        holy = self.ui.holy_data.value()
        double = self.ui.twochats_data.value()
        plaf = self.ui.plaf_data.value()
        qual = f.qual(self.ui.quality_data.value())
        samost = f.selfsup(self.ui.samost_data.value())
        effect = f.effect(self.ui.effect_data.value())
        time = f.alltime(zero, seven, holy, double)

        result = f.result(plaf, time, qual, samost, effect)
        self.ui.coin_data.display(result)

app = QtWidgets.QApplication([])
applic = mywindow()
applic.show()
sys.exit(app.exec())
