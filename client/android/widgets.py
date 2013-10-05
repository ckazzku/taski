#-*- coding:utf-8 -*-

import json

from kivy.logger import Logger
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty
from kivy.uix.accordion import AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
from kivy.uix.settings import Settings

from client import RestClient
from data import Data


class ErrorPopup(Popup):
    message = StringProperty('')


class AddTaskView(ModalView):

    def add_data(self):
        data = Data.get_data()
        data['id'] = None  # чтобы на сервере id сгенерилось
        Logger.debug('Add data: {}'.format(data))
        data = json.dumps(data)
        RestClient.post(data)
        RestClient.get()


class ContentView(GridLayout):
    current = NumericProperty(0)


class Item(AccordionItem):
    first = BooleanProperty(False)

    def __init__(self, content, **kwargs):
        super(Item, self).__init__(**kwargs)
        self.add_widget(content)


class MainView(BoxLayout):
    accordion = ObjectProperty()

    def __init__(self, config, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.config = config
        RestClient.url = config.get('server', 'address')
        RestClient.callback = self._handle_result
        RestClient.errback = self._handle_error
        self.get_all()

    def _handle_result(self, req, res):
        objects = None
        if res:
            json_dic = json.loads(res, encoding='utf-8')
            if 'objects' in json_dic:
                objects = json_dic['objects']
            else:
                objects = [json_dic]

        if objects:
            self.accordion.clear_widgets()
            Data.clear_data()
            for obj in objects:
                Data.add_data(obj)
                obj_id = obj['id']
                Data.current = obj_id
                obj_title = obj['title']
                item = Item(content=ContentView(current=obj_id),
                            title=u'{0}: {1}'.format(obj_id, obj_title))
                self.accordion.add_widget(item)

    def _handle_error(self, req, err):
        Logger.error(str(err))
        popup = ErrorPopup(message=str(err))
        popup.open()

    def sort(self):
        pass

    def get_all(self):
        RestClient.get()

    def add_new(self):
        Data.current = -1
        Data.add_data({'id': -1})
        view = AddTaskView()
        view.open()

    def update_current(self):
        data_id = Data.current
        data = Data.get_data()
        Logger.debug('Update data: {}'.format(data))
        data = json.dumps(data)
        RestClient.patch(data, '/{}'.format(data_id))
        self.get_all()

    def del_current(self):
        data_id = Data.current
        RestClient.delete('/{}'.format(data_id))
        self.get_all()

    def show_settings(self):
        settings = Settings()
        settings.add_json_panel(
            'My custom panel', self.config, 'settings.json')
        settings.bind(on_close=self.remove_widget)
        self.add_widget(settings)
