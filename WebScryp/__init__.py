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
            print("Try: python run.py <website link>")
        elif len(argv) == 2:
            r = get(argv[1])
            print(r.text)
            self.download_file()
                
    def download_file(self):
        question = input("Download (Y/N):").upper()
        if question == "Y":
            download(argv[1])
        else:
            print("GoodBye")
