# !/usr/bin/python
# -*- coding: utf-8 -*-
# Execution example : python script.py


#
# Libs
#
import logging
import os
import shutil


#
# Config
#
log_file = 'script.log'
log_level = logging.DEBUG
path = '/Users/anne/Downloads/archelec'
folder_splitator = '_'


#
# Functions
#
def main() :
    global path
    # Iterate over folder, depth 1
    for folder_01 in os.listdir(path) :
        # If it is a folder
        if not os.path.isfile(os.path.join(path, folder_01)) :
            # Iterate over folder, depth 2
            # This depth will be skipped
            for folder_02 in os.listdir(os.path.join(path, folder_01)) :
                # If it is a folder and folder's name starts with "EL"
                if not os.path.isfile(os.path.join(path, folder_01, folder_02)) and folder_02.startswith('EL') :
                    # Rename folder from ELxx_L_1973_(...) to L_1973_(...)
                    folder_02_new_name = folder_splitator.join(folder_02.split(folder_splitator)[1:])
                    # Iterate over folder, depth 3
                    for folder_03 in os.listdir(os.path.join(path, folder_01, folder_02)) :
                        # If it is a folder
                        if not os.path.isfile(os.path.join(path, folder_01, folder_02, folder_03)) and folder_03.startswith('EL') :
                            # Rename folder from XXX to XXX
                            folder_03_new_name = folder_splitator.join(folder_03.split(folder_splitator)[1:])
                            os.mkdir(os.path.join(path, folder_01, folder_03_new_name))
                            # Iterate over folder, depth 4
                            for folder_04 in os.listdir(os.path.join(path, folder_01, folder_02, folder_03)) :
                                # If it is a folder
                                if not os.path.isfile(os.path.join(path, folder_01, folder_02, folder_03, folder_04)) :
                                    # Iterate over folder, depth 5
                                    for folder_05 in os.listdir(os.path.join(path, folder_01, folder_02, folder_03, folder_04)) :
                                        # If it is a folder and belongs to a restricted list
                                        if not os.path.isfile(os.path.join(path, folder_01, folder_02, folder_03, folder_04, folder_05)) and folder_05 in ['master', 'pdfmasterocr', 'view'] :
                                            # Create subfolder folder_05 if it doesn't exist
                                            if not os.path.exists(os.path.join(path, folder_01, folder_03_new_name, folder_05)) :
                                                os.mkdir(os.path.join(path, folder_01, folder_03_new_name, folder_05))
                                            # Iterate over folder, depth 6
                                            for folder_06 in os.listdir(os.path.join(path, folder_01, folder_02, folder_03, folder_04, folder_05)) :
                                                # Don't copy Mac files
                                                if not folder_06 in ['Thumbs.db'] :
                                                    shutil.move(os.path.join(path, folder_01, folder_02, folder_03, folder_04, folder_05, folder_06), os.path.join(path, folder_01, folder_03_new_name, folder_05))
                    shutil.rmtree(os.path.join(path, folder_01, folder_02))


#
# Main
#
if __name__ == '__main__' :
    # Init logs
    logging.basicConfig(filename = log_file, filemode = 'a', format = '%(asctime)s  |  %(levelname)s  |  %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p', level = log_level)
    logging.info('Start')
    main()
    logging.info('End')