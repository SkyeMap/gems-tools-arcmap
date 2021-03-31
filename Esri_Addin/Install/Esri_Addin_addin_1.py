import arcpy
import pythonaddins
import os

relPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
toolbox = relPath + r"\GeMS_ToolsArc105.tbx"

class ButtonClassAtttributeByKeyValue(object):
    """Implementation for Esri_Addin_addin.button.AtttributeByKeyValue (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(toolbox, "AttributeByKeyValues")

class ButtonClassCompactBackup(object):
    """Implementation for Esri_Addin_addin.button.CompactBackup (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassCreateNewDatabase(object):
    """Implementation for Esri_Addin_addin.button.CreateNewDatabase (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassDMUDocx(object):
    """Implementation for Esri_Addin_addin.button.DMUDocx (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassDeplanarizeCAF(object):
    """Implementation for Esri_Addin_addin.button.DeplanarizeCAF (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassDocxDMU(object):
    """Implementation for Esri_Addin_addin.button.DocxToDMU (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassFixStrings(object):
    """Implementation for Esri_Addin_addin.button.FixStrings (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassGeologicNamesCheck(object):
    """Implementation for Esri_Addin_addin.button.GeologicNamesCheck (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassInclinationNumbers(object):
    """Implementation for Esri_Addin_addin.button.InclinationNumbers (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassMakePolygons(object):
    """Implementation for Esri_Addin_addin.button.MakePolygons (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassMakeTopology(object):
    """Implementation for Esri_Addin_addin.button.MakeTopology (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassMapOutline(object):
    """Implementation for Esri_Addin_addin.button.MapOutline (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassProjectMapData(object):
    """Implementation for Esri_Addin_addin.button.ProjectMapData (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassProjectPoints(object):
    """Implementation for Esri_Addin_addin.button.ProjectPoints (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassPurgeMetadata(object):
    """Implementation for Esri_Addin_addin.button.PurgeMetadata (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassRelationshipClasses(object):
    """Implementation for Esri_Addin_addin.button.RelationshipClasses (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassSetIDvalues(object):
    """Implementation for Esri_Addin_addin.button.SetIDvalues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassSetPlotAtScaleValues(object):
    """Implementation for Esri_Addin_addin.button.SetPlotAtScaleValues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassSetSymbolValues(object):
    """Implementation for Esri_Addin_addin.button.SetSymbolValues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassSymbolToRGB(object):
    """Implementation for Esri_Addin_addin.button.SymbolToRGB (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassTopologyCheck(object):
    """Implementation for Esri_Addin_addin.button.TopologyCheck (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassTranslateToShapefiles(object):
    """Implementation for Esri_Addin_addin.button.TranslateToShapefiles (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassValidateDatabase(object):
    """Implementation for Esri_Addin_addin.button.ValidateDatabase (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ToolClassFGDC1(object):
    """Implementation for Esri_Addin_addin.tool.FGDC1 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass

class ToolClassFGDC2(object):
    """Implementation for Esri_Addin_addin.tool.FGDC2 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass

class ToolClassFGDC3(object):
    """Implementation for Esri_Addin_addin.tool.FGDC3 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        pass
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass