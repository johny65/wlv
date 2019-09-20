class LogLine:
    level = ""
    message = ""
    def __init__(self, level, message):
        self.level = level
        self.message = message
    def __str__(self):
        return self.message

class GlassfishFormatter:
    def parse(self, file_object):
        res = []
        line = ""
        for l in file_object:
            line += l
            # print("termina con:", l[-1:-5])
            print(l)
            print("entra?:", l.strip().endswith("]]"))
            if l.strip().endswith("]]"):
                res.append(self.parse_line(line))
                line = ""
        print("size:", len(res))
        return res
#         for line in f:
#             if same and line.endswith(END):

    def parse_line(self, line):
        if "[MUY DETALLADO]" in line or "[FINER]" in line:
            level = "finer"
        elif "[ADVERTENCIA]" in line or "[WARNING]" in line:
            level = "warn"
        elif "[GRAVE]" in line or "[SEVERE]" in line:
            level = "err"
        else:
            level = "info"
        return LogLine(level, line)

# START = "["
# END = "]]"

# def process(filepath):
#     with open(filepath) as f:
#         same = False
#         for line in f:
#             if same and line.endswith(END):



# """

# ^\[(?<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}[\-\+]\d{4})\] \[.+\] \[(?<alert_level>.+)\] \[.*\] \[(?<component>[a-zA-Z.]*)\] \[[a-zA-Z._\s=\-:()0-9]*\] \[.*\] \[\[(?<body>[\s\S]*)\]\]$
# """