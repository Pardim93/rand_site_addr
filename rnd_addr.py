import random, socket, struct, mechanize
from selenium import webdriver

def search_addr(br):

    addr = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    print(addr)
    try:
        br.open('http://'+addr)
        print(br.title())
    except:
        print('Site não encontrado.')

def main():

    br = mechanize.Browser()

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0')]

    search_addr(br)


if __name__ == "__main__":
    main()
