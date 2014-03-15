# coding=UTF-8

import os.path
import sys

from optparse import OptionParser

import polib


def mangle(template_path, result_path):
    po = polib.pofile(template_path)

    # Some metadata values may break things
    po.metadata[u"Plural-Forms"] = "nplurals=2; plural=(n != 1);"

    for entry in po:
        translation = entry.msgid
        insert = len(translation) // 2
        translation = translation[:insert] + u"👊" + translation[insert:]
        entry.msgstr = translation

    po.save(result_path)


def add_to_linguas(result):
    folder = os.path.dirname(result)
    lingua = os.path.basename(result)

    if not lingua.endswith(".po"):
        print >> sys.stderr, "Can't add non-.po file to LINGUAS"
        return
    lingua = lingua[:-3]

    with open(os.path.join(folder, "LINGUAS"), "a+b") as f:
        linguas = f.read().splitlines()
        if lingua not in linguas:
            f.write(lingua + "\n")


def main():
    parser = OptionParser()
    parser.add_option("-l", "--linguas", dest="add_linguas",
                      action="store_true",
                      help="Add the resulting file to LINGUAS, if it exists")
    options, args = parser.parse_args()

    if len(args) != 2:
        parser.error("need a source and a destination filename")

    template, result = [os.path.abspath(a) for a in args]

    mangle(template, result)

    if options.add_linguas:
        add_to_linguas(result)


if __name__ == '__main__':
    main()
