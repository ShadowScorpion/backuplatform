#!/usr/bin/python
import sys
import argparse
import yaml
from logginsys import LogginSystem as loggin_system
from os import listdir
from os.path import isfile, join

class enable_modules(object):
    def __init__(self, main_conf_data):
        self.conf_data = main_conf_data
        self.mainconf_list = ["logs", "server_id", "include", "log_level"]

    def main_conf(self):
        self.enable_modules, self.disabled_options=self.define_options_main_configuration()
        logs, log_level, server_id, include = self.check_valid_main_conf(self.enable_modules, self.disabled_options, self.conf_data)
        return logs, log_level, server_id, include

    def define_options_main_configuration(self):
        enabled_options = (list(set(self.mainconf_list) & set(self.conf_data['agent'])))
        unknown_options = set(self.conf_data['agent']) - set(self.mainconf_list)
        disabled_options = set(self.mainconf_list) - set(enabled_options)

        if not unknown_options:
            pass
        else:
            print("Unknown options. Please check : ")
            for option in unknown_options:
                    print("Error in line => "+option)
            sys.exit(1)

        for option in disabled_options:
            if str(option) == "server_id":
                print("server_id not setted. Please check configuration")
                sys.exit(1)
        return(enabled_options,disabled_options)

    def check_valid_main_conf(self, enabled_modules, disabled_modules, conf_data):

        for option in enabled_modules:
            if str(option) == "logs":
                logs = conf_data['agent']['logs']
            elif str(option) == "log_level":
                log_level = conf_data['agent']['log_level']
            elif str(option) == "server_id":
                server_id = conf_data['agent']['server_id']
            elif str(option) == "include":
                include = conf_data['agent']['include']

        for option in disabled_modules:
            if str(option) == "logs":
                logs = '/var/log/backuplatform/'
            elif str(option) == "log_level":
                log_level = 'WARN'
            elif str(option) == "include":
                include = '/etc/backuplatorm/conf.d/'

        return logs, log_level, server_id, include

    def define_inventory(self, include_folder):
        inventory_files = [f for f in listdir(include_folder) if isfile(join(include_folder, f))]
        for inventory_file in inventory_files:
            try:
                inventory_yaml = yaml.safe_load(open(include_folder+"/"+inventory_file))
                print(inventory_yaml)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reading of arguments of backupplatform agent')
    parser.add_argument('-c', dest='config_file', default='/etc/backuplatform/backuplatform.conf')
    args = parser.parse_args()

    try :
        f = open(args.config_file)
    except:
        print("Missing configuration file")
        sys.exit(1)

    try :
        dataMap = yaml.safe_load(f)
        class_modules = enable_modules(dataMap)
        option_logs, option_log_level, option_server_id, option_include = class_modules.main_conf()
        log_system = loggin_system(option_logs, option_log_level)
        log_system.running_agent(args.config_file)
        class_modules.define_inventory(option_include)

    except Exception as e:
        print("Problems with configuration file")
        print("Problems in line : %s" % e)
        sys.exit(1)
    f.close()