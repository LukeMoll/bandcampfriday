import argparse
from datetime import timedelta

from bandcampfriday import backends
import bandcampfriday


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", required=True, choices=backends.available_backends())
    parser.add_argument("--webhook-url")

    bandcampfriday.args = parser.parse_args()
    

    backend = backends.get_backend(bandcampfriday.args.backend)

    from bandcampfriday import scraper
    from bandcampfriday import message
    fri = scraper.next_friday(scraper.get_fundraisers())
    if scraper.is_it_bandcamp_friday(fri):
        backend.send_message(message.get_message_yes(fri["datetime"] + timedelta(days=1)))
    else:
        backend.send_message(message.get_message_no(fri["datetime"]))

if __name__ == "__main__":
    main()