import re
from enum import Enum, auto

class Level(Enum):
    CRITICAL = auto()
    ERROR = auto()
    WARNING = auto()
    INFO = auto()
    DEBUG = auto()
    UNDEFINED = auto()


class LogLine:
    def __init__(self, level, message, timestamp="", logger_name="", sub_name=""):
        self.level = level
        self.message = message
        self.timestamp = timestamp
        self.logger_name = logger_name
        self.sub_name = sub_name
    def __str__(self):
        return self.message


# class Parser:
#     pattern = ""

#     def __init__(self):
#         self.regex = "regex compilada con " + self.pattern

#     def parse_line(self, line):
#         pass
        
#     def get_level(self, level_string):
#         raise NotImplementedError()


class GlassfishFormatter:
    pattern = r"^\[(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}[\-\+]\d{4})\] \[.+\] \[(?P<alert_level>.+)\] \[.*\] \[(?P<component>[a-zA-Z.]*)\] \[[a-zA-Z._\s=\-:()0-9]*\] \[.*\] \[\[(?P<body>[\s\S]*)\]\]$"
    regex = re.compile(pattern)

    def parse(self, file_object):
        res = []
        line = ""
        for l in file_object:
            line += l
            if l.strip().endswith("]]"):
                res.append(self.parse_line(line.strip()))
                line = ""
        return res

    def parse_line(self, line):
        if "[INFORMACIÓN]" in line or "[INFO]" in line:
            level = Level.INFO
        elif "[ADVERTENCIA]" in line or "[WARNING]" in line:
            level = Level.WARNING
        elif "[GRAVE]" in line or "[SEVERE]" in line:
            level = Level.ERROR
        else:
            level = Level.DEBUG
        return LogLine(level, line)
    
    def parse_line_regex(self, line):
        m = regex.match(data)
        if m:
            print(m.group("alert_level"))
        else:
            return LogLine()
    
    def fallback_parse(self, line):
        pass