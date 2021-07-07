import os
from os import listdir

def mainMenu():
    print("""
    ███████                        █████                       █████       ███                    █████████             █████        ███████████                                                                   
  ███░░░░░███                     ░░███                       ░░███       ░░░                    ███░░░░░███           ░░███        ░░███░░░░░███                                                                  
 ███     ░░███ ████████   ██████   ░███ █████  ██████   █████  ░███████   ████                  ░███    ░░░  █████ ████ ░███████     ░███    ░███   ██████  ████████    ██████   █████████████    ██████  ████████ 
░███      ░███░░███░░███ ░░░░░███  ░███░░███  ███░░███ ███░░   ░███░░███ ░░███     ██████████   ░░█████████ ░░███ ░███  ░███░░███    ░██████████   ███░░███░░███░░███  ░░░░░███ ░░███░░███░░███  ███░░███░░███░░███
░███      ░███ ░███ ░░░   ███████  ░██████░  ░███████ ░░█████  ░███ ░███  ░███    ░░░░░░░░░░     ░░░░░░░░███ ░███ ░███  ░███ ░███    ░███░░░░░███ ░███████  ░███ ░███   ███████  ░███ ░███ ░███ ░███████  ░███ ░░░ 
░░███     ███  ░███      ███░░███  ░███░░███ ░███░░░   ░░░░███ ░███ ░███  ░███                   ███    ░███ ░███ ░███  ░███ ░███    ░███    ░███ ░███░░░   ░███ ░███  ███░░███  ░███ ░███ ░███ ░███░░░   ░███     
 ░░░███████░   █████    ░░████████ ████ █████░░██████  ██████  ████ █████ █████                 ░░█████████  ░░████████ ████████     █████   █████░░██████  ████ █████░░████████ █████░███ █████░░██████  █████    
   ░░░░░░░    ░░░░░      ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░░  ░░░░ ░░░░░ ░░░░░                   ░░░░░░░░░    ░░░░░░░░ ░░░░░░░░     ░░░░░   ░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░░     
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   """)
    print("Please enter file location of videos & subs:")
    mainMenu.location = input()
    mainMenu.arrayOfFiles = os.listdir(mainMenu.location)
    checkFolder()

def checkFolder():
    checkFolder.mkvArray = []
    checkFolder.srtArray = []
    for item in mainMenu.arrayOfFiles:
        if str(item).endswith((".mkv",".mp4",".mov")):
            checkFolder.vidExtension = item[-4:]
            checkFolder.mkvArray.append(item)

        elif str(item).endswith((".srt", ".ass")):
            checkFolder.subExtension = item[-4:]
            checkFolder.srtArray.append(item)

    #checkLists()
    changeSubNamesUpdate()

def checkLists():
    for i in range(len(checkFolder.mkvArray)):
        print(checkFolder.mkvArray[i])

    for i in range(len(checkFolder.srtArray)):
        print(checkFolder.srtArray[i])


def changeSubNamesUpdate():
    counter = 0
    seasonNum = 1
    epSearch = "S0"+str(seasonNum)+"E"
    epNum = 1
    epNumFormat = "0"
    
    while epNum < len(checkFolder.mkvArray):

        for file in checkFolder.mkvArray:
            if(epNum < 10):
                epSearch = epSearch + epNumFormat+str(epNum)

            elif(epNum >=10):
                epSearch = epSearch+str(epNum)

            if(epSearch in file):
                for i in range(len(checkFolder.srtArray)):
                    if(epSearch in checkFolder.srtArray[i]):
                        os.rename(mainMenu.location+"/"+checkFolder.srtArray[i],mainMenu.location+"/"+file.replace(checkFolder.vidExtension, checkFolder.subExtension))
                        epNum = epNum+1
                        epSearch = "S0"+str(seasonNum)+"E"
                        i=0
                        break
                    elif (epSearch not in checkFolder.srtArray[i] and i<len(checkFolder.srtArray)):
                        i+=1
                        continue    
                    else:
                        epNum = epNum+1
                        epSearch = "S0"+str(seasonNum)+"E"
                        break
                

            else:
                seasonNum = seasonNum+1
                epSearch = "S0"+str(seasonNum)+"E"
                break
    print("Complete :)")
    mainMenu()
mainMenu()