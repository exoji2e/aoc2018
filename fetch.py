import requests, os

from secret import session

def fetch(day, year=2018):
    filename = 'cache/{}.in'.format(str(day))
    
    if not os.path.isdir('cache'):
        os.mkdir('cache')
    exists = os.path.isfile(filename)
    if not exists:
        jar = requests.cookies.RequestsCookieJar()
        jar.set('session', session)
        url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
        r = requests.get(url, cookies=jar)
        with open(filename,'w') as f:
            f.write(r.text.strip())
    return open(filename, 'r').read()

