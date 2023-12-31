from pandas.io.parsers import read_csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, parse_qs
import time

# NOTE: this scrapper is built only for opensider.com
"""
How this scrapper works:
A scrapper is a tool that can be used to "scrape a website" or take the html of a website and 
along with that, any data that can be attained.

For example On openinsider.com, all of the data regarding the insider trading is in a table 
and if we can parse that table using a library using beauitful soup,
we can then extract that data.

This scrapper have 3 portions:
1: scrap the data from openinsider.com
2: generate a pandas dataframe to hold the scrapped data 
   and more data columns for stock price after the stock was brought.
3: Send that scrapped data to the DataGetter class that have the stock data
   APIs to populate the stock data. 
"""


class DailyScrapper():

    def __init__(self, url: str) -> None:
        """This function starts the scrapping process and sets the default data

        Args:
            url (str): url of the open insider website with the filters.
            csvFilePath (str): the filepath that the data is stored, inside the /data folder
            description (str): a small description for the url, such as "CEO purchases from 2011 to 2022"
        """
        print("Scrapping Openinsider.com... please wait a few seconds")
        self.url = url
        self.count = 0
        self.changeTickerCount = 0
        self.removecount = 0
        # if the site is scrapped already, no need to waste time doing it again
        if self.isCluster(url):
            print(
                "detected that this is a cluster query, scrapping could take up to a minute"
            )
            insiderData = {
                'idx': [],
                "Option": [],
                'Filing_Date': [],
                'Trade_Date': [],
                'Ticker': [],
                'Company_Name': [],
                'Industry': [],
                'Insider_Amount': [],
                'Trade_Type': [],
                'Price': [],
                'Qty': [],
                'Owned': [],
                'ΔOwn': [],
                'Value': []
            }
            insiderData = self.turnGroupedDataIntoDict(insiderData, url)
        # insider data contains all the major fields, this will be converted into dataframe and eventurally csv
        # takes the html data of requests and puts it into insider data
        else:
            insiderData = {
                'idx': [],
                "Option": [],
                'Filing_Date': [],
                'Trade_Date': [],
                'Ticker': [],
                'Company_Name': [],
                'Insider_Name': [],
                'Title': [],
                'Trade_Type': [],
                'Price': [],
                'Qty': [],
                'Owned': [],
                'ΔOwn': [],
                'Value': []
            }
            insiderData = self.turnDataintodict(insiderData, url)

        t = TimeFrame()
        self.timeframe = t.timeframe
        self.timeframepercent = t.timeframepecent
        # takes the dict and turn it into data frame
        self.data = pd.DataFrame(data=insiderData)
        # keeps track of original size
        self.originalSize = len(self.data)
        # this is added so stocks after the time period can be filled in.
        self.data[self.timeframe] = 0.0
        # this is change in % since brought
        self.data[self.timeframepercent] = 0.0
        # see if the data is still active today
        self.data["active"] = False
        # done is a variable used to check if the 2w,1m... data has been filled in,
        # in case the program was stopped half way
        self.data["done"] = False
        # this is used to filter out entries that have no good data about then, 
        # such as trading before IPO or if stock no longer exist
        self.data["skip"] = False
        # the API source that this data is gotten from
        self.data["source"] = ""
        # filters out all the entries with no ticker
        self.data = self.data[self.data["Ticker"] != ""]
        self.data = self.data[self.data["Ticker"] != ".."]
        self.data = self.data[self.data["Ticker"] != "Na"]
        self.data = self.data.sort_values("Trade_Date", ascending=False)
        # remove adjcent duplicate tickers
        print(f"Done scrapping, found: {self.size()} entries")
        self.data = self.data.loc[
            self.data['Ticker'] != self.data['Ticker'].shift()]
        self.data = self.data.sort_values("Filing_Date", ascending=False)
        print(
            f"Removed adjcent tickers because same stock brought same day shouldnt be counted, total size is now {self.size()}"
        )
        time.sleep(1)
        self.to_csv()
        # adding the data to scrapped so that it will show up in the main menu
        self.addToScrapped()
        # after scrapping data, fill in the stock price after timeframe(2m,1m,2m ...etc)

        return self.data
    
    
    def size(self):
        return len(self.data)

    def turnDataintodict(self, insiderData: dict, url: str) -> dict:
        """This is the scrapping part where the url is scrapped and insiderData is populated 

        Args:
            insiderData (dict): dictionary of the columns for the insider data such as name,ticker, etc
            url (str): the Url to scrape from

        Returns:
            dict: _description_
        """
        # TODO: add validation to make sure that the url is a openinsider url
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, "lxml")
        body = soup.find_all("tbody")[1]
        rows = body.find_all("tr")
        # parsing table data from open insider
        for items in rows:
            self.count += 1
            column = items.find_all("td")
            insiderData["idx"].append(self.count)

            Option = column[0].get_text()
            insiderData["Option"].append(self.isOptionsTrade(Option))

            Filing_Date = self.getChildData(column[1], "div a").split(" ")[0]
            insiderData["Filing_Date"].append(Filing_Date)

            Trade_Date = self.getChildData(column[2], "div")
            insiderData["Trade_Date"].append(Trade_Date)

            Ticker = self.getChildData(column[3], "b a")
            insiderData['Ticker'].append(Ticker)

            Company_Name = self.getChildData(column[4], "a").split("/")[0]
            insiderData['Company_Name'].append(Company_Name)

            Insider_Name = self.getChildData(column[5], "a")
            insiderData['Insider_Name'].append(Insider_Name)

            Title = column[6].get_text()
            insiderData['Title'].append(Title)

            Trade_Type = column[7].get_text()
            insiderData['Trade_Type'].append(Trade_Type)

            insiderData['Price'].append(0.0)

            Qty = self.toFloat(column[9].get_text())
            insiderData['Qty'].append(Qty)

            Owned = self.toFloat(column[10].get_text())
            insiderData['Owned'].append(Owned)

            OwnChange = self.toFloat(column[11].get_text())
            insiderData['ΔOwn'].append(OwnChange)

            Value = self.toFloat(column[12].get_text())
            insiderData['Value'].append(Value)

        # if the number if rows is 1000, then there might be more data on the next page, so we go to the next page
        if (len(rows) == 1000):
            # pagenumber is found at the end of the url
            page = int(url[-2:].replace("=", ""))
            # 9 is the page limit or 9000 entries
            if (page >= 10):
                return insiderData
            url = url.split("page=")[0] + "page=" + str(page + 1)
            print("currently scanning page:", page, "entries gotten so far:",
                  (page) * 1000)
            # recursively scrape until all the pages are done
            insiderData = self.turnDataintodict(insiderData, url)
        return insiderData

    # D means "derivative" aka options trade
    def isOptionsTrade(self, type) -> bool:
        return "D" in type

    # same function as turnDataintodict, but it deals with cluster instead of indivisual
    def turnGroupedDataIntoDict(self, insiderData, url) -> dict:
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, "lxml")
        body = soup.find_all("tbody")[1]
        rows = body.find_all("tr")
        # parsing table data from open insider
        for items in rows:
            column = items.find_all("td")
            self.count += 1
            insiderData["idx"].append(self.count)

            Option = column[0].get_text()
            insiderData["Option"].append(self.isOptionsTrade(Option))

            Filing_Date = self.getChildData(column[1], "div a").split(" ")[0]
            insiderData["Filing_Date"].append(Filing_Date)

            Trade_Date = self.getChildData(column[2], "div")
            insiderData["Trade_Date"].append(Trade_Date)

            Ticker = self.getChildData(column[3], "b a")
            insiderData['Ticker'].append(Ticker)

            Company_Name = self.getChildData(column[4], "a").split("/")[0]
            insiderData['Company_Name'].append(Company_Name)

            Industry = self.getChildData(column[5], "a")
            insiderData['Industry'].append(Industry)

            Insider_Amount = float(column[6].get_text())
            insiderData['Insider_Amount'].append(Insider_Amount)

            Trade_Type = column[7].get_text()
            insiderData['Trade_Type'].append(Trade_Type)

            # If I cannot find the price on this stock at trade date adjusted for splits and everything,
            # its not going into the final result
            # Price =self.toFloat(column[8].get_text())
            insiderData['Price'].append(0.0)

            Qty = self.toFloat(column[9].get_text())
            insiderData['Qty'].append(Qty)

            Owned = self.toFloat(column[10].get_text())
            insiderData['Owned'].append(Owned)

            ownChange = self.toFloat(column[11].get_text())
            insiderData['ΔOwn'].append(ownChange)

            Value = self.toFloat(column[12].get_text())
            insiderData['Value'].append(Value)
        # if the number if rows is 1000, then there might be more data on the next page, so we go to the next page
        if(len(rows)==1000):
            #page number is found at the end of the url
            page = int(url[-2:].replace("=","")) 
            #9 is the page limit or 9000 entries
            if(page>=10):
                return insiderData
            url = url.split("page=")[0] + "page=" + str(page+1)
            print("currently scanning page:",page, "entries gotten so far:",(page)*1000)
            #recursion until all the pages are done
            insiderData = self.turnGroupedDataIntoDict(insiderData,url)
        return insiderData

    # this function checks if the url given is for grouped or cluster trading  rather than indivisual trading
    def isCluster(self, url) -> bool:
        o = urlparse(url)
        query = parse_qs(o.query)
        return query["grp"][0] == "2"

    def __repr__(self):
        return "-------------------------------------------------------\nDESCRIPTION: " + self.description + "\n found: " + str(
            len(self.data)
        ) + " entries" + "\n Located at:" + self.csvFilePath + "\n-------------------------------------------------"

    def getData(self) -> pd.DataFrame:
        self.data = read_csv(self.csvFilePath)
        return self.data

    # Make sure the same data isnt scrapped again, which takes a while
    def alreadyscrapped(self, description) -> bool:
        f = open("alreadyscrapped.json")
        scrapped = json.load(f)["Scrapped"]
        f.close()
        for entry in scrapped:
            if description == entry["description"]:
                self.originalSize = entry["count"]
                self.changeTickerCount = entry["changeTickerCount"]
                self.removecount = entry["removeCount"]
                return True
        return False

    # stripes unnessary symbols, data like "$100.0" isnt a float because of the "$"
    def toFloat(self, input):
        if input == "New":
            return "New"
        # TODO: refactor to use regex
        removelist = ["+", "%", ",", "$", ">"]
        for i in removelist:
            input = input.replace(i, "")
        return float(input) if input else 0.0

    # helper function so I dont have to type scrapper.data.to_csv(...) everytime
    def to_csv(self):
        self.data.to_csv(self.csvFilePath, index=False)

    # Once a url is scrapped, add it to the json file so its not scrapped again
    def addToScrapped(self) -> None:
        f = open("alreadyscrapped.json")
        scrapped = json.load(f)
        data = {
            "url": self.url,
            "description": self.description,
            "filePath": self.csvFilePath,
            "count": self.originalSize,
            "changeTickerCount": 0,
            "removeCount": 0
        }
        scrapped["Scrapped"].append(data)
        with open("alreadyscrapped.json", "w") as f:
            json.dump(scrapped, f)
        f.close()

    # after scrapping, add the remove count to the file
    def updateScrapped(self):
        f = open("alreadyscrapped.json")
        scrapped = json.load(f)
        for item in scrapped["Scrapped"]:
            if (item["url"] == self.url):
                item["changeTickerCount"] += self.changeTickerCount
                item["removeCount"] += self.removecount
                break
        with open("alreadyscrapped.json", "w") as f:
            json.dump(scrapped, f)
        f.close()

    # sometimes the data in a table is enwrapped in a div or h3 or a tag or multiple nested tags 
    # this function will traverse through it all to get the data
    # example: for the Company ticker, it is enwrapped in:   <div>  <b> <a> ACUTAL TICKER <a> <b> <div>
    # So I would type:  self.getChildData(tickerElement,"div b a") -> ACUTAL TICKER
    def getChildData(self, data, path) -> str:
        path = path.split(" ")
        childNode = None
        for child in path:
            childNode = data.find(child)
        return childNode.get_text()


# this is a helper class that holds all the time frames so I dont have to rewrite them in every class
class TimeFrame:

    def __init__(self) -> None:
        self.timeframe = ["2w","1m","2m","3m","4m","5m","6m","7m","8m",
                        "9m","10m","11m","1yr","2yr"]
        self.timeframepecent= ['2w%',"1m%","2m%","3m%","4m%","5m%","6m%","7m%",
                              "8m%","9m%","10m%","11m%", '1yr%', '2yr%']
        # how many days in each time frame
        self.tradedays = [
            10, 21, 42, 63, 84, 105, 126, 147, 168, 189, 210, 231, 252, 504
        ]
        # how many trade weeks in each week
        self.tradeweeks = [
            2, 4, 8, 12, 16, 21, 25, 30, 36, 38, 43, 47, 52, 104
        ]

    # this will return {"2w":10,"1m":21...etc}
    def getDaysDict(self):
        return dict(zip(self.timeframe, self.tradedays))

    # this will return {"2w":1,"1m":21...etc}
    def getWeekDict(self):
        return dict(zip(self.timeframe, self.tradeweeks))
