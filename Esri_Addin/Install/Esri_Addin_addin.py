import arcpy
import pythonaddins
import os

#relPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#toolbox = relPath + r"\GeMS_ToolsArc105.tbx"
toolbox = r"D:\GitHub\gems-tools-arcmap-forked\GeMS_ToolsArc105.tbx"

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
        pass

class ButtonClassCreateNewDatabase(object):
    """Implementation for Esri_Addin_addin.buttonCreateNewDatabase (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassDMUDocx(object):
    """Implementation for Esri_Addin_addin.buttonDMUDocx (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassDeplanarizeCAF(object):
    """Implementation for Esri_Addin_addin.buttonDeplanarizeCAF (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassDocxDMU(object):
    """Implementation for Esri_Addin_addin.buttonDocxToDMU (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassFixStrings(object):
    """Implementation for Esri_Addin_addin.buttonFixStrings (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassGeologicNamesCheck(object):
    """Implementation for Esri_Addin_addin.buttonGeologicNamesCheck (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassInclinationNumbers(object):
    """Implementation for Esri_Addin_addin.buttonInclinationNumbers (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassMakePolygons(object):
    """Implementation for Esri_Addin_addin.buttonMakePolygons (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassMakeTopology(object):
    """Implementation for Esri_Addin_addin.buttonMakeTopology (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassMapOutline(object):
    """Implementation for Esri_Addin_addin.buttonMapOutline (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassProjectMapData(object):
    """Implementation for Esri_Addin_addin.buttonProjectMapData (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassProjectPoints(object):
    """Implementation for Esri_Addin_addin.buttonProjectPoints (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassPurgeMetadata(object):
    """Implementation for Esri_Addin_addin.buttonPurgeMetadata (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassRelationshipClasses(object):
    """Implementation for Esri_Addin_addin.buttonRelationshipClasses (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassSetIDvalues(object):
    """Implementation for Esri_Addin_addin.buttonSetIDvalues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassSetPlotAtScaleValues(object):
    """Implementation for Esri_Addin_addin.buttonSetPlotAtScaleValues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassSetSymbolValues(object):
    """Implementation for Esri_Addin_addin.buttonSetSymbolValues (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassSymbolToRGB(object):
    """Implementation for Esri_Addin_addin.buttonSymbolToRGB (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassTopologyCheck(object):
    """Implementation for Esri_Addin_addin.buttonTopologyCheck (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassTranslateToShapefiles(object):
    """Implementation for Esri_Addin_addin.buttonTranslateToShapefiles (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ButtonClassValidateDatabase(object):
    """Implementation for Esri_Addin_addin.buttonValidateDatabase (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class ToolClassFGDC1(object):
    """Implementation for Esri_Addin_addin.toolFGDC1 (Tool)"""
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
    """Implementation for Esri_Addin_addin.toolFGDC2 (Tool)"""
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
    """Implementation for Esri_Addin_addin.toolFGDC3 (Tool)"""
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