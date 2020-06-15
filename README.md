<h2>
  <br>
  Aircraft Accident Archives Data Scraper
  <br>
  <br>
</h2>

## Description



## Spesification

Runtime: Python ver. 3.7.7

Library used:
- BeautifulSoup (bs4)
- concurrent.futures
- json
- Request
- re
- threading

## How to Use

## JSON Structure

```
[
    {
      "Accident Date": "2019-09-16",
      "Accident Time": "12:26",
      "Airplane Operator": "twoFlex",
      "Airplane Type": "Cessna 208B Grand Caravan",
      "Flight Phase": "Takeoff ",
      "Crash Location": "Amazonas, Brazil",
      "Crash Site Terrain": "Airport ",
      "Crew on Board": "2",
      "Crew Casualties": "0",
      "Passenger on Board": "8",
      "Passenger Casualties": "0",
      "Other Casualties": "0"
    },
    {
    ...
    },
    ...
]
```
## Screenshot Program

## References

Library used in this program:
- [bs4](https://www.crummy.com/software/BeautifulSoup/)
- [concurrent futures](https://docs.python.org/3/library/concurrent.futures.html)
- [json](https://docs.python.org/3/library/json.html)
- [re](https://docs.python.org/3/library/re.html)
- [request](https://docs.python.org/3/library/urllib.request.html)
- [threading](https://docs.python.org/3/library/threading.html)
