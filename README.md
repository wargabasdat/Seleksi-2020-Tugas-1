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
- Request
- BeautifulSoup
- concurrent.futures
- json
- re

## How to Use

## JSON Structure

```
[
    {
      "Accident Date": "2020-05-22",
      "Accident Time": "14:39",
      "Airplane Operator": "Pakistan International Airlines",
      "Airplane Type": "Airbus A320",
      "Flight Phase": "Landing ",
      "Crash Site Terrain": "City",
      "Crew on Board": "8",
      "Crew Casualties": "8",
      "Passenger on Board": "91",
      "Passenger Casualties": "89",
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
