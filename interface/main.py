import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Interface:
    def __init__(self):
        self.gtk = Gtk
        self.builder = self.gtk.Builder()

        self.builder.add_from_file('./interface/interface.glade')

        self.window = self.builder.get_object('window')
        self.janelinha = self.builder.get_object('janelinha')
        self.texto = self.builder.get_object('texto')
        self.labelzinho = self.builder.get_object('labelzinho')
        self.dialogo = self.builder.get_object('dialogo')
        
        self.janelinha.set_transient_for(self.window)

        self.window.show_all()

        self.window.connect('destroy', self.gtk.main_quit)

    def start(self):
        Gtk.main()

