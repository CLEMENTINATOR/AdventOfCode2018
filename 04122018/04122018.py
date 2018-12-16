from datetime import datetime
from datetime import timedelta
import parse
from enum import Enum
from collections import defaultdict

class RecordType(Enum):
    WAKEUP = 1
    ASLEEP = 2

class Record(object):
    time_format = "[%Y-%m-%d %H:%M]"
    guard_format = parse.compile("Guard #{id} begins shift")

    def __init__(self, record_str):
        r_date = record_str[:record_str.index("]") + 1]
        r_event = record_str[record_str.index("]") + 2:]

        self.date = datetime.strptime(r_date, Record.time_format)
        self.event = r_event

    def __str__(self):
        return datetime.strftime(self.date, Record.time_format) + " " + self.event

    def get_guard_id(self):
        gid = None
        if "Guard" in self.event:
            r = Record.guard_format.parse(self.event)
            gid = int(r["id"])

        return gid

    def get_event_type(self):
        if "Guard" in self.event or "wakes up" in self.event:
            return RecordType.WAKEUP
        if "falls asleep" in self.event:
            return RecordType.ASLEEP

    def get_time(self):
        corrected_time = self.date
        # round to midnight next day if needed
        if corrected_time.hour == 23:
            corrected_time = corrected_time.replace(hour = 0, minute = 0)
            corrected_time += timedelta(days=1)
        return corrected_time

class Chronogram(object):
    def __init__(self, records):
        guard_id = None
        wakeup_time = None
        asleep_time = None
        self.guards_asleep_time = defaultdict(int)
        self.guards_mins_asleep = defaultdict(int)

        for r in records:
            if r.get_guard_id():
                # new day, process last day
                if asleep_time:
                    asleep_minutes = 60 - asleep_time.minute
                    self.guards_asleep_time[guard_id] += asleep_minutes
                    for i in range(asleep_time.minute, 60):
                        self.guards_mins_asleep[guard_id][i] += 1
                # reset variables
                wakeup_time = r.get_time().replace(hour = 0, minute = 0)
                asleep_time = None
                guard_id = r.get_guard_id()
                if not self.guards_mins_asleep[guard_id]:
                    self.guards_mins_asleep[guard_id] = defaultdict(int)
                continue


            evt_time = r.get_time()
            evt_type = r.get_event_type()

            if evt_type == RecordType.WAKEUP:
                wakeup_time = evt_time
                if asleep_time:
                    asleep_minutes = (wakeup_time - asleep_time).seconds / 60
                    self.guards_asleep_time[guard_id] += asleep_minutes
                    for i in range(asleep_time.minute, wakeup_time.minute):
                        self.guards_mins_asleep[guard_id][i] += 1

                    asleep_time = None
            if evt_type == RecordType.ASLEEP:
                asleep_time = evt_time

    def strategy1(self):
        most_asleep_guard = max(self.guards_asleep_time, key=lambda k: self.guards_asleep_time[k])
        most_min_asleep = max(self.guards_mins_asleep[most_asleep_guard], key=lambda k: self.guards_mins_asleep[most_asleep_guard][k])
        print("strategy 1 : {}".format( most_asleep_guard * most_min_asleep))

def main():
    records = []
    with open("input", "r") as f:
        records_str = f.read().split("\n")

    for r in records_str:
        records.append(Record(r))

    records.sort(key=lambda record: record.date)

    chrono = Chronogram(records)
    chrono.strategy1()

if __name__ == "__main__":
    main()