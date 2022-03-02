from hgc.scrapping.web import scrapper as web_scr
from hgc.scrapping.assertions import scrapper as ass_scr
from hgc.filesystem import helper as fs


def main():
    fs.clean_fs()
    web_scr.get_main_page()
    web_scr.get_xsd_urls()
    web_scr.get_xsds()
    ass_scr.extract_assertions()


if __name__ == "__main__":
    main()
