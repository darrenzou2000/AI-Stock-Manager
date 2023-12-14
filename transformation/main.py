import pandas as pd
import requests
import os
if __name__ == "__main__":
    
    groupData = pd.read_csv("../GroupData.csv")
    
    print(groupData.head())