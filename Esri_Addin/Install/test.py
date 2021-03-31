import os

relPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
toolbox = relPath + r'\GeMS_ToolsArc105.tbx'

toolbox_hard = r"D:\GitHub\gems-tools-arcmap-forked\GeMS_ToolsArc105.tbx"

print(toolbox)
print(toolbox_hard)
print(toolbox == toolbox_hard)
