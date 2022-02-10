# import datetime
# from flask import current_app as app
# import requests
# from bs4 import BeautifulSoup
# from flask_sqlalchemy import SQLAlchemy
# # from gettext import find
# # from send_message import send_email

# with app.app_context() as app:
#     db = SQLAlchemy(app)

# class Pricing(db.Model):
#     __tablename__ = "pricing"
#     id = db.Column(db.Integer, primary_key = True)
#     product_title = db.Column(db.VARCHAR(512))
#     email = db.Column(db.VARCHAR(512))
#     product_url = db.Column(db.VARCHAR(512))
#     initial_price = db.Column(db.Numeric(7,2))
#     created = db.Column(db.DateTime)
#     last_checked = db.Column(db.DateTime)

#     def __init__(self, email, product_url, initial_price, product_title, created = datetime.datetime.now(), last_checked = datetime.datetime.now()):
#         self.email = email
#         self.product_url = product_url
#         self.product_title = product_title
#         self.created = created
#         self.initial_price - initial_price

# def initial_scrape(prodlink):
#     # headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
#     headers = {
#         'authority': 'www.amazon.com',
#         'pragma': 'no-cache',
#         'cache-control': 'no-cache',
#         'dnt': '1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'none',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-dest': 'document',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     }
    
#     page = requests.get(prodlink, headers=headers)
#     bs = BeautifulSoup(page.content, 'html.parser')

#     product_title = bs.find(id="productTitle").get_text()
#     product_price = bs.find('span', attrs={"class": "apexPriceToPay"}).find('span').get_text()
    
#     if product_price == None:
#         product_price = bs.find('span', attrs={"class": "priceToPay"}).find('span').get_text()
    
#     product_price.replace("$", "")
#     product_price.replace(",", "")

#     return {'title': product_title, 'price': product_price}

# def run_price_check():
#     while True:
#         # send_email('burjiss@gmail.com', 'testlink', '20.00')
#         # Get all checks that are more than 12 hours old
#         # check_time = datetime.now() - datetime.timedelta(hours = 12)

#         # result = Pricing.query.filter_by('last_checked' < check_time).limit(20).all()

#         check_time = datetime.datetime.now() - datetime.timedelta(hours = 12)
#         # result = Pricing.query.filter_by(Pricing.last_checked < check_time).limit(20).all()
#         # print(result)
        
#         datetime.time.sleep(7200)
    
#     return 'Nothing'

# # Run price check if coming in from cron
# # if __name__ == '__main__':
# #     run_price_check()