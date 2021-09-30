#!/usr/bin/env python3.9

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, GdkPixbuf

GLADE_FILE = './example_atspi.glade'

class App():
    def __init__(self):
        self.load_widgets()


    def run(self):
        self.window.show_all()
        Gtk.main()
        
        
    def load_widgets(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(GLADE_FILE)
        self.window = self.builder.get_object("window")
        self.entry = self.builder.get_object("string_entry")
        self.liststore = self.builder.get_object("liststore")   
        self.builder.connect_signals(self)
 
  
    def on_convert_button_clicked(self, arg):
        s = self.entry.get_text()
        self.liststore.append([s.upper(),s.lower()])
        self.entry.set_text('')
        
    
    def on_window_delete_event(self, arg1, arg2):
        Gtk.main_quit()
        
       
a = App()
a.run()
	



