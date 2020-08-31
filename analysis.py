# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\hproj\analysis.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import numpy as np


class Ui_AnalysisForm(object):
    def setupUi(self, AnalysisForm):
        AnalysisForm.setObjectName("AnalysisForm")
        AnalysisForm.resize(675, 544)
        AnalysisForm.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label = QtWidgets.QLabel(AnalysisForm)
        self.label.setGeometry(QtCore.QRect(220, 40, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setObjectName("label")
        self.dsbtn = QtWidgets.QPushButton(AnalysisForm)
        self.dsbtn.setGeometry(QtCore.QRect(40, 130, 75, 23))
        self.dsbtn.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.dsbtn.setObjectName("dsbtn")
        self.agebtn = QtWidgets.QPushButton(AnalysisForm)
        self.agebtn.setGeometry(QtCore.QRect(150, 130, 75, 23))
        self.agebtn.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.agebtn.setObjectName("agebtn")
        self.hrbtn = QtWidgets.QPushButton(AnalysisForm)
        self.hrbtn.setGeometry(QtCore.QRect(270, 130, 75, 23))
        self.hrbtn.setStyleSheet("background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.hrbtn.setObjectName("hrbtn")
        self.bpbtn = QtWidgets.QPushButton(AnalysisForm)
        self.bpbtn.setGeometry(QtCore.QRect(370, 130, 75, 23))
        self.bpbtn.setStyleSheet("background-color: rgb(85, 0, 127);\n"
"background-color: rgb(0, 255, 255);")
        self.bpbtn.setObjectName("bpbtn")
        self.dgbtn = QtWidgets.QPushButton(AnalysisForm)
        self.dgbtn.setGeometry(QtCore.QRect(490, 130, 75, 23))
        self.dgbtn.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.dgbtn.setObjectName("dgbtn")
        self.clbtn = QtWidgets.QPushButton(AnalysisForm)
        self.clbtn.setGeometry(QtCore.QRect(590, 130, 75, 23))
        self.clbtn.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.clbtn.setObjectName("clbtn")
        self.result = QtWidgets.QTextEdit(AnalysisForm)
        self.result.setGeometry(QtCore.QRect(53, 180, 591, 281))
        self.result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.result.setObjectName("result")
        self.dsbtn.clicked.connect(self.dsfun) 
        self.bpbtn.clicked.connect(self.bpfun)
        self.agebtn.clicked.connect(self.agefun)
        self.clbtn.clicked.connect(self.clfun)
        self.dgbtn.clicked.connect(self.dgfun)
        self.hrbtn.clicked.connect(self.hrfun)
        
        self.retranslateUi(AnalysisForm)
        QtCore.QMetaObject.connectSlotsByName(AnalysisForm)

    def retranslateUi(self, AnalysisForm):
        _translate = QtCore.QCoreApplication.translate
        AnalysisForm.setWindowTitle(_translate("AnalysisForm", "Form"))
        self.label.setText(_translate("AnalysisForm", "DATA ANALYSIS"))
        self.dsbtn.setText(_translate("AnalysisForm", "DESCSTAT"))
        self.agebtn.setText(_translate("AnalysisForm", "AGE"))
        self.hrbtn.setText(_translate("AnalysisForm", "Heart rate"))
        self.bpbtn.setText(_translate("AnalysisForm", "Blood Press"))
        self.dgbtn.setText(_translate("AnalysisForm", "Diagnosis"))
        self.clbtn.setText(_translate("AnalysisForm", "clear"))

    def dsfun(self):
         col_names = ['age','sex','chest_pain','blood_pressure','serum_cholestoral','fasting_blood_sugar', 'electrocardiographic',
             'max_heart_rate','induced_angina','ST_depression','slope','no_of_vessels','thal','diagnosis']

# read the file
         df = pd.read_csv("processed.cleveland.data", names=col_names, header=None, na_values="?")
         # extract numeric columns and find categorical ones
         numeric_columns = ['serum_cholestoral', 'max_heart_rate', 'age', 'blood_pressure', 'ST_depression']
         categorical_columns = [c for c in df.columns if c not in numeric_columns]
         disc=df[numeric_columns].describe()
         data1=str(disc)
         self.result.setText(data1)
        
    def bpfun(self):
        col_names = ['age','sex','chest_pain','blood_pressure','serum_cholestoral','fasting_blood_sugar', 'electrocardiographic',
             'max_heart_rate','induced_angina','ST_depression','slope','no_of_vessels','thal','diagnosis']

# read the file
        df = pd.read_csv("processed.cleveland.data", names=col_names, header=None, na_values="?")
         # extract numeric columns and find categorical ones
        numeric_columns = ['serum_cholestoral', 'max_heart_rate', 'age', 'blood_pressure', 'ST_depression']
        
        data3= str((df.diagnosis).corr(df['blood_pressure']))
        self.result.setText(data3)
    def agefun(self):
       col_names = ['age','sex','chest_pain','blood_pressure','serum_cholestoral','fasting_blood_sugar', 'electrocardiographic',
             'max_heart_rate','induced_angina','ST_depression','slope','no_of_vessels','thal','diagnosis']

# read the file
       df = pd.read_csv("processed.cleveland.data", names=col_names, header=None, na_values="?")
         # extract numeric columns and find categorical ones
       numeric_columns = ['serum_cholestoral', 'max_heart_rate', 'age', 'blood_pressure', 'ST_depression']
        
       data3= str((df.diagnosis).corr(df['age']))
       self.result.setText(data3)
    def clfun(self):
        self.result.clear()
    def dgfun(self):
        col_names = ['age','sex','chest_pain','blood_pressure','serum_cholestoral','fasting_blood_sugar', 'electrocardiographic',
         'max_heart_rate','induced_angina','ST_depression','slope','no_of_vessels','thal','diagnosis']

# read the file
        df = pd.read_csv("processed.cleveland.data", names=col_names, header=None, na_values="?")
         # extract numeric columns and find categorical ones
        numeric_columns = ['serum_cholestoral', 'max_heart_rate', 'age', 'blood_pressure', 'ST_depression']
       
        df.diagnosis = (df.diagnosis != 0).astype(int)
        data2=str(df.diagnosis.value_counts())
        self.result.setText(data2)
        
    def hrfun(self):
         col_names = ['age','sex','chest_pain','blood_pressure','serum_cholestoral','fasting_blood_sugar', 'electrocardiographic',
             'max_heart_rate','induced_angina','ST_depression','slope','no_of_vessels','thal','diagnosis']

# read the file
         df = pd.read_csv("processed.cleveland.data", names=col_names, header=None, na_values="?")
         # extract numeric columns and find categorical ones
         numeric_columns = ['serum_cholestoral', 'max_heart_rate', 'age', 'blood_pressure', 'ST_depression']
        
         data3= str((df.diagnosis).corr(df['max_heart_rate']))
         self.result.setText(data3)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnalysisForm = QtWidgets.QWidget()
    ui = Ui_AnalysisForm()
    ui.setupUi(AnalysisForm)
    AnalysisForm.show()
    sys.exit(app.exec_())

