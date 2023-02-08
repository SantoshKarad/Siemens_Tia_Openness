import clr
clr.AddReference('C:\\Program Files\\Siemens\\Automation\\Portal V17\\PublicAPI\V17\\Siemens.Engineering.dll')
from System.IO import DirectoryInfo
import Siemens.Engineering as tia


project_path = DirectoryInfo('D:\\Projects\\TIA')
project_name = 'Test_Project'

#Starting TIA
print('Starting TIA with UI')
mytia = tia.TiaPortal(tia.TiaPortalMode.WithUserInterface)

#Creating new project
print('Creating project')
myproject = mytia.Projects.Create(project_path, project_name)

#Addding HW to the projects
print('Creating PLC')
PLC_mlfb = 'OrderNumber:6ES7 515-2AM01-0AB0/V2.6'
PLC = myproject.Devices.CreateWithItem(PLC_mlfb, 'PLC', 'PLC')

print('Creating HMI')
HMI_mlfb = 'OrderNumber:6AV2 124-0QC02-0AX1/16.0.0.0'
HMI = myproject.Devices.CreateWithItem(HMI_mlfb, 'HMI', 'HMI')

print("Press any key to quit")
input()
quit()
