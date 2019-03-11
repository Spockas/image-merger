from PIL import Image
import glob
import os

class Merger:

    def __init__(self):
        self.load_settings()

    def load_settings(self):
        # TODO
        a = 1

    def set_main_image(self, location) -> bool:
        try:
            self.main_image = Image.open(location)
        except IOError:
            return False
        return True


    def read_designs(self, folder):
        self.filenames = glob.glob(os.path.join(folder, '*.png'))
        self.which_design = 0
        self.set_design_image(os.path.join(folder, self.filenames[0]))


    def set_design_folder(self, folder) -> None:
        self.folder = folder
        self.read_designs(folder)

    def merge_all(self):
        # TODO

    def merge_current(self):


    def resize_to_fit(self):


    def set_design_image(self, location):
        try:
            self.design_image = Image.open(location)
        except IOError:
            return False
        return True

        return

