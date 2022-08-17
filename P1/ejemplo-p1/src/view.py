#!/usr/bin/env python3

import locale
import gettext

_ = gettext.gettext
N_ = gettext.ngettext


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Atk


class View:
    @classmethod
    def main(cls):
        Gtk.main()

    @classmethod
    def main_quit(cls, w, e):
        Gtk.main_quit()

        
    def build_view(self, date_sample= ""):
        flight_type_store = Gtk.ListStore(str)
        flight_type_store.append([_("one-way flight")])
        flight_type_store.append([_("return flight")])
        self.flight_type = Gtk.ComboBox(model=flight_type_store,
                                        entry_text_column= 0,
                                        active= 0)
        renderer_text = Gtk.CellRendererText()
        self.flight_type.pack_start(renderer_text, True)
        self.flight_type.add_attribute(renderer_text, "text", 0)

        label_start_date = Gtk.Label(label= _("Start date:"), xalign=0)
        self.start_date = Gtk.Entry(text= "")
        self.start_date.set_placeholder_text(_("Ex. {}").format(date_sample))
        self.start_date.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY,
                                                          label_start_date.get_accessible())
        label_return_date = Gtk.Label(label= _("Return date:"), xalign=0)
        self.return_date = Gtk.Entry(text= "")
        self.return_date.set_placeholder_text(_("Ex. {}").format(date_sample))
        self.return_date.get_accessible().add_relationship(Atk.RelationType.LABELLED_BY,
                                                           label_return_date.get_accessible())
        self.book = Gtk.Button(label= _("Book"))

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10, margin=10)
        vbox.pack_start(self.flight_type, False, False, 0)
        vbox.pack_start(label_start_date, False, False, 0)
        vbox.pack_start(self.start_date, False, False, 0)
        vbox.pack_start(label_return_date, False, False, 0)
        vbox.pack_start(self.return_date, False, False, 0)
        vbox.pack_start(self.book, False, False, 0)
        
        self.win = Gtk.Window(title= _("FLIGHT BOOKER"))
        self.win.set_default_size(1,1) # Trick, Is there a cleaner way?
        self.win.add(vbox)


    def show_all(self):
        self.win.show_all()

    def connect_delete_event(self, fun):
        self.win.connect('delete-event', fun)

    def connect_flight_type_changed(self, fun):
        self.flight_type.connect('changed', fun)

    def connect_start_date_changed(self, fun):
        self.start_date.connect('changed', fun)

    def connect_return_date_changed(self, fun):
        self.return_date.connect('changed', fun)

    def connect_book_clicked(self, fun):
        self.book.connect('clicked', fun)

    def update_view(self, **kwargs):
        for name, value in kwargs.items():
            if name == 'flight_type':
                self.flight_type.set_active(value)
            elif name == 'start_date':
                self.start_date.set_text(value)
            elif name == 'return_date':
                self.return_date.set_text(value)
            elif name == 'start_date_is_ok':
                self._update_entry_is_valid(self.start_date, value)
            elif name == 'return_date_is_ok':
                self._update_entry_is_valid(self.return_date, value)
            elif name == 'return_date_enabled':
                self.return_date.set_sensitive(value)
            elif name == 'book_enabled':
                self.book.set_sensitive(value)
            else:
                raise TypeError(f"update_view() got an unexpected keyword argument '{name}'")
    
    def _update_entry_is_valid(self, entry, is_valid):
        if is_valid:
            entry.get_style_context().remove_class('error')
        else:
            entry.get_style_context().add_class('error')
            

    def show_ok(self, text):
        dialog = Gtk.MessageDialog(parent= self.win,
                                   message_type= Gtk.MessageType.INFO,
                                   buttons= Gtk.ButtonsType.OK,
                                   text= text)
        dialog.run()
        dialog.destroy()

    def show_error(self, text):
        dialog = Gtk.MessageDialog(parent= self.win,
                                   message_type= Gtk.MessageType.ERROR,
                                   buttons= Gtk.ButtonsType.CLOSE,
                                   text= text)
        dialog.run()
        dialog.destroy()
