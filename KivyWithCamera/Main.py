''' replace with your current kivy version !
To get kivy version you can execute:
    print "Kivy Version: ", kivy.__version__'''
import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# For settings screen
from kivy.uix.settings import SettingsWithSidebar

Builder.load_string("""
<PantallaDeMenu>:
    GridLayout:
        rows: 2
        size_hint: (None, 1)
        width: 800
        BoxLayout:
            size_hint: (1, None)
            height: 50
            Button:
                text: 'Buscar'
                on_press: root.manager.current = 'busqueda'
            Button:
                text: 'Agregar'
                on_press: root.manager.current = 'insertar'
            Button:
                text: 'Editar'
                on_press: root.manager.current = 'editar'
            Button:
                text: 'Eliminar'
                on_press: root.manager.current = 'eliminar'
            Button:
                text: 'Configuracion'
                on_release: app.open_settings()
            Button:
                text: 'Salir'
                id: btnExit
                on_press: app.stop()
        Label:
            text: 'Label'

<PantallaDeBusqueda>:
    GridLayout:
        rows: 2
        size_hint: (None, 1)
        width: 800
        BoxLayout:
            size_hint: (1, None)
            height: 50
            Button:
                text: 'Busqueda'
            Button:
                text: 'Regresar a Menu'
                on_press: root.manager.current = 'menu'
        Label:
            text: 'Label'

<PantallaDeInsertar>:
    GridLayout:
        rows: 2
        size_hint: (None, 1)
        width: 800
        BoxLayout:
            size_hint: (1, None)
            height: 50
            Button:
                text: 'Insertar'
            Button:
                text: 'Regresar a Menu'
                on_press: root.manager.current = 'menu'

<PantallaDeEditar>:
    GridLayout:
        rows: 2
        size_hint: (None, 1)
        width: 800
        BoxLayout:
            size_hint: (1, None)
            height: 50
            Button:
                text: 'Editar'
            Button:
                text: 'Regresar a Menu'
                on_press: root.manager.current = 'menu'

<PantallaDeEliminar>:
    GridLayout:
        rows: 2
        size_hint: (None, 1)
        width: 800
        BoxLayout:
            size_hint: (1, None)
            height: 50
            Button:
                text: 'Eliminar'
            Button:
                text: 'Regresar a Menu'
                on_press: root.manager.current = 'menu'

""")


# Declare screens
class PantallaDeMenu(Screen):
    pass


class PantallaDeBusqueda(Screen):

    pass


class PantallaDeInsertar(Screen):

    pass


class PantallaDeEditar(Screen):
    pass


class PantallaDeEliminar(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(PantallaDeMenu(name='menu'))
sm.add_widget(PantallaDeBusqueda(name='busqueda'))
sm.add_widget(PantallaDeInsertar(name='insertar'))
sm.add_widget(PantallaDeEditar(name='editar'))
sm.add_widget(PantallaDeEliminar(name='eliminar'))

jsonSettings = """
[
    {
        "type": "string",
        "title": "MySQL Host",
        "desc": "Nombre del Host para la conexion de MySQL",
        "section": "MySQL Config",
        "key": "mysqlhost"
    },
    {
        "type": "string",
        "title": "MySQL User",
        "desc": "Usuario con permiso de Dba para el Host de MySQL",
        "section": "MySQL Config",
        "key": "mysqluser"
    },
    {
        "type": "string",
        "title": "MySQL Password",
        "desc": "Password del usuario de MySQL",
        "section": "MySQL Config",
        "key": "mysqlpwd"
    },
    {
        "type": "numeric",
        "title": "MySQL Puerto",
        "desc": "Puerto para la conexion clasica a MySQL",
        "section": "MySQL Config",
        "key": "mysqlport"
    }
]
"""


class TarjeteroApp(App):

    def build(self):
        self.settings_cls = SettingsWithSidebar
        return sm

    def build_config(self, config):
        config.setdefaults('MySQL Config', {
            "mysqlhost": "localhost",
            "mysqluser": "root",
            "mysqlpwd": "mypwd",
            "mysqlport": 5717})

    def build_settings(self, settings):
        settings.add_json_panel('MySQL Config',
                                self.config,
                                data=jsonSettings)


if __name__ == '__main__':
    TarjeteroApp().run()

