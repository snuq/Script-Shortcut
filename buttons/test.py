#len(bpy.context.scene.objects) > 0
#The first line of the script can be a commented out conditional statement that can be used to enable or disable the button that activates this script
#The example first line above will ensure the button cannot be clicked if no objects are in the scene.

#The script may have a list of commands that will be executed when the button is pressed:
print('This is a basic command')

#Data and functions can be imported from blender:
import bpy
print('The current scene is: '+bpy.context.scene.name)

#Functions, classes, and any other features of python can be defined and used:
def saysomething():
    print('This is run from a function')
saysomething()

#If a 'register' function is included in the script, this will be run automatically when the button is pressed:
def register():
    print('This is in the register function')
