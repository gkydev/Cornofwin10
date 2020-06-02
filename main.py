from abc import ABC, abstractmethod
from win10toast import ToastNotifier
from copy import deepcopy
from resources import *
import time
class Prototype(ABC):
    @abstractmethod
    def __init__(self):
        self.county = "country"
        self.total_cases = "total_cases"
        self.recovered_cases = "recovered_cases"
        self.deaths = "deaths"
    @abstractmethod
    def clone(self):
        pass
class VirusData(Prototype):
    def __init__(self, country, total_cases, recovered_cases, deaths):
        self.country = country
        self.total_cases = total_cases
        self.recovered_cases = recovered_cases
        self.deaths = deaths
    def __operation__(self):
        self.performed_operation = True
    def clone(self):
        return deepcopy(self)
class Main():
    def main(self):
        while True:
            scarper = Scarper()
            us_scarp = scarper.UsDataScarper()
            us_data = VirusData("US",us_scarp[0],us_scarp[1],us_scarp[2])
            tr_scarp = scarper.TrDataScarper()
            tr_data = us_data.clone()
            tr_data.country = "TR"
            tr_data.total_cases = tr_scarp[0]
            tr_data.recovered_cases = tr_scarp[1]
            tr_data.deaths = tr_scarp[2]
            toaster = ToastNotifier()
            print("Sending Notificaiton")
            toaster.show_toast("Corona Virus Notification",
            "|"+ "  " +"Total Cases " + "|" + " Recovered Cases " + "|" + " Deaths \n" + us_data.country + " " + us_data.total_cases + "\t" + us_data.recovered_cases + "\t         " + us_data.deaths + "\n" + tr_data.country + "   " + tr_data.total_cases + "\t" + tr_data.recovered_cases + "\t         " + tr_data.deaths , duration=30 , icon_path="covid.ico"
            )
            time.sleep(86400)
Main().main()