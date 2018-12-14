import os
def log(s):
    print('Fetch: {}'.format(s))

def fetch(day, year=2018):
    filename = 'cache/{}.in'.format(str(day))
    
    if not os.path.isdir('cache'):
        os.mkdir('cache')
    exists = os.path.isfile(filename)
    if not exists:
        import requests
        from secret import session
        jar = requests.cookies.RequestsCookieJar()
        jar.set('session', session)
        url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
        r = requests.get(url, cookies=jar)
        if 'Puzzle inputs' in r.text:
            log('Session cookie expired?')
            return r.text
        if "Please don't repeatedly request this endpoint before it unlocks!" in r.text:
            log('Output not available yet')
            return r.text
        if r.status_code != 200:
            log('Not 200 as status code')
            return r.text
        with open(filename,'w') as f:
            f.write(r.text.strip())
    return open(filename, 'r').read().strip('\n')

