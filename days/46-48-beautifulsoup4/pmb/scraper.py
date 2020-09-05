import requests
import bs4

OVERCAST_LOGIN_URL = "https://overcast.fm/login"
OVERCAST_PODCASTS_URL = "https://overcast.fm/podcasts"
USERNAME_FIELD = "email"
PASSWORD_FIELD = "password"


def pull_site():
    payload = {
        USERNAME_FIELD: "patrickburrell@gmail.com",
        PASSWORD_FIELD: "JVVpZxGPfgYi68hfYnMyXKMXD",
    }

    with requests.Session() as session:
        post = session.post(OVERCAST_LOGIN_URL, data=payload)
        response = session.get(OVERCAST_PODCASTS_URL)
        response.raise_for_status()

    return response


def scrape_site(site):
    header_list = []
    soup = bs4.BeautifulSoup(site.text, "html.parser")
    return soup


def get_podcasts(soup):
    podcasts = soup.find_all("a", class_="feedcell")
    return podcasts


def show_podcasts(podcasts):
    print()
    print("My Overcast Podcast Subscriptions")
    print("---------------------------------")
    for podcast in podcasts:
        print(podcast.div.div.div.text)
    print()


def main():
    site = pull_site()
    soup = scrape_site(site)
    podcasts = get_podcasts(soup)
    show_podcasts(podcasts)


if __name__ == "__main__":
    main()
