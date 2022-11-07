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

#get elements in a category 
from Autodesk.Revit.DB import *
doc = __revit__.ActiveUIDocument.Document
elements = FilteredElementCollector(doc).OfClass(SharedParameterElement)


#Blow that parameter out of existence 
def nuke_away(doc, guids_list):
    for guid in guids_list: 
        Shared_param = SharedParameterElement.Lookup(doc, guid)
        t = Transaction(doc, "Remove sharedParameter {}".format(guid))
        t.Start()
        doc.Delete(Shared_param.Id)
        t.Commit()

#get project Parameters
import Autodesk
from Autodesk.Revit.DB import *

def get_project_params():
    project_info_collector = FilteredElementCollector(doc) \
                            .OfCategory(BuiltInCategory.OST_ProjectInformation) \
                            .ToElements()
    for i in project_info_collector:
        project_number_param = i.LookupParameter('Project Number')
        if project_number_param:
            project_number = project_number_param.AsString()
            print(project_number)
        else: 
            pass 
