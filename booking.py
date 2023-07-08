import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import datetime
from selenium.webdriver.chrome.options import Options

def good(str):
    numbers = re.findall(r'\d+', str)
    alphabets = re.findall(r'[a-zA-Z]+', str)
    return (len(numbers)>0 and int(numbers[0])>=len(pe) and alphabets[0]=='AVAILABLE')
class P:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

def GetDate(Date,f):
    date_object = datetime.datetime.strptime(Date, "%d-%m-%Y")
    weekday = date_object.weekday()
    idx = (datetime.date.weekday(date_object))
    month = date_object.strftime("%b")
    full_name_month = date_object.strftime("%B")
    year = date_object.strftime("%Y")
    day = date_object.strftime("%d")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    Reqday = days[idx]
    Start_Date = Reqday + " " + month + " " + day + " " + year
    if(f==1) :req_month = full_name_month + " " + year
    else :req_month = full_name_month + year
    return Start_Date,req_month

def fname(name):
    idx = len(name)
    cnt=0
    for i in reversed(range(0,len(name))):
       if(name[i]==' '):
          idx=i
          break

    Fmname = name[0:(idx)]
    Lname = name[(idx+1):len(name)]
    return Fmname,Lname

def State(Pincode):
    val = int(Pincode[:3])
    pstates = {(121,131):"Haryana",
               (744,744):"Andaman and Nicobar",
               (110,110):"Delhi",
               (396,396):"Dadra and Nagar Haveli",
               (490,497):"Chhattisgarh",
               (781,788):"Assam",
               (790,792):"Arunachal Pradesh",
               (797,798):"Nagaland",
               (682,682): "Lakshadweep",
               (500,509): "Telangana",
               (737,737): "Sikkim",
               (700,743): "West Bengal",
               (813,835): "Jharkhand",
               (783,794): "Meghalaya",
               (751,770): "Odisha",
               (244,263): "Uttarakhand",
               (180,194): "Jammu and Kashmir",
               (799,799): "Tripura",
               (796,796): "Mizoram",
               (301,345): "Rajasthan",
               (795,795): "Manipur",
               (360,396): "Gujarat",
               (403,403): "Goa",
               (800,855): "Bihar",
               (507,535): "Andhra Pradesh",
               (560,591): "Karnataka",
               (362,396): "Daman and Diu",
               (400,445): "Maharashtra",
               (450,488): "Madhya Pradesh",
               (201,285): "Uttar Pradesh",
               (670,695): "Kerala",
               (140,160): "Chandigarh",
               (600,643): "Tamil Nadu",
               (533,673): "Puducherry",
               (140,160): "Punjab",
               (171,177): "Himachal Pradesh"
               }
    req_state=""
    for pair,state in pstates.items():
      if(pair[0]<=val and val<=pair[1]):
          req_state=state
          break
    if(req_state=="") :req_state = "Others"
    driver.find_element(By.ID,"dt_state_gst_info").click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[text()='{req_state}']"))).click()

type = ""
User_Name = ''
Pass = ''
Start_City = ""
End_City = ""
Start_Date = ""
Return_Date =""
pe = []
irctc = ''
Pincode = ''
Mobile = ""
pclass = ""

os.environ['PATH'] += r"C:/Users/MSI/Desktop/SeleniumFolders"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(options=options)
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
action = ActionChains(driver)



type = type.lower()
if (type == "t"): type = "railways"
if (type == "f"): type = "flights"
if(type=="railways"):driver.get(f"https://www.makemytrip.com/{type}/")
time.sleep(2)
action.click().perform()
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
if type == "flights":
    time.sleep(1)
    Start = driver.find_element(By.ID, "fromCity").click()
    time.sleep(1)
    xpath = "//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input"
    x1path = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/input"
    StartFill = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    StartFill.clear()
    StartFill.send_keys(Start_City)
    time.sleep(1)
    driver.find_element(By.ID, "react-autowhatever-1-section-0-item-0").click()
    End = driver.find_element(By.ID, "toCity").click()
    time.sleep(1)
    EndFill = wait.until(EC.element_to_be_clickable((By.XPATH, x1path)))
    EndFill.clear()
    EndFill.send_keys(End_City)
    time.sleep(1)
    driver.find_element(By.ID, "react-autowhatever-1-section-0-item-0").click()
else:
    Start = driver.find_element(By.ID, "fromCity")
    Start.click()
    xpath = f"//*[@title='From']"
    x1path = f"//*[@title='To']"
    StartFill = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    StartFill.clear()
    StartFill.send_keys(Start_City)
    time.sleep(1)
    driver.find_element(By.ID, "react-autowhatever-1-section-0-item-0").click()
    EndFill = wait.until(EC.element_to_be_clickable((By.XPATH, x1path)))
    EndFill.clear()
    EndFill.send_keys(End_City)
    time.sleep(1)
    driver.find_element(By.ID, "react-autowhatever-1-section-0-item-0").click()
    time.sleep(2)
#SELECTING DATES



Start_Date,req_month = GetDate(Start_Date,1)
for c in range(12):
    if(type=="railways"):curr_month = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div").text
    else:curr_month = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div").text
    if(curr_month==req_month):
        days2 = driver.find_elements(By.XPATH,"//*[@class='DayPicker-Day']")
        for i in days2:
            if i.get_attribute("aria-label")==(Start_Date):
                i.click()
                time.sleep(2)
                break
        break
    else:
        try : driver.find_element(By.CLASS_NAME,"DayPicker-NavButton--next").click()
        except:
            print("Enter A Valid Date")
            break
        time.sleep(1)

if(type!='railways' and Return_Date!=''):
    Return_Date,req_monthr = GetDate(Return_Date,0)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[4]").click()
    for c in range(12):
        curr_monthr = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div").text
        if (curr_monthr == req_monthr):
            days2 = driver.find_elements(By.XPATH, "//*[@class='DayPicker-Day']")
            for i in days2:
                if i.get_attribute("aria-label") == (Return_Date):
                    i.click()
                    time.sleep(2)
                    break
            break
        else:
            try:
                driver.find_element(By.CLASS_NAME, "DayPicker-NavButton--next").click()
            except:
                print("Enter A Valid Date")
                break
            time.sleep(1)

if(type=='railways'):
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/ul/li[1]").click()
    driver.find_element(By.CLASS_NAME, "widgetSearchBtn").click()
    wait.until(EC.element_to_be_clickable((By.ID,"quickFilter-available"))).click()
    cl = "journeyClassFilter-"+pclass
    wait.until(EC.element_to_be_clickable((By.ID,f"{cl}"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"customSelect"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH,f"//li[text()='Travel Time']"))).click()
    opt = driver.find_elements(By.CLASS_NAME,"availibilty-info")
    flag=0
    for i in range(len(opt)):
        str = opt[i].text
        if(good(str)):
            opt[i].click()
            flag=1
            break
    if(flag==0):
        print('Trains are not available as per your choice!')
        time.sleep(2)
        driver.quit()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='OK, GO AHEAD']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/section[1]/div[2]/div/ul/li[2]/div/span/label"))).click()
    tra = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/section[1]/div[3]/div[2]/div/a")))
    for i in range(len(pe)):
        tra.click()
        driver.find_element(By.ID,"name").send_keys(pe[i].name)
        driver.find_element(By.ID, "age").send_keys(pe[i].age)
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div/li/div[3]/div[2]/div/form/div[3]/div").click()
        if(pe[i].gender=='m') :wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[5]/div/div/div/li/div[3]/div[2]/div/form/div[3]/div/ul/li[1]"))).click()
        else: wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[5]/div/div/div/li/div[3]/div[2]/div/form/div[3]/div/ul/li[2]"))).click()
        driver.find_element(By.CLASS_NAME, "bluePrimarybtn").click()
        time.sleep(2)
    driver.find_element(By.ID,"irctcUserName").click()
    driver.find_element(By.ID, "IRCTCUserName").send_keys(irctc)
    driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[1]/div[2]/button/span").click()
    driver.find_element(By.ID,"contactEmail").send_keys(User_Name)
    driver.find_element(By.ID,"mobileNumber").send_keys(Mobile)
    time.sleep(2)
    pin = driver.find_element(By.ID,"pincode_gst_info")
    pin.clear()
    time.sleep(4)
    pin.send_keys(Pincode)
    time.sleep(2)
    State(Pincode)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,"checkboxWithLblWpr__label").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"paymentBtn").click()
else:
    child = []
    adults = []
    infants = []
    for i in  range(len(pe)):
        if(2<pe[i].age<12): child.append(pe[i])
        elif(pe[i].age>12): adults.append(pe[i])
        else: infants.append(pe[i])
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/label/p[1]/span").click()
    av = "adults-"+str(min(10,len(adults)))
    cv = "children-"+str(min(7, len(child)))
    iv = "infants-" + str(min(10, len(infants)))
    clv = "travelClass-"
    if(pclass=="pe") :clv +='1'
    elif pclass=="e":clv+='0'
    else:clv+='2'
    avpath = f"//*[@data-cy='{av}']"
    cvpath = f"//*[@data-cy='{cv}']"
    ivpath = f"//*[@data-cy='{iv}']"
    tpath = f"//*[@data-cy='travellerApplyBtn']"
    class_path = f"//*[@data-cy='{clv}']"
    driver.find_element(By.XPATH,avpath).click()
    driver.find_element(By.XPATH,cvpath).click()
    driver.find_element(By.XPATH,ivpath).click()
    driver.find_element(By.XPATH,class_path).click()
    driver.find_element(By.XPATH,tpath).click()
    driver.find_element(By.CLASS_NAME, "widgetSearchBtn").click()
    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div[2]/div/div/div[3]/button"))).click()
    time.sleep(1)
    mf = driver.find_elements(By.CLASS_NAME,"ViewFareBtn")
    if(len(mf)>0):
        mf[0].click()
        time.sleep(1)
    else:driver.find_element(By.CLASS_NAME,"buttonBig").click()
    time.sleep(2)
    book = driver.find_elements(By.CLASS_NAME,"corp-btn")
    if(len(book)==0):driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[3]/button").click()
    else : driver.find_element(By.CLASS_NAME,"corp-btn").click()
    time.sleep(5)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    opt = driver.find_elements(By.XPATH,"//*[@id='root']/div/div[2]/div[5]/div/div[2]/button")
    if(len(opt)!=0): opt[0].click()
    opt = driver.find_elements(By.XPATH,"//*[@id='INSURANCE']/div[3]/div[2]/label/div/p/span")
    if(len(opt)!=0): opt[0].click()
    try:
        wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='rtaImpinfo-consent']/div[1]/span/label/div/p/span"))).click()
    except:
        print('Booking!')
    time.sleep(2)
    for i in range (len(child)):
        eles = driver.find_elements(By.CLASS_NAME, "addTravellerBtn")
        eles[1].click()
        Fmname, Lname = fname(child[i].name)
        fn = driver.find_elements(By.CSS_SELECTOR, "[placeholder='First & Middle Name']")
        fn[i].send_keys(Fmname)
        ln = driver.find_elements(By.CSS_SELECTOR, "[placeholder='Last Name']")
        ln[i].send_keys(Lname)
        time.sleep(1)
        if (child[i].gender == 'm'):
            g = driver.find_elements(By.CSS_SELECTOR, "[value='MALE']")
        else:
            g = driver.find_elements(By.CSS_SELECTOR, "[value='FEMALE']")
        g[i].click()
        time.sleep(1)
    for i in range(len(adults)):
        eles = driver.find_elements(By.CLASS_NAME, "addTravellerBtn")
        eles[0].click()
        Fmname, Lname = fname(adults[i].name)
        fn = driver.find_elements(By.CSS_SELECTOR, "[placeholder='First & Middle Name']")
        fn[i].send_keys(Fmname)
        ln = driver.find_elements(By.CSS_SELECTOR, "[placeholder='Last Name']")
        ln[i].send_keys(Lname)
        time.sleep(1)
        if (adults[i].gender == 'm'):
            g = driver.find_elements(By.CSS_SELECTOR, "[value='MALE']")
        else:
            g = driver.find_elements(By.CSS_SELECTOR, "[value='FEMALE']")
        g[i].click()
        time.sleep(1)
    mob = driver.find_element(By.CSS_SELECTOR, "[placeholder='Mobile No']")
    mob.clear()
    mob.send_keys(Mobile)
    ema= driver.find_element(By.CSS_SELECTOR, "[placeholder='Email']")
    ema.clear()
    ema.send_keys(User_Name)
    time.sleep(2)
    pin = driver.find_element(By.CSS_SELECTOR,"[placeholder='Your Pincode']")
    pin.clear()
    pin.send_keys(Pincode)
    time.sleep(2)
    checkbox_xpath = "//*[@id='BILLING_ADDRESS']/div/div[3]/div/span"
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
    driver.execute_script("arguments[0].click();", checkbox)
    continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "extraPadBtn")))
    driver.execute_script("arguments[0].click();", continue_button)
    confirm_xpath = "//*[@id='root']/div/div[2]/div[5]/div/div[2]/button"
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, confirm_xpath)))
    driver.execute_script("arguments[0].click();", confirm_button)
    time.sleep(2)
    seats_xpath = "//*[@id='SEATS_N_MEALS']/div/div/div[1]/div/p[7]/button"
    seats_conf = wait.until(EC.element_to_be_clickable((By.XPATH, seats_xpath)))
    driver.execute_script("arguments[0].click();", seats_conf)
    driver.find_element(By.XPATH,"//*[@id='mainSection_1']/div[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='ACKNOWLEDGE_SECTION']/div/button").click()
print('Please enter your credentials on the website')
