from typing import Dict, List
from ... import definitions as DD
from ..web import scrapper as web_scrapper
from ...filesystem import helper as fs


def extract_assertions(persist: bool = True, debug: bool = False) -> Dict:
    assertions = {}
    for filename, xsd_lines in fs.enumerate_xsds():
        matches = _parse_xsd(xsd_lines)
        if matches:
            assertions[filename] = matches
            if debug:
                print(filename)
                print("*" * len(filename))
                for m in matches:
                    print(f"---> {m}")
    if persist:
        fs.save_assertions(assertions)
    return assertions 

def _parse_xsd(xsd_lines: str) -> List[str]:
    valid_lines = [l.strip() for l in xsd_lines if "xs:assert test" in l]
    return valid_lines
