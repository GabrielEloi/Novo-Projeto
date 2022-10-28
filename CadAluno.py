# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadAlunos.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadAlunos(object):
    def setupUi(self, CadAlunos):
        CadAlunos.setObjectName("CadAlunos")
        CadAlunos.resize(496, 381)
        self.centralwidget = QtWidgets.QWidget(CadAlunos)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 31))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";")
        self.label.setObjectName("label")
        self.txt_matricula = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_matricula.setEnabled(False)
        self.txt_matricula.setGeometry(QtCore.QRect(95, 27, 161, 19))
        self.txt_matricula.setObjectName("txt_matricula")
        self.txt_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome.setGeometry(QtCore.QRect(96, 64, 156, 19))
        self.txt_nome.setObjectName("txt_nome")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(31, 57, 61, 31))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.txt_idade = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_idade.setGeometry(QtCore.QRect(95, 97, 159, 19))
        self.txt_idade.setObjectName("txt_idade")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 61, 31))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(31, 122, 61, 31))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.btn_novo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_novo.setGeometry(QtCore.QRect(30, 170, 75, 23))
        self.btn_novo.setObjectName("btn_novo")
        self.btn_editar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_editar.setGeometry(QtCore.QRect(118, 169, 75, 23))
        self.btn_editar.setObjectName("btn_editar")
        self.btn_excluir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_excluir.setGeometry(QtCore.QRect(400, 170, 75, 23))
        self.btn_excluir.setObjectName("btn_excluir")
        self.tb_alunos = QtWidgets.QTableWidget(self.centralwidget)
        self.tb_alunos.setGeometry(QtCore.QRect(30, 200, 451, 131))
        self.tb_alunos.setObjectName("tb_alunos")
        self.tb_alunos.setColumnCount(4)
        self.tb_alunos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_alunos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_alunos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_alunos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_alunos.setHorizontalHeaderItem(3, item)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(35, 343, 101, 31))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.txt_buscar = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_buscar.setGeometry(QtCore.QRect(134, 349, 347, 19))
        self.txt_buscar.setText("")
        self.txt_buscar.setObjectName("txt_buscar")
        self.cb_curso = QtWidgets.QComboBox(self.centralwidget)
        self.cb_curso.setGeometry(QtCore.QRect(95, 126, 159, 22))
        self.cb_curso.setObjectName("cb_curso")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        self.cb_curso.addItem("")
        CadAlunos.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadAlunos)
        QtCore.QMetaObject.connectSlotsByName(CadAlunos)

    def retranslateUi(self, CadAlunos):
        _translate = QtCore.QCoreApplication.translate
        CadAlunos.setWindowTitle(_translate("CadAlunos", "Cadastro de Alunos"))
        self.label.setText(_translate("CadAlunos", "Matricula:"))
        self.label_2.setText(_translate("CadAlunos", "Nome"))
        self.label_3.setText(_translate("CadAlunos", "Idade:"))
        self.label_4.setText(_translate("CadAlunos", "Curso:"))
        self.btn_novo.setText(_translate("CadAlunos", "Novo"))
        self.btn_editar.setText(_translate("CadAlunos", "Editar"))
        self.btn_excluir.setText(_translate("CadAlunos", "Excluir"))
        item = self.tb_alunos.horizontalHeaderItem(0)
        item.setText(_translate("CadAlunos", "Matricula"))
        item = self.tb_alunos.horizontalHeaderItem(1)
        item.setText(_translate("CadAlunos", "Nome"))
        item = self.tb_alunos.horizontalHeaderItem(2)
        item.setText(_translate("CadAlunos", "Idade"))
        item = self.tb_alunos.horizontalHeaderItem(3)
        item.setText(_translate("CadAlunos", "Curso"))
        self.label_5.setText(_translate("CadAlunos", "Buscar (Nome):"))
        self.cb_curso.setItemText(0, _translate("CadAlunos", "Dev Fullstack"))
        self.cb_curso.setItemText(1, _translate("CadAlunos", "Design"))
        self.cb_curso.setItemText(2, _translate("CadAlunos", "Fotografia"))
        self.cb_curso.setItemText(3, _translate("CadAlunos", "Markeing"))
        self.cb_curso.setItemText(4, _translate("CadAlunos", "Metaverso"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadAlunos = QtWidgets.QMainWindow()
    ui = Ui_CadAlunos()
    ui.setupUi(CadAlunos)
    CadAlunos.show()
    sys.exit(app.exec_())