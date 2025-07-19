# 👤 Author & Rights
# Tool Name: Scayid
# Author: Scayar
# All rights reserved © Scayar
# Website: scayar.com | Telegram: @im_scayar | Email: Scayar.exe@gmail.com | BuyMeACoffee: buymeacoffee.com/scayar
#!/usr/bin/python3
import time
import json
import csv
import os
from bs4 import BeautifulSoup
from core.colours import *
import requests
import gender_guesser.detector as gender
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
import random
import string
import qrcode

# TODO: Consider using the 'rich' library for more advanced color and style output in Scayid.

class Person(object):
    def __init__(self, target_gender=None, nationality=None, max_retries=5):
        def strip_value(str):
            if 'value="' in str:
                text_beg = str.index('value="') + 7
                text_end = str.index('"/></div>')
                str = str[text_beg:text_end]
                return str
            if '<p>' in str:
                text_beg = str.index('<p>') + 3
                text_end = str.index('</p>')
                str = str[text_beg:text_end]
                return str
            return str

        import random
        from rich.console import Console
        console = Console()
        person_data = {}
        url = 'https://www.fakepersongenerator.com/Index/generate'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Referer': 'https://www.fakepersongenerator.com/'
        }
        attempts = 0
        while attempts < max_retries:
            attempts += 1
            try:
                req = requests.post(url, headers=headers, timeout=10)
                page = requests.get(req.url, headers=headers, timeout=10)
                if page.status_code != 200:
                    continue
            except requests.RequestException as e:
                console.print(f"[bold red]Request failed: {e}[/bold red]")
                import time; time.sleep(1)
                continue
            soup = BeautifulSoup(page.content, 'html.parser')
            category = soup.select('.info-title')
            name_raw = soup.select('.click')
            data_raw = str(soup.select('.col-md-8'))
            data2 = soup.select('.info-detail')
            if not name_raw or not name_raw[0].string:
                console.print(f"[bold yellow]No name found on the page. Retrying...[/bold yellow]")
                continue
            name = name_raw[0].string.strip()

            index = data_raw.find('<p')
            data_main = []
            data_main_val = []

            while index != -1:
                iterator = 1
                index2 = data_raw.find('<p', index + iterator)
                build_string = data_raw[index + 3: index2 - 4] if index2 != -1 else data_raw[index + 3:]
                data_main.append(build_string)
                index = index2
                iterator += 1

            for a in range(len(data_main)):
                data_main[a] = data_main[a].replace('<b>', '').replace('</b>', '').replace('title="test">', '')
                data_main_val.append(data_main[a][data_main[a].index(':') + 2:])
                data_main[a] = data_main[a][:data_main[a].index(':')]
                person_data[data_main[a]] = data_main_val[a]

            for b in range(len(data2)):
                cat_text = category[b].string if category[b].string else category[b].get_text(strip=True)
                category[b] = cat_text.strip() if cat_text else "Unknown"
                data2[b] = strip_value(str(data2[b]))
                data2[b] = data2[b].replace('<', '<').replace('<br/>', '\n\t\t').replace('"', '"')
                person_data[category[b]] = data2[b]

            self.name = name
            self.race = person_data.get('Race')
            self.birthday = person_data.get('Birthday')
            self.street = person_data.get('Street')
            self.telephone = person_data.get('Telephone')
            self.mobile = person_data.get('Mobile')
            self.email = person_data.get("Email")
            if not self.email or self.email.lower() == 'none':
                # Generate a realistic email
                name_parts = self.name.lower().replace("'", "").replace('.', '').split()
                if len(name_parts) >= 2:
                    base = f"{name_parts[0]}.{name_parts[-1]}"
                else:
                    base = name_parts[0]
                domains = ["gmail.com", "protonmail.com", "outlook.com", "mail.com", "tutanota.com"]
                domain = random.choice(domains)
                self.email = f"{base}@{domain}"
            self.height = person_data.get("Height")
            self.weight = person_data.get("Weight")
            self.hair_color = person_data.get("Hair Color")
            self.blood_type = person_data.get("Blood Type")
            self.zodiac = person_data.get('Starsign(Tropical Zodiac)')
            self.mother_maiden_name = person_data.get("Mother's Maiden Name")
            self.civil_status = person_data.get("Civil Status")
            self.educational_background = person_data.get("Educational Background")
            self.disease_history = person_data.get("Disease History")
            self.social_security = person_data.get("Social Security Number")
            self.passport = person_data.get("Passport")
            self.driver_license = person_data.get("Driver License")
            self.car_license_plate = person_data.get("Car License Plate")
            self.employment_status = person_data.get("Employment Status")
            self.monthly_salary = person_data.get("Monthly Salary")
            self.occupation = person_data.get("Occupation(Job Title)")
            self.company_name = person_data.get("Company Name")
            self.company_size = person_data.get("company_Size")
            self.industry = person_data.get("Industry")
            self.credit_card_type = person_data.get("Credit Card Type")
            self.credit_card_number = person_data.get("Credit Card Number")
            self.cvv2 = person_data.get("CVV2")
            self.expires = person_data.get("Expires")
            self.paypal = person_data.get("Paypal")
            self.western_union_mtcn = person_data.get("Western Union MTCN")
            self.moneygram_mtcn = person_data.get("MoneyGram MTCN")
            self.account_balance = person_data.get("Account Balance")
            self.orders_lifetime = person_data.get("Orders Lifetime")
            self.total_consumption = person_data.get("Total Consumption")
            self.preferred_payment = person_data.get("Preferred Payment")
            self.family_members = person_data.get("Family Members")
            self.vehicle = person_data.get("Vehicle")
            self.online_status = person_data.get("Online Status")
            self.online_signature = person_data.get("Online Signature")
            self.online_biography = person_data.get("Online Biography")
            self.interest = person_data.get("Interest")
            self.favorite_color = person_data.get("Favorite Color")
            self.favorite_movie = person_data.get("Favorite Movie")
            self.favorite_music = person_data.get("Favorite Music")
            self.favorite_song = person_data.get("Favorite Song")
            self.favorite_book = person_data.get("Favorite Book")
            self.favorite_sports = person_data.get("Favorite Sports")
            self.favorite_tv = person_data.get("Favorite TV")
            self.favorite_movie_star = person_data.get("Favorite Movie Star")
            self.favorite_singer = person_data.get("Favorite Singer")
            self.favorite_food = person_data.get("Favorite Food")
            self.personality = person_data.get("Personality")
            self.person_style = person_data.get("Personal Style")
            self.website = person_data.get("Website")
            self.register_time = person_data.get("Register Time")
            self.register_ip = person_data.get("Register IP")
            self.points = person_data.get("Points")
            self.level = person_data.get("Level")
            self.number_of_comments = person_data.get("Number of Comments")
            self.posted_articles = person_data.get("Posted Articles")
            self.friends = person_data.get("Friends")
            self.language = person_data.get("Language")
            self.verified_status = person_data.get("Verified Status")
            self.security_question = person_data.get("Security Question")
            self.security_answer = person_data.get("Security Answer")
            self.browser_user_agent = person_data.get("Browser User Agent")
            self.system = person_data.get("System")
            self.guid = person_data.get("GUID")
            self.geo_coordinates = person_data.get("Geo coordinates")
            self.timezone = person_data.get("Timezone")
            self.ups_tracking = person_data.get("UPS Tracking Number")
            self.country = person_data.get("Country", nationality if nationality else "Unknown")
            self.country_code = person_data.get("Country Code")

            # Gender detection and filtering
            a = str(self.name)
            name_split = a.split()
            df = name_split[0]
            d = gender.Detector(case_sensitive=False)
            self.detected_gender = d.get_gender(df)
            # Flexible gender match
            if target_gender and self.detected_gender and target_gender.lower() not in self.detected_gender.lower():
                console.print(f"[bold yellow]Gender mismatch: {self.detected_gender} != {target_gender} (retrying...)[/bold yellow]")
                continue
            # Flexible nationality match
            if nationality and self.country and not self.country.lower().startswith(nationality.lower()):
                console.print(f"[bold yellow]Nationality mismatch: {self.country} != {nationality} (retrying...)[/bold yellow]")
                continue
            break
        else:
            # Fallback after retries
            self.name = f"Agent {random.randint(1000,9999)}"
            self.detected_gender = target_gender or "unknown"
            self.country = nationality or "Unknown"
            console.print(f"[bold red]Could not find a matching profile after {max_retries} attempts. Using fallback identity.[/bold red]")

        # After extracting all fields, ensure Security & Financial fields are always present
        for key in [
            'credit_card_type', 'credit_card_number', 'cvv2', 'expires', 'paypal',
            'western_union_mtcn', 'moneygram_mtcn', 'account_balance', 'preferred_payment',
            'social_security', 'passport', 'driver_license', 'car_license_plate']:
            if not hasattr(self, key) or getattr(self, key, None) is None:
                setattr(self, key, '—')

        # Generate Security & Financial info if missing
        def fake_cc_number():
            # Simple Luhn-valid Visa/MC/Amex/Discover
            cc_types = [
                ("Visa", "4"),
                ("MasterCard", "5"),
                ("Amex", "3"),
                ("Discover", "6")
            ]
            ctype, prefix = random.choice(cc_types)
            if ctype == "Amex":
                num = prefix + ''.join(random.choices(string.digits, k=13))
            else:
                num = prefix + ''.join(random.choices(string.digits, k=15))
            return ctype, ' '.join([num[i:i+4] for i in range(0, len(num), 4)])
        def fake_cvv(ctype):
            return ''.join(random.choices(string.digits, k=4 if ctype=="Amex" else 3))
        def fake_exp():
            month = str(random.randint(1,12)).zfill(2)
            year = str(random.randint(25, 29))
            return f"{month}/{year}"
        def fake_paypal(email):
            return email if email and email != '—' else f"user{random.randint(1000,9999)}@paypal.com"
        def fake_mtcn():
            return ''.join(random.choices(string.digits, k=10))
        def fake_balance():
            return f"${random.randint(100, 9999):,}.00"
        def fake_ssn():
            return f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(1000,9999)}"
        def fake_passport():
            return random.choice(['X','Y','Z']) + ''.join(random.choices(string.digits, k=7))
        def fake_dl():
            return random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=3)) + '-' + ''.join(random.choices(string.digits, k=4)) + '-' + ''.join(random.choices(string.digits, k=4))
        def fake_plate():
            return ''.join(random.choices(string.ascii_uppercase, k=3)) + '-' + ''.join(random.choices(string.digits, k=4))
        # Always present, generate if missing
        ctype, ccnum = fake_cc_number() if not getattr(self, 'credit_card_type', None) or getattr(self, 'credit_card_type', None) == '—' else (self.credit_card_type, self.credit_card_number)
        self.credit_card_type = ctype
        self.credit_card_number = ccnum
        self.cvv2 = fake_cvv(ctype) if not getattr(self, 'cvv2', None) or getattr(self, 'cvv2', None) == '—' else self.cvv2
        self.expires = fake_exp() if not getattr(self, 'expires', None) or getattr(self, 'expires', None) == '—' else self.expires
        self.paypal = fake_paypal(self.email)
        self.western_union_mtcn = fake_mtcn() if not getattr(self, 'western_union_mtcn', None) or getattr(self, 'western_union_mtcn', None) == '—' else self.western_union_mtcn
        self.moneygram_mtcn = fake_mtcn() if not getattr(self, 'moneygram_mtcn', None) or getattr(self, 'moneygram_mtcn', None) == '—' else self.moneygram_mtcn
        self.account_balance = fake_balance() if not getattr(self, 'account_balance', None) or getattr(self, 'account_balance', None) == '—' else self.account_balance
        self.preferred_payment = random.choice(["PayPal", "Credit Card", "Wire Transfer"]) if not getattr(self, 'preferred_payment', None) or getattr(self, 'preferred_payment', None) == '—' else self.preferred_payment
        self.social_security = fake_ssn() if not getattr(self, 'social_security', None) or getattr(self, 'social_security', None) == '—' else self.social_security
        self.passport = fake_passport() if not getattr(self, 'passport', None) or getattr(self, 'passport', None) == '—' else self.passport
        self.driver_license = fake_dl() if not getattr(self, 'driver_license', None) or getattr(self, 'driver_license', None) == '—' else self.driver_license
        self.car_license_plate = fake_plate() if not getattr(self, 'car_license_plate', None) or getattr(self, 'car_license_plate', None) == '—' else self.car_license_plate

        # Generate interest if missing
        hacker_interests = [
            "Ethical hacking", "Cybersecurity", "Open source coding", "Social engineering", "Digital art",
            "Cryptocurrency", "Pen testing", "AI & machine learning", "Lockpicking", "Retro gaming",
            "Urban exploration", "Drone racing", "Privacy advocacy", "Capture the flag (CTF)", "Bug bounty hunting",
            "Linux customization", "Reverse engineering", "Steganography", "Phreaking", "Network sniffing",
            "Malware analysis", "IoT tinkering", "RFID hacking", "Dark web research", "Forensics"
        ]
        if not hasattr(self, 'interest') or not self.interest or self.interest == '—':
            self.interest = random.choice(hacker_interests)

    def to_dict(self):
        return {
            "name": self.name, "detected_gender": self.detected_gender, "birthday": self.birthday, "zodiac": self.zodiac,
            "mother_maiden_name": self.mother_maiden_name, "family_members": self.family_members,
            "personality": self.personality, "person_style": self.person_style, "language": self.language,
            "verified_status": self.verified_status, "country": self.country, "country_code": self.country_code,
            "street": self.street, "geo_coordinates": self.geo_coordinates, "timezone": self.timezone,
            "employment_status": self.employment_status, "monthly_salary": self.monthly_salary,
            "occupation": self.occupation, "company_name": self.company_name, "company_size": self.company_size,
            "industry": self.industry, "favorite_color": self.favorite_color, "favorite_movie": self.favorite_movie,
            "favorite_music": self.favorite_music, "favorite_song": self.favorite_song, "favorite_book": self.favorite_book,
            "favorite_sports": self.favorite_sports, "favorite_tv": self.favorite_tv,
            "favorite_movie_star": self.favorite_movie_star, "favorite_singer": self.favorite_singer,
            "favorite_food": self.favorite_food, "credit_card_type": self.credit_card_type,
            "credit_card_number": self.credit_card_number, "cvv2": self.cvv2, "expires": self.expires,
            "paypal": self.paypal, "western_union_mtcn": self.western_union_mtcn, "moneygram_mtcn": self.moneygram_mtcn,
            "account_balance": self.account_balance, "preferred_payment": self.preferred_payment,
            "telephone": self.telephone, "mobile": self.mobile, "website": self.website, "email": self.email,
            "online_status": self.online_status, "online_signature": self.online_signature,
            "online_biography": self.online_biography, "security_question": self.security_question,
            "security_answer": self.security_answer, "browser_user_agent": self.browser_user_agent,
            "height": self.height, "weight": self.weight, "hair_color": self.hair_color, "blood_type": self.blood_type,
            "disease_history": self.disease_history, "civil_status": self.civil_status,
            "educational_background": self.educational_background, "social_security": self.social_security,
            "passport": self.passport, "driver_license": self.driver_license, "car_license_plate": self.car_license_plate,
            "vehicle": self.vehicle, "register_time": self.register_time, "register_ip": self.register_ip,
            "points": self.points, "level": self.level, "number_of_comments": self.number_of_comments,
            "posted_articles": self.posted_articles, "friends": self.friends, "ups_tracking": self.ups_tracking
        }

def save_data(person, output_format, filename):
    data_dict = person.to_dict()
    if output_format == 'txt':
        data_str = '''
{ 
    "personal details": {  
        "name": "%s",   
        "gender": "%s",   
        "birthday": "%s",
        "zodiac": "%s",
        "Mother Maiden Name": "%s",
        "Family Members": "%s",
        "Personality": "%s",
        "Person Style": "%s",
        "Language": "%s",
        "Verified Status": "%s",
        "Country": "%s",
        "Country Code": "%s",
        
    "Address and Location": {
        "street": "%s",
        "Geo Coordinates": "%s",
        "Timezone": "%s",
        
    "Employment":{
        "Employment Status": "%s",
        "Monthly Salary": "%s",
        "Occupation": "%s",
        "Company Name": "%s",
        "Company Size": "%s",
        "Industry": "%s",
    
    "Favorite": {
        "color": "%s",
        "Movie": "%s",
        "Music": "%s",
        "Song": "%s",
        "Book": "%s",
        "Sports": "%s",
        "TV": "%s",
        "Movie Star": "%s",
        "Singer": "%s",
        "Food": "%s",

    "Financial": {
        "Credit Card Type": "%s",
        "Credit Card Number": "%s",
        "CVV2": "%s",
        "Expires On:": "%s",
        "PayPal": "%s",
        "Western Union MTCN": "%s",
        "MoneyGram MTCN": "%s",
        "Account Balance": "%s",
        "Preferred Payment": "%s",

    "phonenumber": {
        "telephone": "%s",
        "mobile": "%s",
        
    "Online Details": {
        "Website": "%s",
        "email": "%s",
        "Online Status": "%s",
        "Online Signature": "%s",
        "Online Biography": "%s",
        "Security Question": "%s",
        "Security Answer": "%s",
        "Browser User Agent": "%s",
        
    "Physical Characteristics": {
        "height": "%s",
        "weight": "%s",
        "hair color": "%s",
        "blood types": "%s",
        
    "Medical History": {
        "Disease History": "%s",
      
    "Other Details": {
        "Civil Status": "%s",
        "Educational Background": "%s",
        "Social Security Number": "%s",
        "Passport": "%s",
        "Driver License": "%s",
        "Car License Plate": "%s",
        "Vehicle": "%s",
        "Register Time": "%s",
        "Register IP": "%s",
        "Points": "%s",
        "Level": "%s",
        "Number of Comments": "%s",
        "Posted Articles": "%s",
        "Friends": "%s",
        "UPS Tracking Number": "%s"
    
}}}}}}}}}}}
''' % (
            person.name, person.detected_gender, person.birthday, person.zodiac, person.mother_maiden_name, person.family_members, person.personality, person.person_style, person.language, person.verified_status, person.country, person.country_code, person.street, person.geo_coordinates, person.timezone, person.employment_status, person.monthly_salary, person.occupation, person.company_name, person.company_size, person.industry, person.favorite_color, person.favorite_movie, person.favorite_music, person.favorite_song, person.favorite_book, person.favorite_sports, person.favorite_tv, person.favorite_movie_star, person.favorite_singer, person.favorite_food, person.credit_card_type, person.credit_card_number, person.cvv2, person.expires, person.paypal, person.western_union_mtcn, person.moneygram_mtcn, person.account_balance, person.preferred_payment, person.telephone, person.mobile, person.website, person.email, person.online_status, person.online_signature, person.online_biography, person.security_question, person.security_answer, person.browser_user_agent, person.height, person.weight, person.hair_color, person.blood_type, person.disease_history, person.civil_status, person.educational_background, person.social_security, person.passport, person.driver_license, person.car_license_plate, person.vehicle, person.register_time, person.register_ip, person.points, person.level, person.number_of_comments, person.posted_articles, person.friends, person.ups_tracking)
        with open(f"{filename}.txt", 'w', encoding='utf-8') as file:
            file.write(data_str)
    elif output_format == 'json':
        with open(f"{filename}.json", 'w') as file:
            json.dump(data_dict, file, indent=4)
    elif output_format == 'csv':
        with open(f"{filename}.csv", 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data_dict.keys())
            writer.writeheader()
            writer.writerow(data_dict)

def save_html_profile(person, filename):
    data = person.to_dict()
    def safe(val):
        return val if val and str(val).strip().lower() != 'none' else '—'
    qr_img = f"{filename}_qr.png"
    vcf_file = f"{filename}.vcf"
    sections = [
        ("Personal Info", [
            ("Name", "name"), ("Gender", "detected_gender"), ("Birthday", "birthday"), ("Zodiac", "zodiac"),
            ("Country", "country"), ("Country Code", "country_code"), ("Geo Coordinates", "geo_coordinates"), ("Timezone", "timezone"),
            ("Race", "race"), ("Height", "height"), ("Weight", "weight"), ("Blood Type", "blood_type"),
            ("Mother's Maiden Name", "mother_maiden_name"), ("Family Members", "family_members"), ("Civil Status", "civil_status"),
            ("Educational Background", "educational_background"), ("Disease History", "disease_history"),
        ]),
        ("Contact", [
            ("Phone", "telephone"), ("Mobile", "mobile"), ("Email", "email"), ("Street", "street"),
        ]),
        ("Employment", [
            ("Profession", "occupation"), ("Company", "company_name"), ("Company Size", "company_size"), ("Industry", "industry"),
            ("Employment Status", "employment_status"), ("Monthly Salary", "monthly_salary"),
        ]),
        ("Online", [
            ("Website", "website"), ("Language", "language"), ("Online Status", "online_status"), ("Biography", "online_biography"),
            ("Online Signature", "online_signature"), ("Register Time", "register_time"), ("Register IP", "register_ip"),
            ("Points", "points"), ("Level", "level"), ("Number of Comments", "number_of_comments"), ("Posted Articles", "posted_articles"), ("Friends", "friends"),
        ]),
        ("Favorites", [
            ("Color", "favorite_color"), ("Movie", "favorite_movie"), ("Food", "favorite_food"), ("Music", "favorite_music"), ("Book", "favorite_book"),
            ("Sports", "favorite_sports"), ("TV", "favorite_tv"), ("Movie Star", "favorite_movie_star"), ("Singer", "favorite_singer"),
        ]),
        ("Security & Financial", [
            ("Credit Card Type", "credit_card_type"), ("Credit Card Number", "credit_card_number"), ("CVV2", "cvv2"), ("Expires", "expires"),
            ("PayPal", "paypal"), ("Western Union MTCN", "western_union_mtcn"), ("MoneyGram MTCN", "moneygram_mtcn"), ("Account Balance", "account_balance"),
            ("Preferred Payment", "preferred_payment"), ("Social Security", "social_security"), ("Passport", "passport"), ("Driver License", "driver_license"),
            ("Car License Plate", "car_license_plate"), ("Vehicle", "vehicle"),
        ]),
        ("Other Details", [
            ("Personality", "personality"), ("Personal Style", "person_style"), ("Interest", "interest"),
            ("Security Question", "security_question"), ("Security Answer", "security_answer"), ("Browser User Agent", "browser_user_agent"),
            ("UPS Tracking Number", "ups_tracking"),
        ]),
    ]
    shown_keys = set(k for sec in sections for _, k in sec[1])
    extra = [(k.replace('_', ' ').title(), k) for k in data.keys() if k not in shown_keys]
    if extra:
        sections.append(("Extra", extra))
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scayid Profile - {safe(data['name'])}</title>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{ background: #101820; color: #e0ffe0; font-family: 'Fira Mono', 'Consolas', monospace; margin: 0; padding: 0; }}
        .container {{ max-width: 900px; margin: 48px auto; background: #181c25; border-radius: 18px; box-shadow: 0 0 32px #39ff1440; padding: 0 0 40px 0; }}
        .identity-card {{ background: #23283a; border-radius: 16px; box-shadow: 0 2px 16px #00ffe740; margin: 0 32px 32px 32px; padding: 24px 24px 18px 24px; display: flex; flex-direction: column; align-items: center; gap: 1.2em; }}
        .identity-main {{ display: flex; flex-direction: row; align-items: center; gap: 1.5em; width: 100%; justify-content: center; }}
        .identity-info {{ flex: 1; }}
        .identity-label {{ color: #39ff14; font-weight: bold; min-width: 120px; display: inline-block; letter-spacing: 1px; }}
        .identity-value {{ color: #e0ffe0; font-weight: 400; font-size: 1.1em; }}
        .qr-img {{ width: 110px; height: 110px; border-radius: 10px; box-shadow: 0 0 12px #00ffe7; background: #fff; object-fit: contain; }}
        .vcard-btn {{ background: #39ff14; color: #101820; border: none; border-radius: 6px; padding: 10px 18px; font-size: 1em; font-family: inherit; font-weight: bold; cursor: pointer; margin-top: 10px; box-shadow: 0 2px 8px #39ff1440; transition: background 0.2s; }}
        .vcard-btn:hover {{ background: #00ffe7; color: #101820; }}
        .copy-btn {{ background: #23283a; color: #00ffe7; border: 1px solid #00ffe7; border-radius: 4px; padding: 2px 8px; font-size: 0.9em; margin-left: 8px; cursor: pointer; transition: background 0.2s; }}
        .copy-btn:hover {{ background: #00ffe7; color: #23283a; }}
        .sticky-banner {{ position: sticky; top: 0; background: #101820ee; z-index: 10; padding: 32px 0 16px 0; border-radius: 18px 18px 0 0; box-shadow: 0 2px 16px #39ff1440; }}
        .banner {{ font-size: 2.3em; font-weight: bold; text-align: center; color: #39ff14; text-shadow: 0 0 16px #39ff14, 0 0 2px #fff; letter-spacing: 2px; }}
        .hacker-bar {{ width: 80%; margin: 18px auto 0 auto; height: 5px; background: linear-gradient(90deg, #39ff14, #00ffe7, #39ff14, #00ffe7); background-size: 200% 100%; animation: barMove 2s linear infinite; border-radius: 3px; }}
        @keyframes barMove {{ 0% {{background-position: 0 0;}} 100% {{background-position: 200% 0;}} }}
        .section-card {{ background: #23283a; border-radius: 12px; box-shadow: 0 2px 12px #00ffe720; margin: 32px 32px 0 32px; padding: 24px 32px 18px 32px; transition: box-shadow 0.2s; }}
        .section-card:hover {{ box-shadow: 0 4px 24px #39ff1470; }}
        h2 {{ color: #00ffe7; margin-top: 0; margin-bottom: 18px; font-size: 1.3em; letter-spacing: 1px; text-shadow: 0 0 8px #00ffe7; display: flex; align-items: center; gap: 0.5em; }}
        .kv {{ margin-bottom: 10px; display: flex; flex-wrap: wrap; }}
        .label {{ color: #39ff14; font-weight: bold; min-width: 200px; display: inline-block; letter-spacing: 1px; }}
        .value {{ color: #e0ffe0; font-weight: 400; }}
        .footer {{ margin-top: 40px; text-align: center; color: #39ff14; font-size: 1.1em; opacity: 0.7; }}
        @media (max-width: 700px) {{
            .container {{ max-width: 98vw; margin: 0; border-radius: 0; box-shadow: none; }}
            .section-card {{ margin: 24px 4vw 0 4vw; padding: 18px 8vw 12px 8vw; }}
            .sticky-banner {{ padding: 24px 0 10px 0; }}
            .identity-card {{ margin: 0 4vw 24px 4vw; padding: 18px 4vw 12px 4vw; }}
            .identity-main {{ flex-direction: column; gap: 0.7em; }}
        }}
    </style>
    <script>
    function copyToClipboard(text) {{
        navigator.clipboard.writeText(text);
        alert('Copied: ' + text);
    }}
    </script>
</head>
<body>
    <div class="container">
        <div class="sticky-banner">
            <div class="banner">🕵️‍♂️ SCAYID HACKER PROFILE</div>
            <div class="hacker-bar"></div>
        </div>
        <div class="identity-card">
            <div class="identity-main">
                <img src="{qr_img}" alt="QR Code" class="qr-img" />
                <div class="identity-info">
                    <div><span class="identity-label">Name:</span> <span class="identity-value">{safe(data['name'])}</span></div>
                    <div><span class="identity-label">Phone:</span> <span class="identity-value">{safe(data['telephone'])}</span><button class="copy-btn" onclick="copyToClipboard('{safe(data['telephone'])}')">Copy</button></div>
                    <div><span class="identity-label">Email:</span> <span class="identity-value">{safe(data['email'])}</span><button class="copy-btn" onclick="copyToClipboard('{safe(data['email'])}')">Copy</button></div>
                </div>
            </div>
            <a href="{vcf_file}" download><button class="vcard-btn">Download vCard</button></a>
        </div>
        {''.join(f'<div class="section-card"><h2>{sec}</h2>' + ''.join(f'<div class="kv"><span class="label">{label}:</span> <span class="value">{safe(data.get(key))}</span></div>' for label, key in fields) + '</div>' for sec, fields in sections)}
        <div class="footer">
            <div>Generated by <b>Scayid</b> &copy; Scayar</div>
            <div>Website: <a href="https://scayar.com" style="color:#00ffe7;">scayar.com</a></div>
        </div>
    </div>
</body>
</html>'''
    with open(f"{filename}.html", "w", encoding="utf-8") as f:
        f.write(html)

def save_vcard(person, filename):
    data = person.to_dict()
    vcard = f'''BEGIN:VCARD
VERSION:3.0
FN:{data['name']}
N:{data['name']}
EMAIL:{data['email']}
TEL;TYPE=CELL:{data['mobile']}
TEL;TYPE=HOME:{data['telephone']}
ADR;TYPE=HOME:;;{data['street']};{data['country']}
ORG:{data['company_name']}
TITLE:{data['occupation']}
URL:{data['website']}
BDAY:{data['birthday']}
NOTE:Generated by Scayid
END:VCARD'''
    with open(f"{filename}.vcf", "w", encoding="utf-8") as f:
        f.write(vcard)
    return vcard

def save_qr_code(vcard, filename):
    img = qrcode.make(vcard)
    img.save(f"{filename}_qr.png")

def _scayid_full_output(person, output_format):
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.progress import Progress
    import random
    import os
    import sys
    console = Console()
    with Progress() as progress:
        task = progress.add_task("[cyan]Connecting to the internet...", total=30)
        for _ in range(30):
            import time; time.sleep(0.01)
            progress.update(task, advance=1)
        task2 = progress.add_task("[magenta]Fetching Information...", total=30)
        for _ in range(30):
            import time; time.sleep(0.01)
            progress.update(task2, advance=1)
    table = Table(title=f"[🕵️‍♂️] SCAYID PROFILE", show_header=False, box=None, expand=True)
    table.add_row("[bold green]Name:", f"{person.name}")
    table.add_row("[bold cyan]Gender:", f"{person.detected_gender}")
    table.add_row("[bold magenta]Birthday:", f"{person.birthday}")
    table.add_row("[bold yellow]Zodiac:", f"{person.zodiac}")
    table.add_row("[bold yellow]Country:", f"{person.country}")
    table.add_row("[bold blue]Geo:", f"{person.geo_coordinates}")
    table.add_row("[bold white]Timezone:", f"{person.timezone}")
    table.add_row("[bold red]Phone:", f"{person.telephone}")
    table.add_row("[bold green]Email:", f"{person.email}")
    table.add_row("[bold cyan]Height:", f"{person.height}")
    table.add_row("[bold magenta]Weight:", f"{person.weight}")
    table.add_row("[bold blue]Profession:", f"{person.occupation}")
    table.add_row("[bold blue]Company:", f"{person.company_name}")
    table.add_row("[bold blue]Industry:", f"{person.industry}")
    table.add_row("[bold blue]Language:", f"{person.language}")
    table.add_row("[bold blue]Website:", f"{person.website}")
    table.add_row("[bold blue]Blood Type:", f"{person.blood_type}")
    table.add_row("[bold blue]Favorite Color:", f"{person.favorite_color}")
    table.add_row("[bold blue]Favorite Movie:", f"{person.favorite_movie}")
    table.add_row("[bold blue]Favorite Food:", f"{person.favorite_food}")
    threat_level = random.choice(["LOW", "MEDIUM", "HIGH"])
    digital_footprint = random.choice(["MINIMAL", "MODERATE", "EXTENSIVE"])
    completeness = random.randint(85, 100)
    summary = f"[bold white]Profile:[/bold white] {person.name} | {person.country} | {person.zodiac} | {person.height} | {person.weight}"
    stats = f"[bold bright_black]Threat Level:[/bold bright_black] [bold red]{threat_level}[/bold red]   [bold bright_black]Digital Footprint:[/bold bright_black] [bold green]{digital_footprint}[/bold green]\n[bold bright_black]Profile Completeness:[/bold bright_black] [bold yellow]{completeness}%[/bold yellow]"
    console.print(Panel(table, title="[bold green]🕵️‍♂️ SCAYID PROFILE[/bold green]", border_style="bold magenta"))
    console.print(summary)
    console.print(stats)
    try:
        os.mkdir(person.name)
    except OSError as e:
        console.print(f"[bold red]Failed to create directory {person.name}: {e}[/bold red]")
        sys.exit(1)
    os.chdir(person.name)
    save_data(person, output_format, person.name)
    save_html_profile(person, person.name)
    vcard = save_vcard(person, person.name)
    save_qr_code(vcard, person.name)
    console.print(f"[bold white on green]✔ VCF (vCard) saved: ./{person.name}.vcf[/bold white on green]")
    console.print(f"[bold white on green]✔ QR code saved: ./{person.name}_qr.png[/bold white on green]")
    console.print(f"[bold white on green]✔ HTML profile: ./{person.name}.html[/bold white on green]")
    console.print("[bold bright_black]Tip:[/bold bright_black] Use -s to deploy a social media presence for this identity.")
    sys.exit(0)

def simpleinfogathermale(nationality=None, output_format='txt'):
    while True:
        try:
            person = Person(target_gender='male', nationality=nationality)
            break
        except ValueError as e:
            print(f"{bad} {e}")
            import time; time.sleep(1)
    _scayid_full_output(person, output_format)

def simpleinfogathermalewithprofession(profession, nationality=None, output_format='txt'):
    while True:
        try:
            person = Person(target_gender='male', nationality=nationality)
            break
        except ValueError as e:
            print(f"{bad} {e}")
            import time; time.sleep(1)
    person.occupation = profession
    _scayid_full_output(person, output_format)

def simpleinfogatherfemale(nationality=None, output_format='txt'):
    while True:
        try:
            person = Person(target_gender='female', nationality=nationality)
            break
        except ValueError as e:
            print(f"{bad} {e}")
            import time; time.sleep(1)
    _scayid_full_output(person, output_format)

def simpleinfogatherfemalewithprofession(profession, nationality=None, output_format='txt'):
    while True:
        try:
            person = Person(target_gender='female', nationality=nationality)
            break
        except ValueError as e:
            print(f"{bad} {e}")
            import time; time.sleep(1)
    person.occupation = profession
    _scayid_full_output(person, output_format)

def simplewithprofession(profession, nationality=None, output_format='txt'):
    while True:
        try:
            person = Person(nationality=nationality)
            break
        except ValueError as e:
            print(f"{bad} {e}")
            import time; time.sleep(1)
    person.occupation = profession
    _scayid_full_output(person, output_format)
