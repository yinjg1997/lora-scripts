import os
import shutil


def move_jpg_files(src_dir, dest_dir):
    # 确保目标文件夹存在
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍历源文件夹
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)

        if os.path.isdir(src_path):
            # 如果是文件夹，递归调用
            move_jpg_files(src_path, dest_dir)
        elif item.lower().endswith('.jpg'):
            # 如果是.jpg文件，移动到目标文件夹
            dest_path = os.path.join(dest_dir, item)
            shutil.move(src_path, dest_path)
            print(f"Moved: {src_path} to {dest_path}")

move_jpg_files(src_dir=fr'C:\Users\he3\Desktop\rizzzz-scripts\spider\xiao_hong_shu\scrape_posts\crawled_data\5af2ad89f7e8b942e5fbaebd', 
               dest_dir=fr'datasets/images')