import requests
from bs4 import BeautifulSoup
from models import App

def get_results(query):

    url = "https://play.google.com/store/search?q="+query+"&c=apps"
    r = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
})

    html = r.text
    soup = BeautifulSoup(html)
    ids = []
    resSet = soup.find_all(class_="id-card-list card-list two-cards")
    allApps = resSet[0]
    for app in allApps.findAll("div"):
        if app['class']==['card', 'no-rationale', 'square-cover', 'apps', 'small']:
            print app['data-docid']
            ids.append(app['data-docid'])

    apps = []
    flags = []
    for l,id_ in enumerate(ids):
        if sum(flags)>=10:
            break
        if not App.objects.filter(appid=id_).exists():
            flags.append(get_info(id_))
        else:
            flags.append(True)

    for l,flag in enumerate(flags):
        print l, flag
        if flag:
            apps.append(App.objects.get(appid=ids[l]))

    return apps

def get_info(id_):

    url = "https://play.google.com/store/apps/details?id="+id_
    r = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
})
    html = r.text
    soup = BeautifulSoup(html)

    try:    
        title = soup.find(class_="id-app-title").get_text()
        rating = soup.select_one(".document-subtitle .star-rating-non-editable-container")["aria-label"].strip()

        devname = soup.find(class_="document-subtitle primary").get_text()

        for item in soup.select("div.details-section-contents div.meta-info"):
            if item.select("div.title") and item.select("div.content"):
                info = item.select("div.title")[0].get_text().strip()
                data = item.select("div.content")[0].get_text().strip()
                    
                if info=='Updated':
                    updated = data
                if info=='Size':
                    size = data
                if info=='Installs':
                    installs = data
                if info=='Current Version':
                    curver = data
                if info == 'Requires Android':
                    reqand = data

        src = soup.select("div.cover-container")[0].select("img")[0]['src']
        if not src.startswith("https"):
            src = "https:"+src
        print src
        newApp = App(title=title, appid=id_, rating_info = rating, devname = devname, size=size, \
            installs=installs, current_version = curver, reqs_android = reqand, updated=updated, \
            src=src)
        newApp.save()

        return True
    except:
        return False