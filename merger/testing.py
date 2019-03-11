import merger

merger = merger.Merger()
design_path = "./designs"
hoodie_path = "./hoodie.png"

merger.set_design_folder(design_path)
merger.set_main_image(hoodie_path)

print(merger.filenames)
print(merger.step)
print(merger.output_append)
# merger.set_design_image(design_path + '/' + merger.filenames[0])
merger.design_image.show()
merger.resize_to_fit()
merger.design_image.show()
merger.merge_current()
merger.merged_image.show()
# merger.main_image.show()