import requests
from bs4 import BeautifulSoup

site_url = 'https://myanimelist.net'
response = requests.get(site_url)
print(response.status_code)
print(len(response.text))

doc = BeautifulSoup(response.text, 'html.parser')
print(type(doc))



def gettingTheListOfAnime(linkOfPage):
    most_popular_URL = site_url + linkOfPage
    response = requests.get(most_popular_URL)
    doc = BeautifulSoup(response.text, 'html.parser')
    headers = doc.find('tr', class_='table-header')
    headers.find_all('td')
    row_content = doc.find_all('tr', {'class': "ranking-list"})

    # method to parse the html doc from the episdoes in a more awesthetic way
    def parse_episodes(listt):
        result = []
        for i in listt[:2]:
            r = i.strip()
            result.append(r)
        return result

    # getting rank, title, rating, episodes and release date
    # this for loop will loop through the dictionary row ocntents and will gather the information for each row.
    # top anime list will contain a dictionary for anime, which is added to the list using the append method
    top_anime = []
    for row in row_content:
        episode = parse_episodes(row.find('div', class_="information di-ib mt4").text.strip().split('\n'))
        ranking = {
        'Rank': row.find('td', class_="rank ac").find('span').text,
        'Title': row.find('div', class_="di-ib clearfix").find('a').text,
        'Rating': row.find('td', class_="score ac fs14").find('span').text,
        'Episodes': episode[0],
        'Dates': episode[1]
            }
        top_anime.append(ranking)


    return top_anime


def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return

        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")
def append_csv(items, path):
    # Open the file in write mode
    with open(path, 'a') as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return

        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")

topAnime50 = gettingTheListOfAnime('/topanime.php?type=bypopularity')
write_csv(topAnime50, 'top_anime.csv')

topAnime100 = gettingTheListOfAnime('/topanime.php?type=bypopularity&limit=50')
append_csv(topAnime100, 'top_anime.csv')

topAnime150 =  gettingTheListOfAnime('/topanime.php?type=bypopularity&limit=100')
append_csv(topAnime150, 'top_anime.csv')

topAnime200 = gettingTheListOfAnime('/topanime.php?type=bypopularity&limit=150')
append_csv(topAnime200, 'top_anime.csv')

topAnime250 = gettingTheListOfAnime('/topanime.php?type=bypopularity&limit=200')
append_csv(topAnime250, 'top_anime.csv')

topAnime300 = gettingTheListOfAnime('/topanime.php?type=bypopularity&limit=250')
append_csv(topAnime300, 'top_anime.csv')