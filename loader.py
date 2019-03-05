import json
from icalendar import Calendar, Event
from datetime import timedelta, datetime
import variables

def load(uuid):
    f = open('./data/'+uuid)
    courseList = json.loads(f.read())
    f.close()
    cal = Calendar()
    for week_cnt in range(len(courseList)):
        for day_cnt in range(len(courseList[week_cnt])):
            for course in courseList[week_cnt][day_cnt]:
                e = Event()
                if course['name'] == None:
                    course['name'] = 'none'
                if course['location'] == None:
                    course['location'] = 'none'
                e.add(
                    "description",
                    '课程名称：'+course['name'] +
                    ';上课地点：'+course['location']
                )
                e.add('summary', course['name']+'@'+course['location'])
                semstart=variables.SEMSTART
                date = datetime(semstart[0], semstart[1], semstart[2]) + \
                    timedelta(days=week_cnt*7+day_cnt)  # 从第一 周的第一天起
                (beginTime, endTime) = \
                    variables.SUMMER_TIME[int(course['sectionSpan'][1]/2-1)] if\
                    date.month >= 5 and date.month < 10 else \
                    variables.WINTER_TIME[int(course['sectionSpan'][1]/2-1)]
                (beginTime, endTime) = (beginTime.split(':'), endTime.split(':'))

                e.add(
                    "dtstart",
                    date.replace(
                        hour=int(beginTime[0]),
                        minute=int(beginTime[1])
                    )
                )
                e.add(
                    "dtend",
                    date.replace(
                        hour=int(endTime[0]),
                        minute=int(endTime[1])
                    )
                )
                cal.add_component(e)
    return cal.to_ical().decode('utf-8')
