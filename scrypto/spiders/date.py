from datetime import datetime
import sys

dates = ['9:20AM - 20 dec 2017','11:55PM - 12 jan 2018','8:09AM - 8 mar 2018', '11:55AM - 12 jan 2018', '8:20PM - 5 nov 2016', '6:08AM - 22 feb 2014']
def parseTime(argv):
    timemap = list()
    sorted_timemap = list()
    for hours in argv:
        time, date = hours.strip().split(" - ")
        time = time.replace(" ", "")
        datetuple = f'{time} {date}'
        datetimes = datetime.strptime(datetuple, '%I:%M%p %d %b %Y')
        timemap.append(datetimes)
        sorted_timemap = list(timemap)
        sorted_timemap.sort(reverse=True)
        #print(f'timemap is : {timemap} !!!!!!!!\n')
    return sorted_timemap, timemap

if __name__ == "__main__":
   print(parseTime(dates))

