from time import sleep

import requests
from lxml import html
# import CSV
import datetime


url = 'https://m.csun.edu/default/find_parking/index'
spacesAvailable = {"B3": None, "B5": None, "G3": None}
spacesTaken = {"B3": None, "B5": None, "G3": None}


def main():
    # year, month, day, hour, minute, second
    # waitUntilTime(2018, 10, 17, 14, 0, 0)

    startAt = datetime.datetime(2018,10,31,12,23,0,0)
    waitUntilTime2(startAt)
    for i in range(4):
        getLotNumberCount()
        print(spacesTaken)
        futureTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
        waitUntilTime2(futureTime)
        #Write to CSV

    # WORKING ON FIXING THE DAMN PROBLEM WITH THE TIME ROUNDUP TINHG FUCK

    # for i in range(4):
    #     getLotNumberCount()
    #     CSV.writeRow(spacesAvailable['B3'], spacesAvailable['B5'], spacesAvailable['G3'])
    #     print("Written to " + CSV.filename + " B3: " + str(spacesAvailable['B3']) + " B5: " + str(spacesAvailable['B5']) + " G3: " + str(spacesAvailable['G3']))
    #     sleep(60 * 30)


def getLotNumberCount():
    B3max = 2063
    B5max = 1361
    G3max = 979
    response = requests.get(url)
    page = html.fromstring(response.content)

    # Gets HTML value for the spaces
    B3 = page.xpath('//*[@id="kgoui_Rcontent_I0_Ritems_I0_Fcolumn1"]/a/div/div/span/text()')
    B5 = page.xpath('//*[@id="kgoui_Rcontent_I0_Ritems_I1_Fcolumn1"]/a/div/div/span/text()')
    G3 = page.xpath('//*[@id="kgoui_Rcontent_I0_Ritems_I2_Fcolumn1"]/a/div/div/span/text()')

    # SPACES AVAILABLE - Puts spaces available into dictionary and if they are full converts them
    if str(B3[0]).lower() == "full":
        spacesAvailable["B3"] = 0
    else:
        spacesAvailable["B3"] = B3[0]

    if str(B5[0]).lower() == "full":
        spacesAvailable["B5"] = 0
    else:
        spacesAvailable["B5"] = B5[0]

    if str(G3[0]).lower() == "full":
        spacesAvailable["G3"] = 0
    else:
        spacesAvailable["G3"] = G3[0]

    # SPACES TAKEN - Puts spaces taken into dictionary and if they are full converts them
    if str(B3[0]).lower() == "full":
        spacesTaken["B3"] = B3max
    else:
        spacesTaken["B3"] = B3max - int(B3[0])

    if str(B5[0]).lower() == "full":
        spacesTaken["B5"] = B5max
    else:
        spacesTaken["B5"] = B5max - int(B5[0])

    if str(G3[0]).lower() == "full":
        spacesTaken["G3"] = G3max
    else:
        spacesTaken["G3"] = G3max - int(G3[0])

#Will wait until inputted datetime from current time
def waitUntilTime2(dt):
    now = datetime.datetime.now()
    now = convertTime(now)
    print("Current Date/Time: " + str(now))

    dt = convertTime(dt)
    print("Future  Date/Time: " + str(dt))

    print("Waiting until " + str(dt))
    while(now != dt):
        now = datetime.datetime.now()
        now = convertTime(now)
        sleep(1/100)

    print("Finished waiting..." + "\n")



def waitUntilTime(year, month, day, hour, minute, second):
    # Gets current time and future time
    now = datetime.datetime.now()
    timeThen = datetime.datetime(year, month, day, hour, minute, second, 0)

    # Formats time into readable format
    nowFormatted = now.strftime('%B %d %Y %H:%M:%S')
    timeThenFormatted = timeThen.strftime('%B %d %Y %H:%M:%S')

    print("Now Waiting Until: " + timeThenFormatted + "...")
    while (nowFormatted != timeThenFormatted):
        nowFormatted = datetime.datetime.now().strftime('%B %d %Y %H:%M:%S')
        print(nowFormatted)  # Can Remove
        sleep(1)
    print("Wait Finished")


def convertTime(inputtedDateTime):
    #converts time to simple time
    #it removes seconds and microseconds

    dt = inputtedDateTime
    newNow = (dt - datetime.timedelta(microseconds=dt.microsecond) - datetime.timedelta(seconds=dt.second))
    return newNow

if __name__ == "__main__":
    main()
