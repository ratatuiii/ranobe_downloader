from download_functions import *

def main():
    print('Hello!')
    print('This small script will help you to download ranobe from these sites:')
    print('ranobehub.org(ru)/ranobelib.me(ru)/novelmax.net(en)')
    book_name = input('Please enter the name of the book: ')
    #Need to check if the book is available on each site.
    print('Downloading a book...')
    parse_ranobelib(book_name)
    print('Book succesfully downloaded!')

main()
