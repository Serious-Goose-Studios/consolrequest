import requests
import threading


url = "https://www.texasfootball.com/api/staticPage/formResponseSave"
headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "cookie": "ASP.NET_SessionId=ol52u2chc5as5pt1ekm5yyy4; ARRAffinity=d076d30687d1d63a28581b948a35a00b480e9327765e61895b80b0f48fea9f5a; ARRAffinitySameSite=d076d30687d1d63a28581b948a35a00b480e9327765e61895b80b0f48fea9f5a",
    "Referer": "https://www.texasfootball.com/team-of-the-week/form",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}

data = {
    "formId": 18,
    "rspData": "{\"who_should_be_the_5a_team_of_the_year?\":\"A&M Consolidated\",\"who_should_be_the_6a_team_of_the_year?\":\"\",\"who_should_be_the_4a_team_of_the_year?\":\"\",\"who_should_be_the_3a_team_of_the_year?\":\"\",\"who_should_be_the_2a_team_of_the_year?\":\"\",\"who_should_be_the_1a_team_of_the_year?\":\"\",\"who_should_be_the_pvt_team_of_the_year?\":\"\"}",
}

v = 0

def consol():
    global v
    while True:
        response = requests.post(url, headers=headers, json=data)
        
        print(v, response.text)
        if response.status_code == 200:
            v += 1



for i in range(200):
    t1 = threading.Thread(target=consol)
    t1.start()

while True:
    if v > 10:
            with open("log.txt") as fin:
                a = int(fin.read())
            with open("log.txt", 'w') as fout:
                fout.write(str(a+v))
            v = 0 





