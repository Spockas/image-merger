import merger as mg
import time


beg = time.time()
merger = mg.Merger()
design_path = "./designs"
hoodie_path = "./hoodie.png"

merger.set_design_folder(design_path)
merger.set_main_image(hoodie_path)

print(merger.filenames)
print(merger.step)
print(merger.output_append)
# merger.set_design_image(design_path + '/' + merger.filenames[0])
# merger.design_image.show()
merger.get_display()
start = time.time()
merger.resize_for_hoodie(quality=True)
print((time.time() - start))
# merger.design_image.show()
merger.move_down(80)
merger.move_right(80)

start = time.time()
merger.merge_current()
print((time.time() - start))
print("Merging all starts")
start = time.time()
merger.merge_all()
print((time.time() - start))
# merger.merged_image.show()
# merger.write_to_file()
# merger.main_image.show()


print("Final time:", (time.time() - beg))