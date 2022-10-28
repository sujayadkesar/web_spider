from web_spider import banner
from web_spider import get_user_inputs
from web_spider import domain_ip
from web_spider import Process_request
from web_spider import find_all_links


def main():
    banner()
    get_user_inputs()
    domain_ip()
    Process_request()
    find_all_links()


main()
