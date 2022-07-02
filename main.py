from hgc.scrapping.web import scrapper as web_scr
from hgc.scrapping.assertions import scrapper as ass_scr
from hgc.filesystem import helper as fs


def main():
    print("cleaning the directory...")
    fs.clean_fs()
    print("fetching the main page...")
    web_scr.get_main_page()
    print("scrapping the xsd_urls...")
    web_scr.get_xsd_urls()
    print("fetching the xsds...")
    web_scr.get_xsds()
    print("extracting assertions from xsds...")
    ass_scr.extract_assertions()


if __name__ == "__main__":
    main()

