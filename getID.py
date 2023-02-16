import requests 
import pprint
import csv
import time
baseurl = "https://api.mangadex.org/manga/random/"
params = {
    'includes[]': [
        'manga',
        'cover_art',
    ],
    'contentRating[]': [
        'safe',
        'suggestive',
        'erotica',
        'pornographic',
    ],
    'includedTagsMode': 'AND',
    'excludedTagsMode': 'OR',
}

def main():
    with open('mangaIDs.csv', 'a+', encoding='utf-8') as csvfile:
        csvfile = csvfile.readlines() 
    
        try:
            lastRow = csvfile[-1]
        except IndexError:
            lastRow = ''

        while True:
            r = requests.get(baseurl, params=params)
            ## Add a time delay here for 2 seconds
            time.sleep(2)

            data = r.json()
            title = (data['data']['attributes']['title']['en'])
            mangaid = (data['data']['id'])
            contentrating = (data['data']['attributes']['contentRating'])

            if mangaid not in lastRow:
                with open('mangaIDs.csv', 'a+', encoding='utf-8') as csvfile:
                    fieldnames = ['Title', 'MangaID', 'ContentRating']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
                    writer.writerow({'Title': title, 'MangaID': mangaid, 'ContentRating': contentrating})
                    print("Title: " + title + " MangaID: " + mangaid + " ContentRating: " + contentrating)
            
            csvfile.close()
            
if __name__ == '__main__':
    main()
