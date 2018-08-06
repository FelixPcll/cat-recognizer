"""To run the classifier, all the images must be in the same size.
This script will scan the folders and resize all the images from them
and put all in a new folder

"""

import os
import cv2


def resize_square_and_save(image_current_path, shape, save_path):
    original_image = cv2.imread(image_current_path, 1)
    original_size = original_image.shape[:2]  # (height, width)

    ratio = float(shape)/max(original_size)

    format_size = tuple(reversed([int(i*ratio)
                                  for i in original_size]))  # (width, height)

    resized_image = cv2.resize(original_image, format_size)

    d_w = shape - format_size[0]
    d_h = shape - format_size[1]

    top, bottom = d_h//2, d_h-(d_h//2)
    left, right = d_w//2, d_w-(d_w//2)

    color = [0, 0, 0]

    squared_image = cv2.copyMakeBorder(
        resized_image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

    cv2.imwrite(save_path, squared_image)


def run(folder, shape):
    root0 = os.getcwd()
    dir0 = os.path.join(root0, folder)
    if os.path.isdir(dir0):
        root1, dir1, file1 = [i for i in os.walk(dir0)][0]
        for sub_folder in dir1:
            # Create the new path to drop the formatted figures
            new_path = os.path.join(root0, 'formatted images/'+sub_folder)
            try:
                os.makedirs(new_path)
            except:
                pass

            old_path = os.path.join(root1, sub_folder)
            walk = [i for i in os.walk(old_path)][1:]

            for root, folder_list, img_list in walk:
                for img in img_list:
                    im_path = os.path.join(root, img)
                    save_path = os.path.join(new_path, img)

                    resize_square_and_save(im_path, shape, save_path)

    else:
        raise FileNotFoundError(
            "Can't find a folder called {} on this directory.".format(folder))


run('images', 150)
