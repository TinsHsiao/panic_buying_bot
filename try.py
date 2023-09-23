from calendar import month
from errno import ENETRESET
from inspect import isframe
from nturl2path import url2pathname
from pickle import FALSE
from turtle import goto
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import urllib.request as req
import tkinter as tk
import tkinter.messagebox as msg
import bs4, re
import time



driver = webdriver.Chrome()
driver.get('https://www.goopi.co/users/sign_in')
driver.find_element_by_xpath("/html/body/div[8]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/a/span").click()

def goopi_login() :
    element = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[8]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/a/span')))
    driver.find_element_by_xpath( "/html/body/div[8]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/a/span" ).click()
    account = driver.find_element_by_xpath( '//*[@id="email"]').send_keys("account")
    pas = driver.find_element_by_xpath( '//*[@id="pass"]').send_keys("passeord")
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()


def goopi() :
    url = driver.current_url 
    request = req.Request(url, headers={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response :
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data, "html.parser")
    #element = root.find( text=re.compile('CentralPark.4PM - C-TEX Pocket Tee - Black') )
    #soup = BeautifulSoup(urllib2.urlopen("https://play.google.com/store/apps/details?id=com.wetter.androidclient&hl=de"))
    #result = root.find_all("div", {"class":"Oldsoil - OLDSOILMAG 1"})
    driver.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/form').click()
    driver.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/form/input').send_keys('(A).03G - “DUET” D-L So Wide Tee - Black')
    driver.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/form/input').send_keys(Keys.ENTER)
    driver.find_element_by_partial_link_text('(A).03G - “DUET” D-L So Wide Tee - Black').click()
    select = Select(driver.find_element_by_xpath('/html/body/div[7]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/div[2]/select'))
    select.select_by_visible_text("1號") # 尺寸
    #driver.find_element_by_xpath('/html/body/div[7]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div/span[2]/button').click() # 數量
    driver.find_element_by_xpath('//*[@id="#btn-variable-buy-now"]').click()

    driver.get('https://www.goopi.co')
    driver.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/form').click()
    driver.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/form/input').send_keys('(A).03G - “DUET” D-L So Wide Tee - White')
    driver.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/form/input').send_keys(Keys.ENTER)
    driver.find_element_by_partial_link_text('(A).03G - “DUET” D-L So Wide Tee - White').click()
    select = Select(driver.find_element_by_xpath('/html/body/div[7]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[1]/div[2]/select'))
    select.select_by_visible_text("size") # 尺寸
    #driver.find_element_by_xpath('/html/body/div[7]/div[1]/div/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/div/span[2]/button').click() # 數量
    driver.find_element_by_xpath('//*[@id="#btn-variable-buy-now"]').click()

    #driver.find_element(By.LINK_TEXT, "https://www.goopi.co/checkoutt").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="checkout-container"]/div/div[3]/div[4]/div[2]/section/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="order-customer-phone"]').clear()
    driver.find_element_by_xpath('//*[@id="order-customer-phone"]').send_keys('phone number')
    driver.find_element_by_xpath('//*[@id="user-field-598198f2d4e395db79000a21"]').clear()
    driver.find_element_by_xpath('//*[@id="user-field-598198f2d4e395db79000a21"]').send_keys('account')
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="delivery-form-content"]/div[1]/label').click()
    driver.implicitly_wait(1)


    driver.find_element_by_xpath('//*[@id="seven-eleven-address"]/div/div').click()
    #driver.find_element_by_xpath('//*[@id="seven-eleven-address"]/div/div[2]').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="byName"]/a').click()
    iframe1 = driver.find_element_by_tag_name("iframe")
    driver.switch_to_frame(iframe1)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/ul/li/div').click()
    driver.find_element_by_xpath('//*[@id="storeNameKey"]').send_keys('7-11門市')
    driver.find_element_by_xpath('//*[@id="send"]').click()


    
    #iframe2 = driver.find_element_by_tag_name("iframe")
    #driver.switch_to_frame(iframe2)
    driver.find_element_by_xpath('//*[@id="ol_stores"]/li[1]/p').click()
    driver.switch_to_default_content()
    driver.find_element_by_xpath('//*[@id="sevenDataBtn"]').click()
    driver.find_element_by_xpath('//*[@id="AcceptBtn"]').click()
    driver.find_element_by_xpath('//*[@id="submit_butn"]').click()
    #driver.find_element_by_xpath("//label[contains(text(), '卡號')]").click()
    iframe2 = driver.find_elements_by_tag_name("iframe")
    driver.switch_to_frame(iframe2[0])
    driver.find_element_by_xpath('//*[@id="input-file"]').send_keys('卡號')
    driver.switch_to_default_content()
    driver.switch_to_frame(iframe2[1])
    driver.find_element_by_xpath('//*[@id="input-file"]').send_keys('name')
    driver.switch_to_default_content()
    driver.switch_to_frame(iframe2[2])
    driver.find_element_by_xpath('//*[@id="input-file"]').send_keys('到期日')
    driver.switch_to_default_content()
    driver.switch_to_frame(iframe2[3])
    driver.find_element_by_xpath('//*[@id="input-file"]').send_keys('安全碼')
    driver.switch_to_default_content()

    select = Select(driver.find_element_by_xpath('//*[@id="invoice-type"]'))
    select.select_by_visible_text("捐贈發票")
    driver.implicitly_wait(1)
    
    a = driver.find_element_by_xpath('//*[@id="checkout-container"]/div/div[5]/div[1]/form/div/label/input')
    driver.execute_script("arguments[0].click();", a) 
    driver.find_element_by_xpath('//*[@id="place-order-recaptcha"]').click()
    
    #driver.find_element_by_xpath('//*[@id="checkout-container"]/div/div[5]/div[1]/form/div/label').click()



goopi_login()
goopi()

"""

def habit() :
    driver2 = webdriver.Chrome()
    driver2.get('https://www.habitselect.com/users/61fe49688a4f690018bda26d/edit')
    driver2.find_element_by_xpath('//*[@id="Content"]/div/div/div/div/div/div/div/div[2]/div/div/form/div[1]/div/div/input').send_keys('tinahsiao900510@gmail.com')
    driver2.find_element_by_xpath('//*[@id="Content"]/div/div/div/div/div/div/div/div[2]/div/div/form/div[2]/div/div/input').send_keys('Th09550885311524')
    driver2.find_element_by_xpath('//*[@id="sign-in-btn"]').click()
    driver2.implicitly_wait(2)
    driver2.find_element_by_xpath('/html/body/nav[2]/div/ul/li[1]').click()
    driver2.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/form/input').send_keys('Grocery - Washed Invoice Pocket Tee - Olive')
    driver2.find_element_by_xpath('//*[@id="SearchPanel"]/div/input').send_keys('GOOPiMADE® - "FN-D6” FIDLOCK Label Combat Loop / SAND')
    time.sleep(100)


habit()

"""

"""
def sign_in() :
    i = 0 
    driver = webdriver.Chrome()
    driver.get('https://www.goopi.co/users/sign_in')
    driver.execute_script("window.open('https://www.goopi.co/users/sign_in')")
    driver.execute_script("window.open('https://www.goopi.co/users/sign_in')")
    driver.implicitly_wait(10)
    handles = driver.window_handles
    driver.switch_to.window(handles[0])

    while EC.element_to_be_clickable((By.CLASS_NAME, "btn btn-block btn-facebook-login")) == False :
        if i == -2 :
            i = 0
        else : 
            i -= 1 
        driver.switch_to.window(handles[i])
    driver.switch_to.window(handles[0])
    driver.implicitly_wait(10)
    driver.find_element(By.CLASS_NAME, "btn btn-block btn-facebook-login").click()
    #driver.find_element_by_xpath("/html/body/div[7]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div/a/span").is_displayed()


sign_in()
time.sleep(10)
#driver.get('https://www.goopi.co/users/sign_in')








#driver. ( "//div[text()='CentralPark.4PM - C-TEX Pocket Tee - Black']" ).click()
#print(Link_to_product)
#https://www.goopi.co/products/centralpark4pm-c-tex-pocket-tee-white
#https://www.goopi.co/products/centralpark.4pm-c-tex-pocket-tee-white



#Link_to_product = driver.find_element_by_link_text( str.lower() )
# print(Link_to_product)
#driver.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]').find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/form')
#driver.find_element_by_xpath('//*[@id="fixed-menu-container"]/div[2]/div[4]/formt').click()





#<span class="login-btn-label">使用Facebook登入</span>


"""
"""
url = "https://www.goopi.co/categories/newarrivals-new-arrivals"
request = req.Request(url, headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}) # 讓他知道我們用的瀏覽器與他的系統)

with req.urlopen(request) as response :
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")

win = tk.Tk()
win.title('Input介面')
win.geometry('800x600')
win.resizable(False, False)
name = tk.StringVar()
card = tk.IntVar()
month = tk.IntVar()
years = tk.IntVar()
secure = tk.IntVar()
brand = tk.StringVar()
product = tk.StringVar()

textname = tk.Label( win, text='姓名', font=('Arial', 8) ).place(x=0, y=0)
entryname = tk.Entry(win, textvariable=name, width=20).place(x=30, y=0)
textcard = tk.Label( win, text='卡號', font=('Arial', 8) ).place(x=0, y=30)
entrycard = tk.Entry(win, textvariable=card, width=20).place(x=30, y=30)
textmonth = tk.Label( win, text='月份', font=('Arial', 8) ).place(x=0, y=60)
entrymonth = tk.Entry(win, textvariable=month, width=20).place(x=30, y=60)
textyear = tk.Label( win, text='年分', font=('Arial', 8) ).place(x=0, y=90)
entryyear = tk.Entry(win, textvariable=years, width=20).place(x=30, y=90)
textbrand = tk.Label( win, text='品牌', font=('Arial', 8) ).place(x=0, y=120)
entrybrand = tk.Entry(win, textvariable=brand, width=20).place(x=30, y=120)
textproduct = tk.Label( win, text='品名', font=('Arial', 8) ).place(x=0, y=150)
entryproduct = tk.Entry(win, textvariable=product, width=20).place(x=30, y=150)
btn = tk.Button(win, text='顯示', command=go ).place(x=400, y=300) 
win.mainloop()
"""
