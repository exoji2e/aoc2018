import os
import glob
def log(s):
    print('Fetch: {}'.format(s))

def dl(fname, day, year):
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
    with open(fname,'w') as f:
        f.write(r.text)

def mkdirs(f):
    try:
        os.makedirs(f)
    except: pass


def fetch(day, year=2018, force=False):
    filename = 'cache/{}.in'.format(str(day))
    mkdirs('cache')
    exists = os.path.isfile(filename)
    if not exists or force:
        dl(filename, day, year)
    return open(filename, 'r').read().strip('\n')


def get_samples(day, year=2018):
    d = 'samples/{}_{}'.format(year,day)
    mkdirs(d)
    samples = []
    for fname in glob.glob('{}/*.in'.format(d)):
        inp = open(fname, 'r').read().strip('\n')
        samples.append((fname, inp))
    return samples

