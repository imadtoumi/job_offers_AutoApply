import os
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


# Import info from csv file
def get_info():
    with open("info.csv",newline="",encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                login_name = row["login_name"]
                login_pass = row["login_pass"]
                name = row["name"]
                phone = row["phone"]
                city = row["city"]

    return login_name, login_pass, name, phone, city

# Function reponsible for the form filling
def formautomation(driver, name, phone, city):
    is_processed = False
    name_field = driver.find_element(By.XPATH, '//*[@id="c_senders_name"]').send_keys(name)
    sleep(2)

    phone_field = driver.find_element(By.XPATH, '//*[@id="c_senders_phone"]').send_keys(phone)
    sleep(2)

    motivation_field = driver.find_element(By.XPATH, '//*[@id="c_senders_comments"]').send_keys(".")
    sleep(2)

    # Drop Downs
    select_sa = Select(driver.find_element(By.ID,'secteur_cv'))
    sleep(1)
    select_sa.select_by_visible_text('Informatique / Multimédia / Internet')
    sleep(1)

    fonction = driver.find_element(By.XPATH, '//*[@id="domaine_cv"]').send_keys("Informatique")
    sleep(2)

    niveau_etude = Select(driver.find_element(By.XPATH, '//*[@id="c_senders_studylevel"]'))
    sleep(1)
    niveau_etude.select_by_visible_text('Bac +2')
    sleep(1)

    experience = Select(driver.find_element(By.XPATH, '//*[@id="c_senders_experience"]'))
    sleep(1)
    experience.select_by_visible_text('Moins de 1 an')
    sleep(1)

    ville = Select(driver.find_element(By.XPATH, '//*[@id="c_senders_city"]'))
    sleep(1)
    ville.select_by_visible_text(city)
    sleep(1)

    cv = driver.find_element(By.XPATH, '//*[@id="cv"]').send_keys(os.getcwd()+"/cv-.pdf")
    sleep(2)
                
    #postuler = driver.find_element(By.XPATH, '//*[@id="btn_envoyer"]').click()
    sleep(3)
    is_processed = True
    return is_processed

def login(driver, login_name, login_pass):
    # Perform login only once
    try:
        driver.get(url = "https://www.marocannonces.com/mon-compte/")
        name_input = driver.find_element(By.ID, "username").send_keys(login_name)
        sleep(1)

        password_input = driver.find_element(By.ID, "password").send_keys(login_pass)
        sleep(1)

        login_button = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div[1]/form/fieldset/input').click()
        sleep(2)   
    except Exception as e:
        print(f"Error in login {e}")
        driver.quit()

def apply(driver, login_name, login_pass, name, phone, city):
    login(driver, login_name, login_pass)
    # Offer's url are retrieved from the links.txt file and deleted after they are applied to
    reader = open("links.txt", "r", encoding="utf-8").readlines()

    processedoffers = []

    remaining_offers = []

    for offer in reader :
        try:
            driver.get(url = offer)
            sleep(2)

            postuler_button = driver.find_element(By.CLASS_NAME, "btn-reply").click()
            sleep(3)

            # Application
            is_processed = formautomation(driver, name, phone, city)

            # Delete the offer link from the file if applied to  
            if not is_processed: 
                break
            elif is_processed:
                print(f"{offer} was applied to successfully")
                processedoffers.append(offer)
                            
        except Exception as e:
            print(f"Error {e}")

    for link in reader:
        if link in processedoffers:
            print(f"{link} must be gone")
            continue
        elif link not in processedoffers:
            remaining_offers.append(link)

    with open("links.txt", "w", encoding="utf-8") as file:
        for line in remaining_offers:
            file.write(line)

    driver.quit()


def main():
    # Initialize WebDriver
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service = service)

    # Get login details
    login_name, login_pass, name, phone, city = get_info()
    apply(driver, login_name, login_pass, name, phone, city)

if __name__ == "__main__":
    main()