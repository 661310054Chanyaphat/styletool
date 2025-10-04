try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui 

IMAGE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/styletool'

class StyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('Style Tool')
		self.resize(300,100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet(
			'''
				QDialog{
					background-color: #704EB5;

				}
			'''

			)
		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f'{IMAGE_DIR}/heart.png')
		scalePixmap = self.imagePixmap.scaled(
			QtCore.QSize(64,64),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation

			)

		self.imageLabel.setPixmap(scalePixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('👽Name:')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			''' 
				QLineEdit{
					background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #8A368A, stop:1 #462663);
					color: white;
					border-radius: 8px;
					font-family: Arial;
					font-weight: bold;

				}
			'''	

			)


		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.selectButton = QtWidgets.QPushButton('Select🤪')
		self.selectButton.setStyleSheet(
			'''
				 QPushButton {
					background-color: #42269E;
					border-radius: 10px;
					font-size: 16px;
					font-family:  Papyrus;
					font-weigh: bold;
					padding: 4px;

				 }
				 QPushButton:hover{
				 	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #21306E, stop:1 #3C79BA);

				 }
				 QPushButton:pressed{
				 	background-color: #5AF29E;

				 }
				 
		    '''

		    )

		self.cancelButton = QtWidgets.QPushButton('Cancel💢')
		self.cancelButton.setStyleSheet(
			'''
				 QPushButton {
					background-color: #42269E;
					border-radius: 10px;
					font-size: 16px;
					font-family:  Papyrus;
					font-weigh: bold;
					padding: 4px;

				 }
				 QPushButton:hover{
				 	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #21306E, stop:1 #3C79BA);

				 }
				 QPushButton:pressed{
				 	background-color: #5AF29E;

				 }
				 
		    '''
		    )

		self.buttonLayout.addWidget(self.selectButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()



def run():
	global ui
	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = StyleToolDialog(parent=ptr)
	ui.show()
	