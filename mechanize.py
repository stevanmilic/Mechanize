browser = mechanize.Browser()
browser.set_handle_robots(False)

def checkLogin(url,formLogin,formPass,username,password):
	browser.open(url)
	print browser.geturl()
	browser.select_form(nr=0)
	browser.form[formLogin] = username
	browser.form[formPass] = password
	browser.submit()
	print browser.geturl()
