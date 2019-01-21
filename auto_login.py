import mechanize, re

br = mechanize.Browser()
br.open("localhost:3000")
response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
print(br.title())
print(response1.geturl())
print(response1.info())  # headers
print(response1.read())  # body

#br.select_form(name="order")
