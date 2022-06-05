import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import json

answer_key_question = []

class main:
    def __init__(self, username, password,name, activity_id,subject):
        self.username = username
        self.password = password
        self.name = name
        self.activity_id = activity_id
        self.bot = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.page_link = ""
        self.subject = subject
        self.is_true = True

    def login(self):
        bot = self.bot
        bot.get("https://elearning.gyaschool.com/login/index.php")
        username = bot.find_element(By.NAME, "username")
        username.send_keys(self.username)
        password = bot.find_element(By.NAME, "password")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def open_activity(self):
        bot = self.bot
        print(self.activity_id)
        bot.get('https://elearning.gyaschool.com/mod/quiz/view.php?id=' + self.activity_id)
        start_attempt_btn = bot.find_element(By.XPATH, "//button[normalize-space()='Attempt quiz now']")
        start_attempt_btn.click()
        WebDriverWait(bot, 180).until(EC.presence_of_element_located((By.CLASS_NAME, "yui3-widget-stdmod")))
        confirm_start_attempt = bot.find_element(By.ID, "id_submitbutton")
        confirm_start_attempt.click()
        WebDriverWait(bot, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "info")))
        self.page_link = bot.current_url
        print(self.page_link)

    def fill_answer(self):
        link = self.page_link
        self.bot.get(link)
        file = f"{self.subject.lower()}.json"
        print(self.name)
        while self.is_true:
            with open(file, 'r') as f:
                formulation = self.bot.find_elements(By.CLASS_NAME, "formulation ")
                answer_sheet = json.load(f)
                time.sleep(5)
                for x in formulation:
                    for q in x.find_elements(By.CLASS_NAME, "qtext"):
                        for y in x.find_elements(By.CLASS_NAME, "answer"):
                            answer = y.find_elements(By.TAG_NAME, "div")
                            for ans in answer:
                                radio_button = ans.find_elements(By.TAG_NAME, "input")
                                for button in radio_button:
                                    for key, value in answer_sheet.items():
                                        if q.text == value:
                                            ans2 = answer_sheet[f"answer{key[5:]}"]
                                            z = ans.text
                                            if ans2[2:] == z[2:]:
                                                 button.click()
                                                 print("clicked")
                                                 self.page_link = self.bot.current_url

                    for key, value in answer_sheet.items():
                        for a in x.find_elements(By.TAG_NAME, "tbody"):
                            for b in a.find_elements(By.TAG_NAME, "tr"):
                                question_text = b.find_elements(By.CLASS_NAME,"text")
                                for q in question_text:
                                    option = b.find_elements(By.TAG_NAME, "option")
                                    for opt in option:
                                        if q.text == value:
                                            if opt.text == answer_sheet[f"manswer{key[5:]}"]:
                                                print("btn clicked")
                                                opt.click()


            yo = input("Has next page[Yes or No]: ")
            if yo.lower() == "yes":
                self.bot.find_elements(By.CLASS_NAME, "mod_quiz-next-nav")[0].click()
                WebDriverWait(self.bot, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "info")))
                self.is_true = True
            elif yo.lower() == "no":
                self.is_true = False
                self.bot.find_elements(By.CLASS_NAME, "mod_quiz-next-nav")[0].click()
                po = input("Continue[Yes or No]: ")
                if po.lower() != "yes":
                    sleep(100)


actvity_id = input("Enter the activity ID: ")
subject = input("Subject: ")
user1 = {
    "name": "Dagmawi Solomon",
    "username": "1192043@gyaschool.com",
    "password": "tbFvBY@sTzhL"
}
user2 = {
    "name": "Natnael Amde",
    "username": "8100100258@gyaschool.com",
    "password": "0911606469N"
}
user3 = {
    "name" : "A/J",
    "username": "8100991@gyaschool.com",
    "password": "8100991A"
}
user4 = {
    "name": "Hawlet Muhdin",
    "username": "7654321",
    "password": "Hawlet7654"
}
user5 = {
    "name": "Yohannes",
    "username": "1169126",
    "password": "12345678910Jo",
}
user6 = {
    "name": "Musab",
    "username": "1121513",
    "password": "M1121513m",
}
user7 = {
    "name": "Beshar Semir",
    "username": "1171548",
    "password": "Besharsemir",
}
user8 = {
    "name": "Enaya Redwan",
    "username": "1193302",
    "password": "Er@1193302",
}
user9 = {
    "name": "Asim",
    "username": "201815790@gyaschool.com",
    "password": "A201815790",
}
user10 = {
    "name" :"Enaya hussien",
    "username": "201568054@gyaschool.com",
    "password": "Enayahussien",
}
user11 = {
    "name" :"Oumer Yasin",
    "username": "1156506@gyaschool.com",
    "password": "Onecuberocks",
}
user12 = {
    "name":"Sumeya Mohammed",
    "username": "1155377@gyaschool.com",
    "password": "Mohasusu1913",
}
user13 = {
    "name":"Nardos k",
    "username": "8100100348",
    "password": "Meronbiruk",
}
user14 = {
    "name": "Eyoel",
    "username": "654322@gyaschool.com",
    "password": "Eyoel2003",
}
user15 = {
    "name": "Newal B",
    "username": "1143057",
    "password": "Newalnbnb",
}
user16 = {
    "name": "yafet",
    "username": "201596837",
    "password": "ABC6277620911",
}
user17 = {
    "name": "Ikhlas",
    "username": "1146626",
    "password": "Ikamohhd",
}
user18 = {
    "name": "Teyam",
    "username": "1134461",
    "password": "Vinsmoke3$",
}
user19 = {
    "name": "Dawit",
    "username": "1129971",
    "password": "Dawithaile",

}
user20 = {
    "name": "Nebiyu",
    "username": "201517301",
    "password": "Nebyu123",
}
user21 = {
    "name": "Abel",
    "username": "8100524",
    "password": "Ab3lm3ch@l",
}
user22 = {
    "name": "Hanan",
    "username": "201567083",
    "password": "Hs@201567083"
}
user23 = {
    "name": "Intisar",
    "username": "201658865",
    "password": "Intuk@m03",
}
users = {
    # "user5": user5,
    # "user14": user14,
    # "user3": user3,
    # "user2": user2,
    "user1": user1,
    # "user9": user9,
    # "user16": user16,
    # "user17": user17,
    # "user18": user18,
    "user7": user7,
    "user22": user22,
    "user23": user23,
    # "user15": user15,
    # "user20": user20
    # 'user4': user4,
    # "user8": user8,
     # "user12": user12,
    # "user13": user13,
    # "user10": user10,
    # "user11": user11,
    # "user19": user19
    # "user21": user21
}
for key, value in users.items():
    var = main(value["username"], value["password"],value['name'], actvity_id,subject)
    var.login()
    var.open_activity()
    var.fill_answer()





