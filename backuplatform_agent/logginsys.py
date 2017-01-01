import os, sys
import datetime

class LogginSystem(object):

    def __init__(self, logs_folder, global_log_level):
        log_file_path = logs_folder+"backuplatform.log"
        exist_folder = os.path.isdir(logs_folder)
        exist_file = os.path.exists(log_file_path)
        self.global_log_level = global_log_level
        if exist_folder == False:
            print("No folder for logs. Trying to create it")
            try:
                os.makedirs(logs_folder)
                print("Folder %s was created" % logs_folder)
            except:
                print("Problem with access to logs folder please check")
        self.log_file = log_file_path
        if exist_file == False:
            try:
                with open(log_file_path, 'w') as log_file:
                    log_file.write("%s [INFO] New logs file for backuplatform agent was created.\n" % str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
            except:
                print("Problem with access to log file %s" % self.log_file)
                sys.exit(1)

    def running_agent(self, configuration_file):
        with open(self.log_file, 'a') as log_file_temp:
            log_file_temp.write("%s [INFO] Starting backuplatform agent \n" % str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
            log_file_temp.write("%s [INFO] Main configuration file is %s \n" % (str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), configuration_file))
            log_file_temp.write("%s [INFO] Start reading inventofies configuration files \n" % str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))

#    def write_log(self, message, log_level_message):
#        with open(self.log_file, 'a') as log_file:
