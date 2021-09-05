import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import itertools
import threading
import sys
from playsound import playsound
import os



checker = ("1,000.00")
valuelist = ["0","1","2","3","4"]
goldenValue = "0" 
firstFour = True #check whether 4 list slots are filled with the old values
firstFourCounter = 0
shouldSound = False

# LOADING ANIMATION__________________________________________________
done = False



#Sound output




print(" ")
print("\033[1;30;46m   B.I.T.C.H. : BINARY INVESTMENT TECHNICALLY CALIBERATED HELPER   ")
print("\033[0;37;0m           v1.01 Alpha    |     2020     |      navintc")
print("")


# def notifysound():

#     while (True):

#         if shouldSound:
#             playsound(os.path.join(sys.path[0], 'sound.mp3'))
#             shouldSound = False


# notifysoundThread = threading.Thread(target=notifysound)
# notifysoundThread.start()
# shouldSound = True








#here is the animation
def animate():
    print ("..................................................................")
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rSetting Up..  ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    print(' ')
    print(' ')
    print('\033[0;32;40mSetting Up Complete! \n')
    print(' ')
# LOADING ANIMATION___________________________________________________





# LOADING ANIMATION START__________
loadanimationThread = threading.Thread(target=animate)
loadanimationThread.start()


driver = webdriver.Chrome(os.path.join(sys.path[0], 'chromedriver.exe'))  # findin the chromedrive.
driver.get("https://oauth.binary.com/oauth2/authorize?app_id=1&l=EN&signup_device=desktop") #goes to the login page

#opens the file credentials
f=open(os.path.join(sys.path[0], "credentials.txt"), "r")
contents = f.read()

#splitting data
email, slash, password = contents.partition('/')
print("")
print("\033[0;35;40m Loggin in to {} with '{}'. " .format(email, password) )
print("\033[0;37;40m")

#inserting login data in to the page
driver.find_element_by_id("txtEmail").send_keys(email)
driver.find_element_by_id("txtPass").send_keys(password)
link1 = driver.find_element_by_name("login")
link1.click()



time.sleep(4) # let the page to load



driver.get("https://www.binary.com/en/trading.html?currency=USD&market=synthetic_index&underlying=R_100&formname=matchdiff&duration_amount=1&duration_units=t&amount=10&amount_type=stake&expiry_type=duration&prediction=0")
time.sleep(4) # let the page to load

print("\033[0;31;40mSuccessfully Logged in.")
print("")



# LOADING ANIMATION END______________
done = True

#patience bro
time.sleep(1)


print("\033[0;32;40mSpot checker is Activated.")
print("\033[0;37;0m")
print ("..................................................................")
print (" ")

shouldSound = True





#Actual Work------------------------------------------------------------------------------------------------------------------------------------------------------
while (True):

    spot_box = driver.find_element_by_id("spot")
    spot_value = spot_box.get_attribute('innerHTML')

    #checks wheather the spot has been changed lately since its frequency can be changed from time to time
    if (checker != spot_value):
        #arranges the list in a symphony
        valuelist[0] = valuelist [1]
        valuelist[1] = valuelist [2]
        valuelist[2] = valuelist [3]
        valuelist[3] = valuelist [4]
        #takes in the last digit
        last_digit = spot_value[-1:]
        #inserts the new digit in to the list
        valuelist[-1:] = last_digit

        print (valuelist)

        if ((valuelist[0] == valuelist[1]) and (firstFour==False)):
            
            if (valuelist[1] == valuelist[2]):
                
                if (valuelist[2] == valuelist[3]):

                    if (valuelist[3] == valuelist[4]):
                            
                        #takes in the last digit to a variable
                        goldenValue = valuelist[4]

                        #clicks on the drop list
                        driver.find_element_by_xpath("(//div[@class='select-dropdown'])[position()=3]").click()
                        #aims to the 9th value
                        lastdigitWebElement = driver.find_element_by_xpath("//li[@data-value='{}']".format(goldenValue))
                        #clicks on the aimed value
                        driver.execute_script("arguments[0].click();", lastdigitWebElement)
                        driver.find_element_by_id("purchase_button_bottom").click()

                        #just some funky stuff
                        
                        print(" ")
                        print ("\033[1;30;42m High win probability spot sequence identified.")
                        print("\033[0;31;40m ")
                        print("Purchased a spot")
                        print("\033[0;37;0mContinuing the Spot checker")
                        print(" ")

        #looks whether the list is filled with fresh values
        firstFourCounter += 1
        if firstFourCounter == 5 :
            firstFour = False

        
    #assigns the in-came spot as the last spot to the checker
    checker = spot_value 

    # time.sleep(1)

















