import requests
from bs4 import BeautifulSoup as bs


def get_soup(url:str):
    session = requests.Session()
    html = session.get(url).content
    soup = bs(html,'lxml')

    return soup
def get_categorys(soup):
    category = soup.find_all('li',attrs = {'class':'menu__popUp__link--category'})
    categorys = []
    if category == None:
        return None
    for elements in category:
        categorys.append(elements.text)

    return categorys
def get_sub_link(soup):
    link = soup.find('a',attrs = {'class':'result'})['href']
    return link
def get_article_title(sub_soup):
    title = sub_soup.find('div',attrs = {'class':'article__content__head__text'})
    if title == None:
        return None
    title = title.find('h1').text

    return title
def get_article_content(sub_soup):
    content = []
    pre_content = sub_soup.find('div',attrs = {'class':'content_wrapper'})
    if pre_content == None:
        return None
    pre_content = pre_content.find_all('p')
    for p in pre_content:
        content.append(p.text)
    del(content[0])
    return ' '.join(content)
def get_tags(sub_soup):
    tags = []
    tg = sub_soup.find_all('a',attrs = {'class':'tag'})
    if tg == None:
        return None
    for tag in tg:
        tags.append(tag.text)

    return ','.join(tags)
def get_category(soup,sub_link):
    article = soup.find('a',attrs = {'href':sub_link})
    category = article.find('div',attrs = {'class':'atom__additional_category'}).text
    if category == None:
        return None
    return category
def get_img(sub_soup):
    img = sub_soup.find('amp-img',attrs = {'layout':'responsive'})
    if img == None:
        return None
    return img['src']
def get_date(sub_soup):
    date = sub_soup.find('div',attrs = {'class':'article__head__additional_published'}).text
    if date == None:
        return None

    return date
def decode(content):
    return content.replace('\xa0',' ')
def mix_content(soup,sub_soup,sub_link):
    text_content = [decode(get_article_title(sub_soup)),
                    decode(get_article_content(sub_soup)),
                    get_date(sub_soup),
                    get_tags(sub_soup),
                    get_category(soup,sub_link),
                    get_img(sub_soup)
                    ]

    return '__'.join(text_content)
def main():
    soup = get_soup('https://nv.ua/allnews.html')
    sub_link = get_sub_link(soup)
    sub_soup = get_soup(sub_link)
    content =  mix_content(soup,sub_soup,sub_link)
    return content
if __name__ == '__main__':
    main()
