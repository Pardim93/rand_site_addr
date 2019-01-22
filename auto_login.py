# import mechanize, re, urllib
# br = mechanize.Browser()
# # br.open('http://localhost:3000/articles')
# br.open('http://localhost:3000/articles')
# # agent = mechanize.new
#
# params = {'name': 'dhh', 'password':'secret'}
# data = urllib.parse.urlencode(params)
# # request  = mechanize.Request('http://localhost:3000/articles/new')
# # response = mechanize.urlopen(request,data)
# # print(dir(response.read()))
# # payload = {'username': 'dhh', 'password': 'secret'}
# br.find_link(text='New article')
# # r = mechanize.Request(url='http://localhost:3000/articles', data=payload, headers=payload)
# # print(r.visit)
# # print (dir(r))
#
# # print (r.data())
# req = br.click_link(text='New article')
# req.set_data(data)
# print(br.open(req))
#
# #print (br.response().read())
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\webbrowser\chromedriver.exe')
browser.get('localhost:3000/articles')
browser.find_element_by_link_text('New article').click()
print(dir(browser))

# browser.send_key("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# browser.send_key("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
