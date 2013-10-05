#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-

from kivy.app import App
from widgets import MainView


class TasksApp(App):
    title = 'Taski'

    def build(self):
        return MainView(self.config)

    def build_config(self, config):
        config.read('config.ini')

if __name__ == '__main__':
    TasksApp().run()
