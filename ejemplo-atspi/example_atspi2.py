#!/usr/bin/env python3.9

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, GdkPixbuf



class App():
    def __init__(self):
        self.load_widgets()


    def run(self):
        self.window.show_all()
        Gtk.main()
        
        
    def load_widgets(self):	
        self.window = Gtk.Window()
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.entry = Gtk.Entry()
        self.button = Gtk.Button(label="Add")

        self.liststore = Gtk.ListStore(str, str)
        treeview = Gtk.TreeView(model=self.liststore)
        renderer_text = Gtk.CellRendererText()
        column1 = Gtk.TreeViewColumn("Uppercase", renderer_text, text=0)
        column2 = Gtk.TreeViewColumn("Lowercase", renderer_text, text=1)
        treeview.append_column(column1)
        treeview.append_column(column2)
        
        self.box.pack_start(self.entry, False, False, 0)
        self.box.pack_start(self.button, False, False, 0)
        self.box.pack_start(treeview, True, True, 0)
        
        self.window.add(self.box)
        
        self.button.connect("clicked", self.on_convert_button_clicked)
        self.window.connect("delete-event", self.on_window_delete_event)
        
        # Set a name to gtk widgets in order to find them by name
        # in the Atspi tree
        entry_accessible = self.entry.get_accessible()
        entry_accessible.set_name("string_entry")
        button_accessible = self.button.get_accessible()
        button_accessible.set_name("convert_button")
        treeview_accessible = treeview.get_accessible()
        treeview_accessible.set_name("string_treeview")
        
        
        
  
    def on_convert_button_clicked(self, arg):
        s = self.entry.get_text()
        self.liststore.append([s.upper(),s.lower()])
        self.entry.set_text('')
        
    
    def on_window_delete_event(self, arg1, arg2):
        Gtk.main_quit()
        
       
a = App()
a.run()
	



