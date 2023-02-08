import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
import clr
clr.AddReference("C:\\Program Files\\Siemens\\Automation\\Portal V17\\PublicAPI\\V17\\Siemens.Engineering")
clr.AddReference("C:\\Program Files\\Siemens\\Automation\\Portal V17\\PublicAPI\\V17\\Siemens.Engineering.Hmi")
from System.IO import DirectoryInfo
import Siemens.Engineering as tia


class TIAProject(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1200, 300, 400, 400)
        self.setWindowTitle("Armstrong-Dematic TIA Project Manager")
        self.setWindowIcon(QIcon("download.png"))


        # Create new project button
        self.createButton = QPushButton("Create Project", self)
        self.createButton.clicked.connect(self.create_project)
        self.createButton.move(100, 150)

        # Open existing project button
        self.openButton = QPushButton("Open Project", self)
        self.openButton.clicked.connect(self.open_project)
        self.openButton.move(100, 200)

        # Project name input
        self.projectNameInput = QLineEdit(self)
        self.projectNameInput.move(200, 50)

        # Project location input
        self.projectLocationInput = QLineEdit(self)
        self.projectLocationInput.move(200, 80)

        # Project name label
        self.projectNameLabel = QLabel("Project Name:", self)
        self.projectNameLabel.move(100, 50)

        # Project location label
        self.projectLocationLabel = QLabel("Project Location:", self)
        self.projectLocationLabel.move(100, 80)

        self.show()

    def create_project(self):
        project_path = DirectoryInfo('D:\\Projects\\TIA')
        project_name = 'Test_Project'
        # Connect to TIA Portal
        # tia_portal = Openness.create()
        mytia = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)

        # Create new project
        # project = tia_portal.create_project()
        myproject = mytia.Projects.Create(project_path, project_name)

        # Set project name and location
        myproject.name = self.projectNameInput.text()
        myproject.location = self.projectLocationInput.text()

        # Add devices, networks, and programs
        PLC_mlfb = 'OrderNumber:6ES7 515-2AM01-0AB0/V2.6'
        PLC = myproject.Devices.CreateWithItem(PLC_mlfb, 'PLC', 'PLC')

        HMI_mlfb = 'OrderNumber:6AV2 124-0QC02-0AX1/16.0.0.0'
        HMI = myproject.Devices.CreateWithItem(HMI_mlfb, 'HMI', 'HMI')

        # Save and close the project
        mytia.save()
        mytia.close()

    def open_project(self):
        # Connect to TIA Portal
        mytia = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)

        # Open existing project
        project = mytia.open_project(self.projectNameInput.text(), self.projectLocationInput.text())

        # Access project's devices, networks, and programs
        # Add your code here to access the project's devices, networks, and programs

        # Close the project
        mytia.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tia = TIAProject()
    sys.exit(app.exec_())
