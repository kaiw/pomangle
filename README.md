pomangle
========

Mangle .po files, because there's never enough UnicodeDecodeErrors to go around

This script doesn't do anything exciting; it just inserts stupid emoji into the
middle of every message in a `.po` file. The goal of this is just to test
places where Python's gettext isn't returning a unicode string, or where you're
incorrectly composing non-unicode gettext-ed strings.


Using
-----

As much as I'd like to be running with `en_WIBBLE`, Python will complain if
you don't give it a valid locale, so just use something sensible that no one
ever bothers to translate for:

    python pomangle.py project.pot en_AU.po

If you have a LINGUAS file in the same directory as your new `.po` file,
passing the `-l` flag will add your new lingua there as well.

Now, just build your `.mo` files and run with your new setting, and before
long you'll be in UnicodeDecodeError heaven.
