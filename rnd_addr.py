import random, socket, struct, threading
import requests, bs4, logging

# Global var
found_site = None

def search_addr():
    addr = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    # Google IP for testing
    # addr = '172.217.28.228'
    try:
        r = requests.get('http://'+addr)
        html = bs4.BeautifulSoup(r.text,features="html5lib")
        logging.debug(html.title.text)
    except:
        logging.debug('IP: ' +addr + ' - Not reachable.')

def main():
    threads = []
    logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

    for i in range(4):
        t = threading.Thread(target=search_addr)
        threads.append(t)
        t.start()


    # search_addr(headers)


if __name__ == "__main__":
    main()
