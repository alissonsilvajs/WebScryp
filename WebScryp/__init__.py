from requests import get
from wget import download
from sys import argv

class WebScryp:
    def __init__(self):
        self.run() 
        # Call the run function
    def run(self):
        """
        Collect the command line arguments
        """
        if len(argv) == 1:
            print("Try: python main.py <website whitout https://>")
        elif len(argv) == 2:
            if argv[1]:
                r = get("https://" + argv[1])
                print(r.text)
                self.download_file()
                
    def download_file(self):
        question = input("Download (Y/N):").upper()
        if question == "Y":
            download("https://" + argv[1])
        elif question == "N":
            print("GoodBye")