# Is the user logged in - returns True or False 
from Autodesk.Revit import ApplicationServices
uiApp = ApplicationServices.Application
username = uiApp.IsLoggedIn.ToString()
print(str(username))

#get revit user name 
from Autodesk.Revit import DB
doc = __revit__.ActiveUIDocument.Document
username = doc.Application.Username
print(username)

#get current date 
from datetime import datetime
current_date = str(datetime.now().date())
print(current_date)
