#!/usr/bin/env python
######################################################################################
#                                                                                    #
# THIS PROGRAM IS TO MONITOR THE UDP PORT WITH THE SERVICE IF CLOSED                 #
# OR OPENED. IF PORT IS CLOSED MEANS NO CONNECTIONS AND WE ALERT.                    #
# V. 1.0                                                                             #
#                                                                                    #
######################################################################################
import subprocess
from pprint import pprint


def monitor_udp_status(port, host_ip_or_name):
    """
    To clear the page cache from the host machine
    :param process:
    :return:
    """
    udp_command = 'nmap -P0 -sU -p%d %s' % (port, host_ip_or_name)
    udp_process = subprocess.Popen(udp_command, stdout=subprocess.PIPE, shell=True)
    pprint(udp_process)
    out, err = udp_process.communicate()
    pprint(out, err)


def main():
    host_ip = 'my_application.example.com'
    host_udp_or_tcp_port = 74638
    monitor_udp_status(host_udp_port, host_ip)


if __name__ == "__main__":
    main()