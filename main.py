#!/usr/bin/python3

import os
import shutil

folder_list = os.listdir(os.getcwd())
for i, curr_folder in enumerate(folder_list):
    print(f"{i}) {curr_folder}")
folder_number = input("Input Folder Number: ")
work_dir = folder_list[int(folder_number)]
for root_folder, main_dirs, main_files in os.walk(work_dir):
    for main_dir in main_dirs:
        try:
            artist = main_dir.split(" - ")[0]
            song = main_dir.split(" - ")[1]
        except IndexError:
            print(f"Nothing to do here for {main_dir}. Skipping...")
            break
        new_work_dir = f"{os.getcwd()}/{work_dir}/{main_dir}"
        artist_folder = f"{os.getcwd()}/{work_dir}/{artist}"
        song_folder = f"{artist_folder}/{song}"
        try:
            os.mkdir(artist_folder)
        except FileExistsError:
            pass
        try:
            os.mkdir(song_folder)
        except FileExistsError:
            pass
        for file in os.listdir(new_work_dir):
            print(f"Copying {file} to new home in {artist} / {song}...")
            file_path = f"{new_work_dir}/{file}"
            shutil.copy2(file_path, song_folder)
        shutil.rmtree(new_work_dir)
