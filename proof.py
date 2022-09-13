from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import sys

from bs4 import BeautifulSoup
import requests

#Web Scrape with requests and BeautifulSoup
source = requests.get('https://www.rottentomatoes.com/m/pinocchio_2022').text

soup = BeautifulSoup(source, 'lxml')

print(soup.prettify)


#Showing PyQt5 UI
class MainWindow(QDialog):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi("tt.ui",self)
		self.tableWidget.setColumnWidth(0,200)
		self.tableWidget.setColumnWidth(1,150)
		self.tableWidget.setColumnWidth(2,300)
		self.loaddata()

	def loaddata(self):
		movies=[{"title":"Jaws", "year":"1975", "genre":"horror", "rating":"R"}, {"title":"The Big Lebowski", "year":"1998", "genre":"comedy", "rating":"PG"}]
		row = 0
		self.tableWidget.setRowCount(len(movies))
		for movie in movies:
			self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(movie["title"]))
			self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(movie["year"]))
			self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(movie["genre"]))
			self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(movie["rating"]))
			row = row + 1

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(900)
widget.setFixedWidth(1300)
widget.show()
try:
	sys.exit(app.exec_())
except:
	print("Exiting")