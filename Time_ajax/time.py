from datetime import datetime
import pytz
import cgi, cgitb
import json

now = datetime.now()  # UTC 0시간 기준 London, Lisbon, Portugal, Iceland
worldtime = str(now)
print(worldtime)