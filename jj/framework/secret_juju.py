# Secret JuJu Framework!
#
# The framework will be using "lazy" loading.
# that way, the program will do every thing when
# it's needed. and procrastinating the job.
#
#

from jj.framework.gui import guimanager
from jj.framework.file.juju_file_utility import *

JJ_IS_RUNNING = 0b1

class juju:
    def __init__(self):
        print("시크릿 쥬쥬라규~!")

        self.ui_manager = guimanager()
        self.file_manager = jj_mini_repository("window_data")

        self.loading_object = None

        #0b*  is for running?
        #0b0* is for need loading?
        self.flag: int = 0b0

    def bind_loading_object(self, object):
        self.loading_object = object

    def program_loop(self):

        while self.flag & JJ_IS_RUNNING == 1:


            pass

    def start(self):
        self.run = True
        self.program_loop()
