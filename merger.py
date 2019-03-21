from PIL import Image, ImageTk
import glob
import os
import json

class Merger:
    def __init__(self):
        self.load_settings()
        self.design_image = None
        self.design_image_resized = None
        self.main_image = None
        self.design_image_name = None
        self.merged_image = None
        self.offset = [0, 0]
        self.output_path = None
        self.display_image = None
        self.centre = [0, 0]
        self.ratio = 1.414196123147092
        self.set_size = (600, int(600 * self.ratio))

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
                self.overwrite = settings_dict['overwrite']
                return
        self.step = 5
        self.output_append = "_applied"
        self.overwrite = True
        return

    def set_main_image(self, location) -> bool:
        try:
            self.main_image = Image.open(location)
        except IOError:
            "error: can't set main image"
            return False
        return True

    def merge_current(self, centre=None):
        if not self.design_image is None and not self.main_image is None:
            if self.design_image_resized is None:
                self.resize_to_set_size()
            if centre is None:
                centre = self.find_centre()
            if self.offset != [0, 0]:
                centre = list(centre)
                centre[0] += self.offset[0]
                centre[1] += self.offset[1]
                centre = tuple(centre)
            self.merged_image = self.main_image.copy()
            self.merged_image.alpha_composite(self.design_image_resized, centre)
            self.display_image = None
        else:
            print("Error: images not set")
        return

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
        counter = 0
        for filename in self.filenames:
            if not self.design_image_name == filename:
                self.set_design_image(filename)
            self.resize_to_set_size()
            self.merge_current()
            self.write_to_file(self.output_path)
            counter += 1
            print(counter, self.design_image_name)
        return

    def resize_for_hoodie(self, size=600, quality=True):
        if quality:
            filter_to_use = Image.LANCZOS
        else:
            filter_to_use = Image.NEAREST
        self.design_image_resized = self.design_image.resize((size, int(self.ratio * size)), filter_to_use)
        self.set_size = (size, int(self.ratio * size))

    def resize_to_set_size(self, size=None, quality=True):
        if size is None:
            size = self.set_size
        if quality:
            filter_to_use = Image.LANCZOS
        else:
            filter_to_use = Image.NEAREST
        self.design_image_resized = self.design_image.resize(size, filter_to_use)

    def set_design_image(self, location):
        try:
            self.design_image = Image.open(location)
            self.design_image_name = os.path.basename(location)
            self.merged_image = None
            self.design_image_resized = None
        except IOError:
            print("Something very bad with design images")
            return False
        self.display_image = None
        return True

    def find_centre(self) -> (int, int):
        centre = (int((self.main_image.size[0] - self.design_image_resized.size[0]) / 2), int((self.main_image.size[1] - self.design_image_resized.size[1]) / 2))
        return centre

    def get_display(self, size=340):
        if self.merged_image is None:
            self.merge_current()
        if self.display_image == None:
            self.display_image = self.merged_image.resize((int(size / self.ratio), size))
        return self.display_image

    def change_settings(self, **kwargs):
        return

    def set_output_path(self, path):
        self.output_path = path

    def write_to_file(self, path=None):
        if path is None:
            path = os.path.join(self.folder, "applied", os.path.splitext(self.design_image_name)[0] + self.output_append + os.path.splitext(self.design_image_name)[1])
        else:
            path = os.path.join(path, os.path.splitext(self.design_image_name)[0] + self.output_append + os.path.splitext(self.design_image_name)[1])
        if os.path.exists(path) and not self.overwrite:
            return
        if self.merged_image is None:
            self.merge_current()
        self.merged_image.save(path)

    def add_blur(self):
        # TODO
        return

    def move_up(self, step=None):
        if step is None:
            step = self.step
        self.offset[1] -= step
        self.merge_current()
        return


    def move_down(self, step=None):
        if step is None:
            step = self.step
        self.offset[1] += step
        self.merge_current()
        return

    def move_right(self, step=None):
        if step is None:
            step = self.step
        self.offset[0] += step
        self.merge_current()
        return

    def move_left(self, step=None):
        if step is None:
            step = self.step
        self.offset[0] -= step
        self.merge_current()
        return
