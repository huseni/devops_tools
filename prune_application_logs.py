#!/usr/bin/env python
#######################################################################################################################
#                                                                                                                     #
# THIS SCRIPT IS TO CLEAR ALL THE LOG, ERROR AND INFO FILES OLDER THAN 5 DAYS IN THE SPECIFIED DIRECTORY              #
# PERIODICALLY.                                                                                                       #
# VERSION 1.0                                                                                                         #
# USAGE:                                                                                                              #
#       python prune_application_logs.py                                                                              #
#                                                                                                                     #
#######################################################################################################################
import sys
import subprocess
import time
import os
from datetime import datetime


def get_file_last_modification_date(filename=None):
    """
    Get the file name for the status
    :param filename:
    :return:
    """
    with open(filename, 'r') as fp:
        for line in fp:
            if line.startswith('Modify'):
                date_line = line.split()[1]
                file_date = datetime.strptime(date_line, "%Y-%m-%d")
        return filename, file_date


def get_current_date():
    """
    To find the current date of the host machine
    :return:
    """
    cmd = '/bin/date +\%Y-\%m-\%d'
    t_pid = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = t_pid.communicate()
    if not out:
        print("Error while running the command for capturing the date")
        sys.exit(1)
    date_ = out.split()[0]
    current_date = datetime.strptime(date_ , "%Y-%m-%d")
    return current_date


def get_list_of_files_in_dir(file_list_path=None):
    """
    This will return all the files available in the specified directory
    :param directory:
    :return:
    """
    return os.listdir(file_list_path)


def remove_files(filename=None):
    """
    To remove the file specified in this.
    :param filename:
    :return:
    """
    os.remove(filename)
    print("The file %s has been removed" % filename)


def get_file_stat(dir_path, stat_file, filename=None ):
    """
    To get the file stat information to calculate the date difference of it
    :param filename:
    :return:
    """
    new_dir_path = os.path.join(dir_path, filename)
    file_stat_cmd = 'stat %s' % new_dir_path
    file_stat = subprocess.Popen(file_stat_cmd, stdout=subprocess.PIPE, shell=True)
    out, err = file_stat.communicate()
    if out:
        with open(stat_file, 'w') as fs:
            fs.write(out)
    else:
        print("Command could not run. Please check")


def main():
    """
    Main function to start the program execution
    """
    dir_path = '/home/ubuntu/test_files' # path for the log files that needs to be pruned
    stat_file_name = 'file_status_info' # temp file will be created to store the stat of each files to calculate when to delete
    
    # Get the list of all the files where we want to perfrom the delete operations
    file_list = get_list_of_files_in_dir(dir_path)

    # Get the current system date
    current_date = get_current_date()

    # Iterate through all the log, error, info files in the specified directory path and check for the criteria of file older than 5 days and delete.
    for fil in file_list:
        get_file_stat(dir_path, stat_file_name, fil)
        filename, file_date = get_file_last_modification_date(stat_file_name)

        print("*********** %s file stat is written **************" % fil)
        days = abs(current_date - file_date).days
        
        # Check if the file modification date if older than 5 days.
        if days > 5:
            remove_files(os.path.join(dir_path, fil))
        else:
            print("No eligible file(s) found to be deleted")


if __name__ == '__main__':
    main()