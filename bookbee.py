import requests

API_URL = 'https://library.memoryoftheworld.org/search/titles/'

def main():
    query = input('🔍 Search for a book: ')

    response = requests.get(API_URL + query)

    if response.status_code == requests.codes.ok:
        data = response.json()
        data = data['_items']

        print('')

        for (index, book) in enumerate(data, start=1):
            if book['authors']:
                authors = ','.join(book['authors'])
            else:
                authors = 'No authors'
            print(f'({index}) - ' + book['title'] + f' [{authors}] ' + str(len(book['formats'])) + ' formats')

        print('')
        choice = int(input('Enter the index for your choice of book: '))
        chosen = data[choice - 1]
        library_url = chosen['library_url']

        print('')
        print('Available formats: ')
        for (index, formt) in enumerate(chosen['formats'], start=1):
            print(f'({index}) - ' + formt['format'])

        print('')
        file_choice = int(input('Enter the index for your preferred format: '))
        file_chosen = chosen['formats'][file_choice - 1]

        try:
            download_url = 'https:' + library_url + file_chosen['dir_path'] + file_chosen['file_name']
            filenm = file_chosen['file_name']

            r = requests.get(download_url)

            open(filenm, 'wb').write(r.content)
            
            print(f"File has downloaded! Saved as {filenm}")
        except:
            print("Couldn't download file")    
            print(f"Here's the download link: {download_url}")    

if __name__ == '__main__':
    main()