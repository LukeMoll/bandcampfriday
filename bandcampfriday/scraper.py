import urllib.request
from bs4 import BeautifulSoup
import json, datetime

def get_fundraisers() -> list:
    with urllib.request.urlopen("https://isitbandcampfriday.com/") as res:
        html = res.read()

        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find("div", attrs={"id":"bandcamp-friday-vm"})
        if div is not None:
            try:
                lst = json.loads(div.attrs['data-fundraisers'])
                assert type(lst) is list
                assert len(lst) > 0

                return lst

            except KeyError:
                ...

def next_friday(fundraisers: list) -> dict:
    fri = fundraisers[0]
    assert type(fri) is dict
    assert "date" in fri
    assert str(fri["date"]).startswith("Fri")

    fri["datetime"] = datetime.datetime.strptime(fri["date"], "%a, %d %b %Y %H:%M:%S %z")

    return fri

def is_it_bandcamp_friday(fri) -> bool:
    start = fri["datetime"]
    end = start + datetime.timedelta(days=1)
    now = datetime.datetime.now(tz=datetime.timezone.utc)

    if start <= now <= end:
        return True
    else:
        return False