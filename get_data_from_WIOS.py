import requests
import pycurl
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2017, 1, 1)
end_date = date(2017, 6, 2)
for single_date in daterange(start_date, end_date):
    print single_date.strftime("%Y.%m.%d")

# query={"measType":"Auto","viewType":"Parameter","dateRange":"Day","date":"01.12.2017","viewTypeEntityId":"pm2.5","channels":[202,211,1911]}
#
# http://monitoring.krakow.pios.gov.pl/dane-pomiarowe/pobierz
#
# curl "http://monitoring.krakow.pios.gov.pl/dane-pomiarowe/pobierz" -H "Host: monitoring.krakow.pios.gov.pl" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: pl,en-US;q=0.7,en;q=0.3" --compressed -H "Referer: http://monitoring.krakow.pios.gov.pl/dane-pomiarowe/automatyczne/parametr/pm2.5/stacje/202-211-1911/dzienny/01.12.2017" -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Cookie: cookiesAccepted=yes; _ga=GA1.3.1121058621.1511822560; start_selector_nth=0; start_selector_hide=yes" -H "Connection: keep-alive" --data "query="%"7B"%"22measType"%"22"%"3A"%"22Auto"%"22"%"2C"%"22viewType"%"22"%"3A"%"22Parameter"%"22"%"2C"%"22dateRange"%"22"%"3A"%"22Day"%"22"%"2C"%"22date"%"22"%"3A"%"2201.12.2017"%"22"%"2C"%"22viewTypeEntityId"%"22"%"3A"%"22pm2.5"%"22"%"2C"%"22channels"%"22"%"3A"%"5B202"%"2C211"%"2C1911"%"5D"%"7D"
#
# table_data = requests.get('http://monitoring.krakow.pios.gov.pl/dane-pomiarowe/automatyczne/parametr/pm2.5/stacje/202-211-1911/dzienny/01.12.2017').content
# print table_data