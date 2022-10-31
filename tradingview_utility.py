import time
from selenium.webdriver import ChromeOptions
from helium import (
    start_chrome,
    kill_browser,
    click,
    write,
    press,
    go_to,
    wait_until,
    refresh,
    Text,
    Button,
    S,
    ENTER,
    BACK_SPACE,
)


LONG = 1.5
MED = 0.5
SHORT = 0.5
LOAD = 5


class TDV_utlit:

	def Download_path(download_dir: str='./'):
		options = ChromeOptions()
		options.add_argument("window-size=1920,1080")
		chrome_prefs = {"download.default_directory": download_dir}
		options.add_experimental_option("prefs", chrome_prefs)
		return options

	def Sign_in(username: str='xxxxxxx@gmail.com',
				password: str='ooooooo',
				options=None):

		url='https://www.tradingview.com/'	
		start_chrome(url, options=options)
		time.sleep(LONG)

		click("open user menu")
		click("Sign in")
		click("Email")
		write(username, into="Username or Email")
		write(password, into="Password")
		click("Sign in")
		print("#-------- Log In OK --------#")
		time.sleep(LONG)

		go_to('https://www.tradingview.com/chart/')
		time.sleep(LONG)

		click("Accept All")
		time.sleep(SHORT)

	def Search_asset(asset: str):
		click(S("#header-toolbar-symbol-search"))
		time.sleep(LONG)
		write(asset, into="Symbol Search")
		time.sleep(SHORT)
		click(asset)
		#press(ENTER)

		time.sleep(LONG)

	def Scroll_to_Date(date: str = "20200101"):
        # date = YYYYMMDD
		# set time interval to 1 day
		click(S("#header-toolbar-intervals"))
		click("1 day")

		# Scroll to date
		click(S(".icon-YC6a1zPj"))
		time.sleep(LONG)
		for i in range(10):
			press(BACK_SPACE)
			time.sleep(SHORT)
        
		for char in list(date):
			press(char)
			time.sleep(SHORT)

		press(ENTER)
		time.sleep(LOAD)

	def Download_CSV():
		click(S(".arrow-fATUMGKH"))
		time.sleep(SHORT)
		
		click("Export chart data")
		time.sleep(SHORT)

		click("Export")
		time.sleep(MED)


	def Close_Browser():
		kill_browser()
