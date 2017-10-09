#!/usr/bin/env python
######################################################################################
#                                                                                    #
# THIS PROGRAM IS TO SEARCH THE CONFIG TEXT IN THE FILE AND REPLACE WITH THE VALUE   #
# SPECIFIED                                                                          #
# V. 1.0                                                                             #
#                                                                                    #
######################################################################################
import os
import sys
import fileinput


def search_and_replace_config(param_dict, config_file):
    """
    To search and replace the text config string the file
    :return:
    """
    if param_dict is None:
        raise ValueError('could not find parameters to update the configuration: %s' % param_dict)

    if config_file is None:
        raise ValueError('could not find config file to update the configuration: %s' % config_file)

    search_users_config = param_dict['search_users_config']
    replace_users_config = param_dict['replace_users_config']
    search_processes_config = param_dict['search_processes_config']
    replace_processes_config = param_dict['replace_processes_config']
    search_users_config_ubuntu = param_dict['search_users_config_ubuntu']
    replace_users_config_ubuntu = param_dict['replace_users_config_ubuntu']
    search_processes_config_ubuntu = param_dict['search_processes_config_ubuntu']
    replace_processes_config_ubuntu = param_dict['replace_processes_config_ubuntu']

    print ("File to perform search and replace on: %s" % config_file)

    modify_config_file(param_dict, config_file, search_users_config, replace_users_config)
    modify_config_file(param_dict, config_file, search_processes_config, replace_processes_config)
    modify_config_file(param_dict, config_file, search_users_config_ubuntu, replace_users_config_ubuntu)
    modify_config_file(param_dict, config_file, search_processes_config_ubuntu, replace_processes_config_ubuntu)


def modify_config_file(config_file, search_config, replace_config):
    """
    To read the config file, modify the threshold content and truncate the file
    """
    with open(config_file, 'r+') as f:
        content = f.read()
        f.seek(0)
        f.write(content.replace(search_config, replace_config))
        f.truncate()
        f.close()

def main():
    config_file = '/etc/nagios/nrpe.cfg'
    param_dict = {"search_users_config": "command[check_users]=/usr/lib64/nagios/plugins/check_users -w 5 -c 10",
                  "replace_users_config": "command[check_users]=/usr/lib64/nagios/plugins/check_users -w 300 -c 500",
                  "search_processes_config": "command[check_total_procs]=/usr/lib64/nagios/plugins/check_procs -w 250 -c 400",
                  "replace_processes_config": "command[check_total_procs]=/usr/lib64/nagios/plugins/check_procs -w 450 -c 600",
                  "search_users_config_ubuntu": "command[check_users]=/usr/lib/nagios/plugins/check_users -w 5 -c 10",
                  "replace_users_config_ubuntu": "command[check_users]=/usr/lib/nagios/plugins/check_users -w 300 -c 500",
                  "search_processes_config_ubuntu": "command[check_total_procs]=/usr/lib/nagios/plugins/check_procs -w 250 -c 400",
                  "replace_processes_config_ubuntu": "command[check_total_procs]=/usr/lib/nagios/plugins/check_procs -w 450 -c 600"
                  }

    search_and_replace_config(param_dict, config_file )


if __name__ == '__main__':
    main()