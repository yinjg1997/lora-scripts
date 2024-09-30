import warnings

from PIL import Image

warnings.filterwarnings("ignore", category=FutureWarning)

import os
import shutil


def move_jpg_files(src_dir, dest_dir):
    # 确保目标文件夹存在
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.move(src_path, dest_path)
                print(f"Moved: {src_path} to {dest_path}")



def center_crop(image_path, output_path, crop_width: int = 1080, crop_height: int = 1080):
    """
    对图像进行中央裁剪
    :param image_path: 输入图像的路径
    :param output_path: 输出图像的路径
    :param crop_width: 裁剪后的宽度
    :param crop_height: 裁剪后的高度
    """
    # 打开图像
    image = Image.open(image_path)
    img_width, img_height = image.size

    # 计算左上角和右下角的坐标
    left = (img_width - crop_width) / 2
    top = (img_height - crop_height) / 2
    right = (img_width + crop_width) / 2
    bottom = (img_height + crop_height) / 2

    # 裁剪图像
    cropped_image = image.crop((left, top, right, bottom))

    # 保存裁剪后的图像
    cropped_image.save(output_path)


def batch_process(callback):
    dirs_path = r'C:\Users\he3\Desktop\rizzzz-scripts\spider\xiao_hong_shu\scrape_posts\crawled_data\5af2ad89f7e8b942e5fbaebd'

    for root, dirs, files in os.walk(dirs_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.jpg'):
                callback(file_path, file_path)


if __name__ == '__main__':
    datasets_images_dir = r'C:\Users\he3\Desktop\lora-scripts\datasets\images'

    # batch_process(center_crop)

    dirs_path = r'C:\Users\he3\Desktop\rizzzz-scripts\spider\xiao_hong_shu\scrape_posts\crawled_data\5af2ad89f7e8b942e5fbaebd'
    move_jpg_files(dirs_path, datasets_images_dir)
    pass
