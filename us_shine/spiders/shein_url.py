# flake8: noqa
import time
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


class SheinUrlSpider(scrapy.Spider):
    name = "shein_url"
    allowed_domains = ["us.shein.com"]
    # start_urls = ["https://us.shein.com"]
    
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service)
    
    start_urls = [
            "https://us.shein.com/new/Plus-Tops-New-In-15-Days-sc-00211498.html?adp=40630796&categoryJump=true&ici=us_tab00navbar01menu02dir03&src_identifier=fc%3DAll%60sc%3DNew%20In%60tc%3DNew%20In%20Curve%20Clothing%60oc%3DTops%60ps%3Dtab00navbar01menu02dir03%60jc%3DitemPicking_00211498&src_module=topcat&src_tab_page_id=page_select_class1725546343756",
            "https://us.shein.com/new/New-In-Curve-Dresses-sc-00203657.html?adp=41059320&categoryJump=true&ici=us_tab01navbar01menu02dir02&src_identifier=fc%3DNew%20In%60sc%3DNew%20In%60tc%3DNew%20In%20Curve%20Clothing%60oc%3DDresses%60ps%3Dtab01navbar01menu02dir02%60jc%3DitemPicking_00203657&src_module=topcat&src_tab_page_id=page_home1725546333193",
            "https://us.shein.com/new/New-In-Curve-Blouses-sc-00203667.html?adp=40660063&categoryJump=true&ici=us_tab01navbar01menu02dir04&src_identifier=fc%3DNew%20In%60sc%3DNew%20In%60tc%3DNew%20In%20Curve%20Clothing%60oc%3DBlouses%60ps%3Dtab01navbar01menu02dir04%60jc%3DitemPicking_00203667&src_module=topcat&src_tab_page_id=page_select_class1725546378096",
            "https://us.shein.com/new/New-In-Curve-Tees-sc-00203666.html?adp=40065370&categoryJump=true&ici=us_tab00navbar01menu02dir05&src_identifier=fc%3DAll%60sc%3DNew%20In%60tc%3DNew%20In%20Curve%20Clothing%60oc%3DT-shirts%60ps%3Dtab00navbar01menu02dir05%60jc%3DitemPicking_00203666&src_module=topcat&src_tab_page_id=page_select_class1725546579535"
        ]
    dataset = {}
    def parse(self, response, **kwargs):
        
        self.driver.get(response.url)
        
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sui-pagination__next sui-pagination__btn"))
        )
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, ".product-card"))
        )
        time.sleep(5)
        html_content = self.driver.page_source
        
        response_ = HtmlResponse(url=response.url, body=html_content, encoding='utf-8')
        
        product_cards = response_.css('.product-card')
        
        if product_cards:
            c = 1