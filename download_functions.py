import requests
from bs4 import BeautifulSoup as bs
from ebooklib import epub
def parse_ranobelib(name):

    params = {'name' : name} #params for finding a book in catalogue

    response = requests.get('https://ranobelib.me/manga-list', params = params) # gets a desired page with params and parses it
    soup = bs(response.text, 'html.parser')

    url = soup.find_all('a', class_ ="media-card")[0].get('href') #finds book url

    response = requests.get(url) # parses book's main page
    soup = bs(response.text, 'html.parser')

    chapter_amount = int(soup.find_all('div', class_="media-info-list__value text-capitalize")[1].text) # gets amount of chapters to pars
    chapter_url = soup.find_all('a', class_ ="button button_block button_primary")[0].get('href') # gets url to main chapter


    #initializing a book
    book = epub.EpubBook()

    book.set_identifier(f"idk")
    book.set_title(name)
    book.set_language("ru")
    book.add_author("Author Authorowski")
    book.spine = []

    chapter_pointer = 1
    while chapter_pointer != chapter_amount+1:
        try:
            response = requests.get(chapter_url, params = params) # parses page
            soup = bs(response.text, 'html.parser')

            chapter = epub.EpubHtml(title=f"Chapter {chapter_pointer}", file_name=f"chapter_{chapter_pointer}.xhtml", lang="ru") # creates new epub chapter

            chapter_text = soup.find_all('div', class_ = "reader-container container container_center")[0] # parses text of a chapter

            chapter_title = f'''<h1> Глава {chapter_pointer} </h1>'''

            chapter.content = chapter_title + str(chapter_text)
            book.add_item(chapter)
            book.spine.append(chapter)

            if chapter_pointer != chapter_amount:
                chapter_url = soup.find_all('a', class_="reader-next__btn button text-truncate button_label button_label_right")[0].get('href')
            print(f"Chapter {chapter_pointer}/{chapter_amount}. {round(chapter_pointer/chapter_amount, 2)*100}%")
            chapter_pointer += 1
        except:
            print('Something went wrong. Trying again...')
            response = requests.get(chapter_url, params = params) # parses page
            soup = bs(response.text, 'html.parser')

            chapter = epub.EpubHtml(title=f"Chapter {chapter_pointer}", file_name=f"chapter_{chapter_pointer}.xhtml", lang="ru") # creates new epub chapter

            chapter_text = soup.find_all('div', class_ = "reader-container container container_center")[0] # parses text of a chapter

            chapter_title = f'''<h1> Глава {chapter_pointer} </h1>'''

            chapter.content = chapter_title + str(chapter_text)
            book.add_item(chapter)
            book.spine.append(chapter)

            if chapter_pointer != chapter_amount:
                chapter_url = soup.find_all('a', class_="reader-next__btn button text-truncate button_label button_label_right")[0].get('href')

            print(f"Chapter {chapter_pointer}/{chapter_amount}. {round((chapter_pointer * 100)/chapter_amount, 2)}%")
            chapter_pointer += 1
    epub.write_epub(f"books/{'_'.join(name.split())}.epub", book, {})
    return name


# print(parse_ranobelib('Мать Ученья'))