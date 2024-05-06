import os

def batch_rename_files(folder_path, extension):
    file_list = os.listdir(folder_path)
    for filename in file_list:
        new_name = int(filename[:-4]) - 32
        old_file_path = os.path.join(folder_path, filename)
        new_filename = f"{new_name:03d}.{extension}"
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)

# 使用示例
folder_path = "C:\\Code\\VideoProcess\\VideoStitchingViaShakinessRemoving\\case-cuhk_lib\\process\\right_down_back\\"
# folder_path = "./right"
# out_path = "./right"
extension = "jpg"
batch_rename_files(folder_path, extension)
