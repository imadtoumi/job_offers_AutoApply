from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Enter the wbsite
url = "https://www.marocannonces.com/index.php"


def autoenter(url):
    try:
        # Open the browser
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service = service)

        driver.get(url)
        sleep(0.5)

        # Enter the job listing page
        offreemploi = driver.find_element(By.XPATH, '//*[@id="twocolumns"]/div[1]/ul/li[1]/a/span[1]').click()
        sleep(3)

        # Start looking for what you want
        keyword = driver.find_element(By.CLASS_NAME, 'kw').send_keys("Devops")
        sleep(0.5)

        domaindropdown = Select(driver.find_element(By.XPATH, '//*[@id="field_3"]/select'))
        domaindropdown.select_by_visible_text('Informatique / Multimédia / Internet')
        sleep(1)

        citydropdown = Select(driver.find_element(By.XPATH, '//*[@id="select-ville"]'))
        citydropdown.select_by_visible_text("Casablanca")

        return driver.page_source
    
    except Exception as e:
        print(f"Error , {e}")
        return 0


def extract(new_url):
    soup = BeautifulSoup(new_url, 'html.parser')

    retrieved_links = []
    for item in soup.find_all("a", href = True):
        link = item["href"]
        if "Développeur" in link:
            retrieved_links.append(link)

    return retrieved_links  


def comparelinks(retrieved_links):
    reader = open("links.txt", "r", encoding="utf-8").readlines()

    offers = []
    for link in retrieved_links:
        link = "https://www.marocannonces.com/"+link+"\n"
        in_file = False
        for line in reader:
            if link == line:
                in_file = True
                print(f"{link} is already in the file")
                break
        
        if not in_file:
            offers.append(link)

    return offers
    

def savetofile(offers):
    with open("links.txt", "a", encoding="utf-8") as file:
        for link in offers:
            file.write(link)


def main():
    new_url = autoenter(url)
    if new_url == 0:
        print("Error")
    else:
        if retrieved_links:= extract(new_url):
            offers = comparelinks(retrieved_links)
            savetofile(offers)


if __name__ == "__main__":
    main()