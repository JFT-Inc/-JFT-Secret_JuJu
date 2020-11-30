from jj.framework.gui import guimanager
from jj.framework.juju_file_utility import *

class juju:
    def __init__(self):
        print("시크릿 쥬쥬라규~!")

        self.run: bool = False
        self.ui_manager = guimanager()
        self.file_manager = jj_mini_repository("window_data")

    def pre_loading(self, functions):
        pass

    def main_loading(self, function):
        pass

    def program_loop(self):
        while self.run:
            pass

    def start(self):
        self.run = True
        self.program_loop()
