import requests as rq
from bs4 import BeautifulSoup as Bs

def check_404(url):
    broken = []
    good = []

    # Télécharger la page web.
    res = rq.get(url)
    res.raise_for_status()

    # Analyser le contenu de la réponse.
    soup = Bs(res.text, 'html.parser')
    a_tags = soup.find_all("a")

    # Trouver tous les liens commençant par 'http'.
    links = [a_tag.get('href') for a_tag in a_tags if str(a_tag.get('href')).startswith('http')]

    # Télécharger chaque page web, tester si elle est introuvable ou non.
    for link in links:
        try:
            res = rq.get(link)

            if res.status_code != 404:
                print('good:', link)
                good.append(link)
            else:
                print('NOT FOUND:', link)
                broken.append(link)
        except rq.exceptions.ConnectionError:
            print('good:', link)
            good.append(link)

    print('\nGood links:', len(good),"\n",'Not Found:', len(broken))
    print('\nLiens introuvables : ',broken)

if __name__ == "__main__":
    check_404('http://ensam-casa.ma')