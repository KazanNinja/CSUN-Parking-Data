import csv
import datetime

filename = "Log_" + str(datetime.datetime.now()).replace(':', '_') + ".csv"
print("Created " + filename)

with open(filename, 'w') as f:
    fieldnames = ['Current Date', 'Current Day', 'B3', 'B5', 'G3']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    f.close()


def writeRow(b3, b5, g3):
    with open(filename, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        dt_now = datetime.datetime.now()
        currentDayName = dt_now.strftime('%A')
        currentDate = (dt_now.strftime('%B %d %Y %H:%M'))
        writer.writerow({'Current Date': currentDate,  'Current Day': currentDayName, 'B3': b3, 'B5': b5, 'G3': g3})
        f.close()

