import os
import time


class Printer:

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return self.name


def filter_printers(devices_lines):
    printers_list = []
    for line in devices_lines:
        # print(line[0: 7])
        if line[0: 7].lower() == 'printer':
            printer_info = line.split('.  enabled')[0]
            printer_info_s = printer_info.split(' is ')
            printer_name = printer_info_s[0]
            printer_status = printer_info_s[1]
            printer_data = Printer(name=printer_name, status=printer_status)
            printers_list.append(printer_data)

    # print(printers_list)
    # for p in printers_list:
    #     print(p.name + ' is ' + p.status)
    return printers_list


def load_all_printers():
    print('loading all available drivers')
    save_file = ' > devices.txt'
    load_devices_command = 'lpstat -p -d'
    final_command = load_devices_command + save_file
    os.system(final_command)
    with open('devices.txt') as f:
        lines = f.readlines()
    # print(lines)
    printers_list = filter_printers(devices_lines=lines)
    return printers_list


# trial to load all cups installed drivers
def printx_load_printers():
    _printer_list = []
    _jobs_list = []
    # services = ['1. Load all cups installed printers.']
    # print('Please Choose service?')
    # for s in services:
    #     print(s)
    # service_selected = input('Choose service number.\n')
    try:
        # service_number = int(service_selected)
        # print('Service selected ==> ' + service_selected)
        # if service_number == 1:
        _printer_list = load_all_printers()

    except Exception as e:
        print(str(e))

    return _printer_list

# printx_load_printers()
