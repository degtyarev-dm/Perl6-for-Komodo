# Komodo Perl6 language service.

import logging
from koUDLLanguageBase import KoUDLLanguage


log = logging.getLogger("koPerl6Language")
log.setLevel(logging.DEBUG)


def registerLanguage(registry):
    log.debug("Registering language Perl6")
    registry.registerLanguage(KoPerl6Language())


class KoPerl6Language(KoUDLLanguage):
    name = "Perl6"
    lexresLangName = "Perl6"
    _reg_desc_ = "%s Language" % name
    _reg_contractid_ = "@activestate.com/koLanguage?language=%s;1" % name
    _reg_clsid_ = "788033f0-84c1-4a24-b6ed-08067e4bda3b"
    defaultExtension = '.p6'
    lang_from_udl_family = {
                            'SSL': 'Perl6',
                            }

