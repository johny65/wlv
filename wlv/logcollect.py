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


class GlassfishParser:
    pattern = r"^\[(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}[\-\+]\d{4})\] \[.+\] \[(?P<alert_level>.+)\] \[.*\] \[(?P<component>[a-zA-Z.]*)\] \[[a-zA-Z._\s=\-:()0-9]*\] \[.*\] \[\[(?P<body>[\s\S]*)\]\]$"
    regex = re.compile(pattern)
    level_mapping = {
        "INFORMACIÓN": Level.INFO,
        "INFO": Level.INFO,
        "ADVERTENCIA": Level.WARNING,
        "WARNING": Level.WARNING,
        "GRAVE": Level.ERROR,
        "SEVERE": Level.ERROR
    }

    def parse(self, file_object):
        res = []
        line = ""
        for l in file_object:
            line += l
            if l.strip().endswith("]]"):
                res.append(self._parse_line(line.strip()))
                line = ""
        return res

    def _parse_line(self, line):
        m = self.regex.match(line)
        if m:
            timestamp = self._get_group(m, "timestamp")
            body = self._get_group(m, "body")
            component = self._get_group(m, "component")
            level_string = self._get_group(m, "alert_level")
            if level_string is None:
                level = Level.UNDEFINED
            else:
                level = self.level_mapping.get(level_string)
                level = level if level else Level.DEBUG
            return LogLine(level, body, timestamp, component)
        else:
            return self._fallback_parse(line)
    
    def _get_group(self, match, group_name):
        try:
            return match.group(group_name)
        except IndexError:
            return None

    def _fallback_parse(self, line):
        if "[INFORMACIÓN]" in line or "[INFO]" in line:
            level = Level.INFO
        elif "[ADVERTENCIA]" in line or "[WARNING]" in line:
            level = Level.WARNING
        elif "[GRAVE]" in line or "[SEVERE]" in line:
            level = Level.ERROR
        else:
            level = Level.UNDEFINED
        return LogLine(level, line)
