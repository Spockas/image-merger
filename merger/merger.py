from PIL import Image, ImageTk
import glob
import os
import json

class Merger:

    def __init__(self):
        self.load_settings()

    def load_settings(self):
        try:
            settings = open("settings.json", 'r')
        except IOError:
            print("Settings file not found")
        except OSError:
            print("OSError")
        except:
            print("Something else wrong with file")
        else:
            try:
                settings_dict = json.loads(settings.read())
            except json.JSONDecodeError:
                print("Bad json format")
            except:
                print("Something else wrong with json")
            else:
                self.step = settings_dict['step']
                self.output_append = settings_dict['output_append']
                return
        self.step = 0
        self.output_append = "_on_hoodie_empty"
        return

    def set_main_image(self, location) -> bool:
        try:
            self.main_image = Image.open(location)
        except IOError:
            return False
        return True


    def read_designs(self, folder):
        self.filenames = glob.glob(os.path.join(folder, '*.png'))
        self.which_design = 0
        if len(self.filenames) == 0:
            return False
        self.set_design_image(self.filenames[0])


    def set_design_folder(self, folder) -> None:
        self.folder = folder
        self.read_designs(folder)

    def merge_all(self):
        # TODO
        return

    def merge_current(self):
        self.merged_image = self.main_image.copy()
        self.merged_image.alpha_composite(self.design_image)
        return

    def resize_to_fit(self):
        self.design_image = self.design_image.resize(self.main_image.size, Image.LANCZOS)
        return

    def set_design_image(self, location):
        try:
            self.design_image = Image.open(location)
        except IOError:
            print("Something very bad with design images")
            return False
        return True

    def get_display(self, size=256):
        image_to_display = self.merged_image.resize(int(self.merged_image.size[0] / self.merged_image.size[0] * size), size)
        return ImageTk.PhotoImage(image_to_display)

    def move_up(self):
        # TODO
        return


    def move_down(self):
        # TODO
        return


    def move_right(self):
        # TODO
        return


    def move_left(self):
        # TODO
        return



