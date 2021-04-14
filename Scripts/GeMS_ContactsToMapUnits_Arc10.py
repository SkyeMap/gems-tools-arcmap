import arcpy
import os
import sys
import re

def get_trailing_number(s):
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else 0

def findLyr(lname):
    mxd = arcpy.mapping.MapDocument('CURRENT')
    for df in arcpy.mapping.ListDataFrames(mxd):
        lList = arcpy.mapping.ListLayers(mxd, '*', df)
        for lyr in lList:
            if lyr.name == lname:
                pos = lList.index(lyr)
                #wks = lyr.workspacePath
                if pos == 0:
                    refLyr = lList[pos + 1]
                    insertPos = "BEFORE"
                else:
                    refLyr = lList[pos - 1]
                    insertPos = "AFTER"
                    
                return [lyr, df, refLyr, insertPos]

def pm(msg, severity=0): 
	# prints msg to screen and adds msg to the geoprocessor (in case this is run as a tool) 
	# pm(msg) 
	try: 
	  for string in msg.split('\n'): 
		# Add appropriate geoprocessing message 
		if severity == 0: 
			arcpy.AddMessage(string) 
		elif severity == 1: 
			arcpy.AddWarning(string) 
		elif severity == 2: 
			arcpy.AddError(string) 
	except: 
		pass
            
#********************************************************************************************
#Get the parameters
lineLayer = arcpy.GetParameterAsText(0)
polyLayer = arcpy.GetParameterAsText(1)
labelPoints = arcpy.GetParameterAsText(2)
saveMUP = arcpy.GetParameterAsText(3)

#collect the findLyr properties
lyrProps = findLyr(polyLayer)
lyr = lyrProps[0]               #the layer object
df = lyrProps[1]                #the data frame within which the layer resides
refLyr = lyrProps[2]            #a layer above or below which the layer resides
insertPos = lyrProps[3]         #index above or below the reference layer
newPolys = lyr.dataSource       #the path to the dataSource of the polygon layer

#save a temporary layer file for the polygons to save rendering and other settings
#including joins to other tables
#.lyr is saved to the folder of the geodatabase
lyrPath = os.path.join(os.path.dirname(lyr.workspacePath), lyr.name + '.lyr')
if arcpy.Exists(lyrPath):
    os.remove(lyrPath)
		
pm("  saving " + polyLayer + ' to ' + lyrPath)
arcpy.SaveToLayerFile_management(lyr, lyrPath, "RELATIVE")

#set the workspace variable to the workspace of the feature class
#and get the name of the feature dataset
dsPath = os.path.dirname(newPolys)
arcpy.env.workspace = dsPath

try:
	#remove join if one is there
	arcpy.RemoveJoin_management(lyr)
except:
	pass

# make a labelPoints feature class if one was not provided
if labelPoints in ['#', '', None]:
    #create the labelPoints name
    labelPoints = polyLayer + '_tempLabels'

    #check for an old copy of labelpoints
    if arcpy.Exists(labelPoints):
        arcpy.Delete_management(labelPoints)
        
    #create points from the attributed polygons
    arcpy.FeatureToPoint_management(polyLayer, labelPoints, 'INSIDE')

#and now remove the layer from the map
arcpy.mapping.RemoveLayer(df, lyr)

#save a copy of the polygons fc or delete
if saveMUP == 'true':
    # get new name
    pfcs = arcpy.ListFeatureClasses(polyLayer + "*", "Polygon")
    maxN = 0
    for pfc in pfcs:
        try:
            n = int(get_trailing_number(pfc))
            if n > maxN:
                maxN = n
        except:
            pass
    oldPolys = lyr.dataSource + str(maxN + 1)
    pm("  saving " + polyLayer + ' to ' + oldPolys)
   
    try:
        oldPolysPath = os.path.join(dsPath, oldPolys)
        arcpy.Copy_management(lyr.dataSource, oldPolysPath, "FeatureClass")
    except:
        pm("  arcpy.Copy_management(mup,oldPolys) failed. Maybe you need to close ArcMap?")
        sys.exit()


pm("  deleting " + lyr.dataSource)
arcpy.Delete_management(lyr.dataSource)
#arcpy.RefreshCatalog(arcpy.env.workspace)
#raise ValueError()
# and rebuild the polygons
pm("  recreating " + newPolys + " from new linework")

# select all unconcealed lines
where = '"IsConcealed"  NOT IN (\'Y\',\'y\')'
#wherec = '"IsConcealed" = \'N\''
arcpy.SelectLayerByAttribute_management(lineLayer, "NEW_SELECTION", where)
arcpy.FeatureToPolygon_management(lineLayer, newPolys, '#', '#', labelPoints)
arcpy.RefreshCatalog(arcpy.env.workspace)
arcpy.SelectLayerByAttribute_management(lineLayer, "CLEAR_SELECTION")
#arcpy.Delete_management(labelPoints)

# add the layer file 
pm("  adding " + lyrPath + " to the map")
addLyr = arcpy.mapping.Layer(lyrPath)
#arcpy.mapping.AddLayer(df, addLyr)
arcpy.mapping.InsertLayer(df, refLyr, addLyr, insertPos)
#arcpy.Delete_management(lyrPath)
