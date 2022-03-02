import os
import shutil
from typing import Dict, List, Tuple, Union

from .. import definitions as DD


def save_xsd(contents: Union[str, bytes], filename: str) -> None:
    return _save_contents(contents, filename, DD.DIR_OUTPUT_XSD)


def save_finding(contents: Union[str, bytes], filename: str) -> None:
    return _save_contents(contents, filename, DD.DIR_OUTPUT_FINDINGS)


def save_assertions(assertions: Dict[str, List[str]]) -> None:
    contents = ""
    for k, v in assertions.items():
        contents += k+"\n"
        contents += "=" * len(k) + "\n"
        contents += "\n".join(v)
        contents += "\n\n"
    return _save_contents(contents, DD.FILENAME_ASSERTIONS, DD.DIR_OUTPUT_FINDINGS)


def enumerate_xsds() -> Tuple[str, List[str]]:
    d = os.path.join(_get_parent_output_dir(),  DD.DIR_OUTPUT_XSD)

    path_genexpr = ((fn, os.path.join(d, fn)) for fn in os.listdir(d)
                    if fn.upper().endswith(".XSD"))

    for filename, path in path_genexpr:
        f = open(path, "rt", encoding="utf-8")
        contents = f.readlines()
        f.close()
        yield (filename, contents)


def clean_fs() -> None:
    d = _get_parent_output_dir()
    if os.path.exists(d) and os.path.isdir(d):
        shutil.rmtree(d)


def _save_contents(contents: Union[str, bytes], filename: str, output_dir: str) -> None:
    d = os.path.join(_get_parent_output_dir(), output_dir)
    _create_dir_if_needed(d)

    f = os.path.join(d, filename)
    flags = _get_flags(contents)
    encoding = _get_encoding(contents)
    with open(f, flags, encoding=encoding) as f:
        f.write(contents)


def _get_parent_output_dir() -> str:
    d = os.path.join(DD.DIR_HERE, DD.DIR_OUTPUT_BASE)
    return d


def _create_dir_if_needed(d: str) -> None:
    if not os.path.exists(d) or not os.path.isdir(d):
        os.makedirs(d)


def _get_flags(contents: Union[str, bytes]) -> str:
    return "wt" if type(contents) == str else "wb"


def _get_encoding(contents: Union[str, bytes]) -> Union[str, None]:
    return "utf-8" if type(contents) == str else None
