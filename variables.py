MORNING_TIME = [
    ("8:30", "10:05"),
    ("10:25", "12:00")
]
SUMMER_TIME = MORNING_TIME+[
    ("14:30", "16:05"),
    ("16:25", "18:00"),
    ("19:30", "21:05"),
]
WINTER_TIME = MORNING_TIME+[
    ("14:00", "15:35"),
    ("15:55", "17:30"),
    ("19:00", "20:35"),
]
SEMSTART = (2019, 2, 25)

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate"
}

REGEX_HIDDEN_TAG = '<input type="hidden" name="(.*)" value="(.*)"'
REGEX_HTML_COMMENT = r'<!--\s*([\s\S]*?)\s*-->'
