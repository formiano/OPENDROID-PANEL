from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Components.PluginComponent import plugins
from Components.Sources.List import List
from Components.Label import Label
from Components.config import config, configfile
from Screens.MessageBox import MessageBox
from Plugins.Plugin import PluginDescriptor
from Tools.Directories import resolveFilename, SCOPE_SKIN_IMAGE
from Tools.LoadPixmap import LoadPixmap
from AddonsPanel import * 
from Plugin import *
from OPENDROID.OPD_panel import OPD_panel

class GreenPanel(Screen):
	skin = """
		<screen name="GreenPanel" position="center,60" size="1225,635" title="OPENDROID Green Panel" >
		<widget source="list" render="Listbox" position="80,100" size="600,400" enableWrapAround="1" zPosition="2" scrollbarMode="showOnDemand"  transparent="1">
		<convert type="TemplatedMultiContent">
		{"template": [MultiContentEntryText(pos = (115, 3), size = (385, 24), font=0, text = 0),MultiContentEntryText(pos = (115, 25), size = (385, 20), font=1, text = 1),MultiContentEntryPixmapAlphaTest(pos = (5, 5), size = (100, 40), png = 2),],"fonts": [gFont("Regular", 22),gFont("Regular", 18)],
"itemHeight": 50}
		</convert>
		</widget>
		<widget name="key_red" position="135,600" zPosition="1" size="180,45" font="Regular;20" foregroundColor="red" backgroundColor="red" transparent="1" />		
		<widget name="key_green" position="410,600" zPosition="1" size="180,45" font="Regular;20" foregroundColor="green" backgroundColor="green" transparent="1" />
		<widget name="key_yellow" position="675,600" zPosition="1" size="180,45" font="Regular;20" foregroundColor="yellow" backgroundColor="yellow" transparent="1" />
		<widget name="key_blue" position="945,600" zPosition="1" size="180,45" font="Regular;20" foregroundColor="blue" backgroundColor="blue" transparent="1" />
		</screen>"""
	def __init__(self, session):
		Screen.__init__(self, session)
		self.list = []
		self['list'] = List(self.list)
		self.updateList()
		self['key_red'] = Label(_('Ipk Tools'))
		self['key_green'] = Label(_('OPD_panel'))
		self['key_yellow'] = Label(_('Addons '))
		self['key_blue'] = Label(_('Extension Install'))
		self['actions'] = ActionMap(['WizardActions', 'ColorActions'], 
		{'ok': self.save, 
		 'back': self.close, 
		 'red': self.openManualInstaller, 
		 'green': self.OPD_panel, 
		 'yellow': self.openAddonsManager, 
		 'blue': self.ExtensionInstaller
		}, -1)
	def save(self):
		self.run()
	def run(self):
		mysel = self['list'].getCurrent()
		if mysel:
			mysel
			plugin = mysel[3]
			plugin(session=self.session)
		else:
			mysel
	def updateList(self):
		self.list = []
		self.pluginlist = plugins.getPlugins(PluginDescriptor.WHERE_PLUGINMENU)
		for plugin in self.pluginlist:
			if plugin.icon is None:
				png = LoadPixmap(resolveFilename(SCOPE_SKIN_IMAGE, '/usr/share/enigma2/oDreamy-FHD/icons/plugin.png'))
			else:
				png = plugin.icon
			res = (plugin.name, plugin.description, png, plugin)
			self.list.append(res)
		self['list'].list = self.list
		return None
	def openAddonsManager(self):
		self.session.open(AddonsUtility)
	def openManualInstaller(self):
		self.session.open(ManualPanel)
	def OPD_panel(self):
		self.session.open(OPD_panel)	
	def ExtensionInstaller(self):
		self.session.open(InstallFeed)
	def NotYet(self):
		mybox = self.session.open(MessageBox, 'Function Not Yet Available', MessageBox.TYPE_INFO)
		mybox.setTitle(_('Info'))

