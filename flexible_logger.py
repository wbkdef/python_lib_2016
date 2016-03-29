import os
import datetime
from glob import glob
import traceback

import easygui
import textwrap

def get_now_str():
    now = datetime.datetime.now()
    time = "{:%H:%M:%S:%f}".format(now)[:-3]
    return time


class Logger:
    def __init__(self,
                 logging_directory=r'C:\Users\Willem\Desktop\organization\Autohotkey\file_communication',
                 logging_filename_base = "flex_log",
                 default_priority = 3,
                 print_priority = 5,
                 msgbox_priority = 1
                 ):
        self.logging_directory = logging_directory
        self.logging_filename_base = logging_filename_base
        self.default_priority = default_priority

        self.print_priority = print_priority
        self.msgbox_priority = msgbox_priority

        self.log_num = 0

        self.clear_log_files()

    ALL_PRIORITIES = range(6)

    def get_logging_path(self, priority):
        return os.path.join(self.logging_directory, self.logging_filename_base+str(priority) + ".txt")

    def clear_log_files(self):
        to_glob = self.get_logging_path(1)[:-5] + "*"
        for f in glob(to_glob):
            os.remove(f)

    def log_to_file(self, priority, s):
        path = self.get_logging_path(priority)
        try:
            with open(path, 'a') as f:
                f.write(s)
        except Exception as e:  # __c
            easygui.msgbox(
                "logging to file failed with path " + path + "\n\n %s " % e)

    def get_file_log_str(self, priority, s, priority_of_log_file=None):
        if priority_of_log_file is None:
            priority_of_log_file = priority
        full_stack = traceback.extract_stack()


        # if priority_of_log_file < 5:
            # easygui.msgbox(stack_info)
        file_info = [si for si in full_stack if 'flexible_logger' not in si.filename][-2]
        stack_info = os.path.split(file_info.filename)[1] + " line %s" % file_info.lineno
        if priority_of_log_file >= 3:
            stack_info += " - " + file_info.filename
        if priority_of_log_file >= 5:
            stack_info += " - " + str(full_stack)
        metta_data = "\n%s. Python-%s " % (self.log_num, priority) + get_now_str() + ' %s: \n' % stack_info
        indented_str = textwrap.indent(s, "    ")
        return metta_data + indented_str

    def log_to_files(self, priority, s):
        for i in self.ALL_PRIORITIES[priority:]:
            self.log_to_file(i, self.get_file_log_str(priority, s, i))

    def log_to_print(self, priority, s):
        print(self.get_file_log_str(priority, s))

    def log_to_msgbox(self, priority, s):
        easygui.msgbox(self.get_logging_path(priority) + "\n\n" + self.get_file_log_str(priority, s))

    def log(self, s, priority=None):
        self.log_num += 1
        if priority is None:
            priority = self.default_priority
        if priority <= self.print_priority:
            self.log_to_print(priority, s)
        self.log_to_files(priority, s)
        if priority <= self.msgbox_priority:
            self.log_to_msgbox(priority, s)


logger = Logger()

def log(s, priority=None):
    logger.log(s, priority)

# logging_filename = r'C:\Users\Willem\Desktop\organization\Autohotkey\file_communication\flex_log.txt'
#
#
# def log(s, priority=None):
#     if priority is None:
#         priority = default_priority
#     if priority <= print_priority:
#         print(s)
#     if logging_filename is not None and priority <= log_to_file_priority:
#         try:
#             with open(logging_filename, 'a') as f:
#                 f.write("\nPython-" + get_now_str() + ': ' + s)
#         except Exception as e:  # __c
#             easygui.msgbox(
#                 "logging to file failed with logging_filename " + logging_filename + "\n\n %s " % e)
#     if priority <= msgbox_priority:
#         easygui.msgbox('log: ' + s)

