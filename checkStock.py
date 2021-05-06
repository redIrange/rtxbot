from urllib.request import urlopen
    
def checkStock(url):
    page = urlopen(url)
    print(page)
    html_bytes = page.read()
    html = html_bytes.decode("latin-1")
    print(html)
    file = open("file.txt","w")
    for line in html:
        file.write(line)
    with open('file.txt') as f:
        if 'Sorry, this item is out of stock.<br />Please <a class="lk simple-lk" href="#rr_placement_1">click here</a> to view similar products.' in f.read():
            return True
        else:
            return False

getHtml("https://www.currys.co.uk/gbuk/computing-accessories/components-upgrades/graphics-cards/msi-geforce-rtx-3060-12-gb-ventus-2x-oc-graphics-card-10220926-pdt.html")