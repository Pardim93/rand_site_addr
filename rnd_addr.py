import random, socket, struct, threading
import requests, bs4, logging, argparse
# Globals
found_site_event = threading.Event()
sites = []
ip_args = 1

def write_found_sites():
    with open('found_sites.txt', 'a') as file:
        for site in sites:
            file.write("%s\n" % site)

def search_addr():
    while not found_site_event.is_set():
        addr = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
        # Google IP for testing
        # addr = '172.217.28.228'
        try:
            r = requests.get('http://'+addr)
            html = bs4.BeautifulSoup(r.text,features="html5lib")
            logging.debug(html.title.text +' - '+ addr)
            sites.append(addr)
            if len(sites) >= ip_args:
                found_site_event.set()
        except:
            logging.debug('IP: ' +addr + ' - Not reachable.')


def set_search_threads(thread_args, ip_args):
    threads = []
    logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

    for i in range(thread_args):
        t = threading.Thread(target=search_addr)
        threads.append(t)
        t.start()

    logging.debug(sites)

def main():
    # config parser
    parser = argparse.ArgumentParser(description='Get random accessible IP addresses (Port 80).')
    parser.add_argument('--threads',  default=1, type=int, help='Amount of threads (default = 1)')
    parser.add_argument('--ip' , default=1, type=int, help='Amount of IP to find (default = 1)')

    args = parser.parse_args()
    thread_args, ip_args =  args.threads, args.ip
    set_search_threads(thread_args, ip_args)

    found_site_event.wait()
    write_found_sites()

if __name__ == "__main__":
    main()
