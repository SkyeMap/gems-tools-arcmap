import arcpy
import pythonaddins
import os

#relPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#toolbox = relPath + r"\GeMS_ToolsArc105.tbx"
toolbox = r"W:\DATABASE_MAPS\24K\SkyeTraining\GitHub\gems-tools-arcmap\GeMS_ToolsArc105.tbx"

class ButtonClassAtttributeByKeyValue(object):
    """Implementation for Esri_Addin_addin.buttonAtttributeByKeyValue (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "AttributeByKeyValues")

class ButtonClassCompactBackup(object):
    """Implementation for Esri_Addin_addin.buttonCompactBackup (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "CompactAndBackup")

class ButtonClassCreateNewDatabase(object):
    """Implementation for Esri_Addin_addin.buttonCreateNewDatabase (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "CreateDatabase")

class ButtonClassDMUDocx(object):
    """Implementation for Esri_Addin_addin.buttonDMUDocx (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "DMUtoDocx")

class ButtonClassDeplanarizeCAF(object):
    """Implementation for Esri_Addin_addin.buttonDeplanarizeCAF (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "Deplanarize")

class ButtonClassDocxDMU(object):
    """Implementation for Esri_Addin_addin.buttonDocxToDMU (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "DocxToDMU")

class ButtonClassFGDC1(object):
    """Implementation for Esri_Addin_addin.buttonFGDC1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "Metadata-FGDC1")

class ButtonClassFGDC2(object):
    """Implementation for Esri_Addin_addin.buttonFGDC2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "MetadataFGDC-2")

class ButtonClassFGDC3(object):
    """Implementation for Esri_Addin_addin.buttonFGDC3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "FGDC-3")

class ButtonClassFixStrings(object):
    """Implementation for Esri_Addin_addin.buttonFixStrings (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "FixStrings")

class ButtonClassGeologicNamesCheck(object):
    """Implementation for Esri_Addin_addin.buttonGeologicNamesCheck (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "GeologicNamesCheck")

class ButtonClassInclinationNumbers(object):
    """Implementation for Esri_Addin_addin.buttonInclinationNumbers (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "InclinationNumber")

class ButtonClassMakePolygons(object):
    """Implementation for Esri_Addin_addin.buttonMakePolygons (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "MakePolys")

class ButtonClassMakeTopology(object):
    """Implementation for Esri_Addin_addin.buttonMakeTopology (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "MakeTopology")

class ButtonClassMapOutline(object):
    """Implementation for Esri_Addin_addin.buttonMapOutline (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "MapOutline")

class ButtonClassProjectMapData(object):
    """Implementation for Esri_Addin_addin.buttonProjectMapData (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "ProjectCrossSectionData")

class ButtonClassProjectPoints(object):
    """Implementation for Esri_Addin_addin.buttonProjectPoints (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "ProjectPointsToCrossSection")

class ButtonClassPurgeMetadata(object):
    """Implementation for Esri_Addin_addin.buttonPurgeMetadata (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "PurgeMetadata")

class ButtonClassRelationshipClasses(object):
    """Implementation for Esri_Addin_addin.buttonRelationshipClasses (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "RelationshipClasses")

class ButtonClassSetIDvalues(object):
    """Implementation for Esri_Addin_addin.buttonSetIDvalues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "SetIDvalues2")

class ButtonClassSetPlotAtScaleValues(object):
    """Implementation for Esri_Addin_addin.buttonSetPlotAtScaleValues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "SetPlotAtScales")

class ButtonClassSetSymbolValues(object):
    """Implementation for Esri_Addin_addin.buttonSetSymbolValues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "SetSymbols")

class ButtonClassSymbolToRGB(object):
    """Implementation for Esri_Addin_addin.buttonSymbolToRGB (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "SetSymbols")

class ButtonClassTopologyCheck(object):
    """Implementation for Esri_Addin_addin.buttonTopologyCheck (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "TopologyCheck")

class ButtonClassTranslateToShapefiles(object):
    """Implementation for Esri_Addin_addin.buttonTranslateToShapefiles (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "TranslateToShape")

class ButtonClassValidateDatabase(object):
    """Implementation for Esri_Addin_addin.buttonValidateDatabase (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "ValidateDatabase2")
