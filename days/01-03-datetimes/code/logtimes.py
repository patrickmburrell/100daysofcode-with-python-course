import os
import urllib.request
from datetime import datetime, timedelta

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, "log")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/messages.log", logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:


def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    datetime_segment = line.split(" ")[1]
    dt = datetime.strptime(datetime_segment, "%Y-%m-%dT%H:%M:%S")
    return dt


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_loglines = [line for line in loglines if "Shutdown initiated" in line]

    first_datetime = convert_to_datetime(shutdown_loglines[0])
    last_datetime = convert_to_datetime(shutdown_loglines[-1])

    delta = last_datetime - first_datetime
    return delta


time_diff = time_between_shutdowns(loglines)
print(f"The time difference is: {time_diff}")
