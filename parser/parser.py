from bs4 import BeautifulSoup

with open('https://www.rusgeocom.ru/products/teplovizor-amo-t820-s-poverkoy.html') as file:
    src = file.read()
    
    soup = BeautifulSoup(src, 'lxml')
    
    title = soup.title
    print(title)