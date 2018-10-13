# Script Shortcut Addon For Blender

## Features:
* Easily load python scripts as a button in Blender's interface
* Set up individual custom panels for each type of blender area
* Add as many buttons as you like
* Add labels and spaces between buttons
* Group buttons into presets and select them from a menu
* Make buttons conditional on a true-false statement included in the button script file
* Save and load panel presets to an external file
* Use keyboard shortcuts to quickly activate the loaded buttons



Development for this script is supported by my multimedia and video production business, [Creative Life Productions](http://www.creativelifeproductions.com)  
But, time spent working on this addon is time I cannot spend earning a living, so if you find this addon useful, consider donating:  

PayPal | Bitcoin
------ | -------
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=XHRXZBQ3LGLH6) | ![Bitcoin Donate QR Code](http://www.snuq.com/snu-bitcoin-address.png) <br> 1JnX9ZFsvUaMp13YiQgr9V36EbTE2SA8tz  

Or support me by hiring Creative Life Productions if you have a need for the services provided.



# Installation:
* Download 'ScriptShortcut.py', or download the master zip and extract this file.  
* Open Blender, and from the 'File' menu, select 'User Preferences'.
* In this new window, click on the 'Add-ons' tab at the top.
* Click the 'Install Add-on from File...' button at the bottom of this window.
* Browse to and select the 'ScriptShortcut.py' file, click the 'Install Add-on from File' button.
* You should now see the addon displayed in the preferences window, click the checkbox next to the name to enable it.
* Now, below the addon information, disable or enable panels in specific Blender areas by clicking the checkbox next to the name of the area.
* Click the 'Save User Settings' button to ensure this addon is loaded next time Blender starts.



# Editing The Panel:
You will need at least one python script, these can be downloaded from the 'buttons' directory above, or found anywhere python scripts are found.  
Any python script that can be run in Blender should work as a button, but be careful with scripts that are designed as an addon, running them multiple times may cause menus or button panels to appear multiple times.  

The 'Script Shortcuts' panel will start out as empty, with only an 'Edit' checkbox showing, clicking this will switch the panel to edit mode.  
When you are finished editing the panel, click the 'Edit' checkbox again to be able to use the panel.  


### Add A New Button:
Click the '+ Button' button to add a new button.  
Use the file browser to find a python '.py' script to have the button run.
* Double-click the file, or single click it and click the 'Select A Script...' button in the top-right.

You will now be prompted to rename the button.
* You may keep the default name, or type in a new one.
* Click the 'Select Script' button to pick a different python script.
* Click the 'OK' button to confirm the new button.  

You should now see the new button in the list.
* Click the button name to rename it or change the script.
* Click the up or down arrows to move the button up or down in the list.
* Click the 'X' button to delete the button.
* Click the checkbox to the right of the button to enable conditional mode, which will help prevent the button from being clicked when it shouldn't be.  


### Add A New Label:
Use a label to arrange your buttons into categories and make a specific one easier to find.  
Click the '+ Label' button to add a new label.
Rename the label in the dialog that opens, and click 'OK' to finish.  

You should now see the new label in the list.
* Like buttons, labels can be renamed by clicking them.
* Use the up and down arrows to move the label.
* Delete the label with the 'X' button.


### Add A New Spacer:
Use a spacer to separate the list of buttons and labels, making individual buttons easier to find.  
Click the '+ Spacer' button to add a new spacer.  

You should now see the black space in the list.  
* Use the u and down arrows to move the spacer.
* Delete the spacer by clicking the 'X' button next to it.


### Add A New Panel Preset:
Panel presets allow you to switch between groups of buttons with a drop-down menu.  
Click the 'Panel Presets' menu at the top of the panel.  
Click 'Add Current As Preset' to create a new preset using the current panel buttons.  
A popup will appear, prompting you to name the preset.
* Give the preset a unique name.
* Click 'OK' to create the preset.

The new preset name should now show in the list.
* Click the preset name to rename it.
* Click the 'X' button next to the preset to delete it.

You are now free to clear the current panel and create a new setup.  
Be sure to save each new panel setup as a preset, the current panel will be overwritten when a preset is selected!  


### Clear The Panel:
Click the 'Clear' button to remove all current buttons, labels and spacers.  The panel presets will not be affected.


### Save The Panel Layout:
Save the current buttons, labels and spacers to an external file for access later.  
Other panel presets are not saved.  
Click the 'Save' button to open a file browser.  
* Browse to the location you wish to save the panel layout.
* Give the export layout a filename, an extension is not needed.
* Click 'Save Layout' to write the file.


### Load A Panel Layout:
Load a panel preset file by clicking the 'Load' button.  
Be careful not to accidentally load a file that is not a layout, a lot of garbage buttons can be created!  
Loading a layout will completely replace the current button layout.  
A file browser will open.
* Browse to the folder where a layout was saved.
* Double click on the layout file, or click it once and click the 'Load Layout' button in the upper right.



# Using The Panel:
Once you have the panel set up the way you like it, be sure to save your .blend file.  
Set up your panels with your favorite default buttons in a blank startup file, then in the file menu, click 'Save Startup File' to have these buttons on every new blender file.  

If you created multiple presets, a 'Panel Presets' drop-down menu will be visible at the top of the panel.  Select a preset from this menu to load it into the panel.  
Now, simply click one of the buttons to activate the script behind it.  

You may call a popup version of the panel in any Blender area that has a panel enabled by pressing Ctrl-Shift-Space.  

You may directly activate each button of the panel by pressing Ctrl-Shift-'Number Key'. Ctrl-Shift-1 will activate the top button, Ctrl-Shift-2 the second button, etc... up to Ctrl-Shift-0 for button 10.  



# Creating Your Own Scripts:
If you don't know any python, it is far too complex of a subject to cover here.  Read a book on learning python 3, check out Blender's python api documentation, and learn from the many great addons that have been released for Blender.  
However, if you know some python, creating your own buttons can be easy and fun.  

The only non-standard element of a button script is the first line - If the first line of the script is a comment, it can be evaluated as a true-false statement that will disable the button if it is false.  
For instance:  
`#len(bpy.context.scene.objects) > 0`  

This will disable the button if there are no objects in the current scene.  
After this line, simply follow with any python code you wish: other comments, imports, functions, classes, or just a list of commands.  

Script Shortcut will also call the register function (`def register():`) if it is defined in the python file before executing the script, you will not need to call it in the code itself.  
See the 'test.py' file in the buttons directory for some example code.  



# Changelog:
### 0.3
   * Initial Release

### 0.4
   * Added popup menu with the shortcut Ctrl-Shift-Space that pops up the current panel for an area
   * Added a change script button to the button editor dialog
   * Implemented stored panel presets through a drop-down menu

### 0.5
   * Made panel settings into addon preferences, they no longer clog up the window view menu with a settings menu
   * Resolved error messages when loading script

### 0.6
   * Cleaned up code
   * Added ability to call buttons with Ctrl-Shift-'Number Key'
   * When creating a new button, the filename is first used for the title, then user is asked to rename
