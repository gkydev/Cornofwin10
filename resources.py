import requests
from bs4 import BeautifulSoup as bs
class Scarper():
    def UsDataScarper(self):
        r = requests.get("https://www.worldometers.info/coronavirus/country/us/")
        soup = bs(r.text,"html.parser")
        data = soup.findAll("div",{"class": "maincounter-number"})
        all_cases = str(data[0]).strip('<div class="maincounter-number">').strip('<span>').strip('</span>').strip('</div>').strip('</span>\n').strip('\n<span style="color:#aaa">')
        deaths = str(data[1]).strip('<div class="maincounter-number">').strip('<span>').strip('</span>').strip('</div>').strip('\n<span>').strip('</span>\n')
        recovered_cases = str(data[2]).strip('<div class="maincounter-number">').strip('<span>').strip('</span>').strip('</div>').strip('yle="color:#8ACA2B ">\n<span>').strip('</span>\n')
        return_data = [all_cases,deaths,recovered_cases]
        return return_data
    def TrDataScarper(self):
        r = requests.get("https://www.worldometers.info/coronavirus/country/turkey/")
        soup = bs(r.text,"html.parser")
        data = soup.findAll("div",{"class": "maincounter-number"})
        all_cases = str(data[0]).strip('<div class="maincounter-number">').strip('<span>').strip('</span>').strip('</div>').strip('</span>\n').strip('\n<span style="color:#aaa">')
        deaths = str(data[1]).strip('<div class="maincounter-number">').strip('<span>').strip('</span>').strip('</div>').strip('\n<span>').strip('</span>\n')
        recovered_cases = str(data[2]).strip('<div class="maincounter-number">').strip('<span>').strip('</span>').strip('</div>').strip('yle="color:#8ACA2B ">\n<span>').strip('</span>\n')
        return_data = [all_cases,recovered_cases,deaths]
        return return_data
