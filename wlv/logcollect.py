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