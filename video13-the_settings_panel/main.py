
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import SettingsWithSidebar

from settingsjson import settings_json

Builder.load_string('''
<Interface>:
    orientation: 'vertical'
    Button:
        text: 'open the settings!'
        font_size: 150
        on_release: app.open_settings()
''')

class Interface(BoxLayout):
    pass

class SettingsApp(App):
    def build(self):
        self.settings_cls = SettingsWithSidebar
        self.use_kivy_settings = False
        setting = self.config.get('example', 'boolexample')
        return Interface()

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option2',
            'stringexample': 'some_string',
            'pathexample': '/some/path'})

    def build_settings(self, settings):
        settings.add_json_panel('Panel Name',
                                self.config,
                                data=settings_json)

    def on_config_change(self, config, section,
                         key, value):
        print config, section, key, value


SettingsApp().run()
