import csv
import pathlib
from bs4 import BeautifulSoup
import time
# import pandas as pd
# from IPython.display import display
from pageopen import get_soup_from_sel
from greq_open import local_file_open
import string
import pandas as pd
from db_class import StorageDatabase

URL_JAZZ = "https://www.secrettelaviv.com/tickets/categories/live-music"
FILE = "data.csv"


def scrape_site(start, start_url, file_name = ""):

    db = StorageDatabase("sql11.freemysqlhosting.net", "3306", "sql11593194", "sql11593194", "2CPjwjQHDQ")
    #
    newfile = False
    if not pathlib.Path(file_name).is_file():
        newfile = True
    csv_file = open(file_name,'a',newline='')
    csv_writer = csv.writer(csv_file)
    if newfile:
        csv_writer.writerow(['name', 'venue', 'date', 'time', 'description', 'href'])

    try:
        # soup = get_soup_from_sel("https://www.secrettelaviv.com/tickets/bad-night-sponsored-by-a")
        soup = local_file_open('secrettelaviv.html')
        # soup = single_url_open(start_url)
    except FileNotFoundError as ex:
        # csv_file.close()
        print(ex)
        return
    data = []
    hrefs = []
    soup = soup.find(class_="events-page")
    # soup = soup.find("ul")
    for i, parameter in enumerate(soup.find_all("tr")):
        # if i == 2:
        #     break
        # print(parameter)
        # for parameter in soup.find_all(class_="usajobs-joa-summary__item usajobs-joa-summary--beta__item"):
        # print("Class_found")
        href_item_soup = parameter.find("a", href=True)
        a_string = str(href_item_soup).split('"')
        if len(a_string) > 2:
            href = a_string[1]
            name_ven = a_string[2].split('@')
            name = name_ven[0].strip(' >')
            try:
                venue = name_ven[1].split('<')[0].strip()
            except:
                venue = ''
            print(href, name, venue)
            soup1 = get_soup_from_sel(href)
            # print(soup1)
            desc_section = soup1.find(class_="em em-view-container")
            text = desc_section.text.splitlines()
            while len(text[0]) == 0:
                text.pop(0)
            date_time = text[0].split('|')
            date = date_time[0].strip()
            time = date_time[1].strip()
            text.pop(0)
            while len(text[0]) == 0:
                text.pop(0)
            print(date,time)
            # print(text)


            description = []
            for a_string in text:

                a_string = a_string.translate(str.maketrans('','',string.punctuation))

                a_string = a_string.split()
                if " ".join(a_string) == "Check Out The Event Page On Facebook":
                    break
                if len(a_string) > 0:
                    description.extend(a_string)


            description = " ".join(description)
            print(description)
            data.append([name, venue, date, time, description, href])
            data_dict = {"name": name, "venue": venue, "date" : date, "time" :time,
                         "description" : description, "url" : href}
            db.table_add_row('TLV', data_dict)
            csv_writer.writerow([name, venue, date, time, description, href])
        if i > 10 and i % 10 == 0:
            db.db_commit()
    db.db_commit()
    # df = pd.DataFrame(data, columns = ['name', 'venue', 'date', 'time', 'description', 'href'])
    # df.to_csv(file_name)








        # url = txt.split('"')[1]
        # print(url)
        # print("/".join(href_item_soup['href'].split('/')[:1]))
        # hrefs.append(href_item_soup['href'])
        # print(href_item_soup['href'])

    # c_hrefs = ['/'.join(a.strip('/').split('/')[:2]) for a in hrefs]
    # print(c_hrefs[:3])
    # c_hrefs = [1,2,3]
    #
    # newfile = False
    # if not pathlib.Path(file_name).is_file():
    #     newfile = True
    # csv_file = open(file_name, 'a', newline='')
    # csv_writer = csv.writer(csv_file)
    # if newfile:
    #     csv_writer.writerow(['No', 'Name', 'Text'])
    #
    # for i, ref in enumerate(c_hrefs):
    #     if i < start:
    #         continue
    #     if i == 100:
    #         break
    #     page_url = f"https://www.afisha.ru/{ref}"
    #
    #     try:
    #         soup1 = single_url_open(page_url)
    #     except FileNotFoundError as ex:
    #         csv_file.close()
    #         print("Event page not open")
    #         print(ex)
    #         return
    #
    #     texts = soup1.find_all(class_="_1V-Pk")
    #     names = soup1.find("h1", class_="KOq_N")
    #     name = names.find_all('span')
    #     print(name[1].text)
    #     csv_writer.writerow([i, name[1].text, texts[1].text])
    #     time.sleep(20)
    # csv_file.close()
    #

def test_scrape():
    file_name = 'texts.csv'
    c_hrefs = [1,2,3]
    newfile = False
    if not pathlib.Path(file_name).is_file():
        newfile = True
    csv_file = open(file_name,'a',newline='')
    csv_writer = csv.writer(csv_file)
    if newfile:
        csv_writer.writerow(['No', 'Name', 'Text'])


    for i, ref in enumerate(c_hrefs):
        if i == 1000:
            break

        soup1 = local_file_open("page.html")
        texts = soup1.find_all(class_="_1V-Pk")
        names = soup1.find("h1", class_="KOq_N")
        name = names.find_all('span')
        csv_writer.writerow([i, name[1].text, texts[1].text])

    csv_file.close()

# def show_csv(file_name):
#     df = pd.read_csv(file_name)
#     display(df)

if __name__ == "__main__":
    # scrape_site(24, URL_JAZZ, JAZZ_FILE)
    scrape_site(0, URL_JAZZ, FILE)
    # show_csv(CLASSICS_FILE)