# Komodo Perl6 language service.

import logging
from koXMLLanguageBase import koXMLLanguageBase


log = logging.getLogger("koPerl6Language")
log.setLevel(logging.DEBUG)


def registerLanguage(registry):
    log.debug("Registering language Perl6")
    registry.registerLanguage(KoPerl6Language())


class KoPerl6Language(koXMLLanguageBase):
    name = "Perl6"
    lexresLangName = "Perl6"
    _reg_desc_ = "%s Language" % name
    _reg_contractid_ = "@activestate.com/koLanguage?language=%s;1" % name
    _reg_clsid_ = "788033f0-84c1-4a24-b6ed-08067e4bda3b"
    defaultExtension = '.p6'
    lang_from_udl_family = {
                            'M': 'HTML',
                            'SSL': 'Perl6',
                            }

    #TODO: Update 'lang_from_udl_family' as appropriate for your
    #      lexer definition. There are four UDL language families:
    #           M (markup), i.e. HTML or XML
    #           CSL (client-side language), e.g. JavaScript
    #           SSL (server-side language), e.g. Perl, PHP, Python
    #           TPL (template language), e.g. RHTML, Django, Smarty
    #      'lang_from_udl_family' maps each UDL family code (M,
    #      CSL, ...) to the sub-langauge name in your language.
    #      Some examples:
    #        lang_from_udl_family = {   # A PHP file can contain
    #           'M': 'HTML',            #   HTML
    #           'SSL': 'PHP',           #   PHP
    #           'CSL': 'JavaScript',    #   JavaScript
    #        }
    #        lang_from_udl_family = {   # An RHTML file can contain
    #           'M': 'HTML',            #   HTML
    #           'SSL': 'Ruby',          #   Ruby
    #           'CSL': 'JavaScript',    #   JavaScript
    #           'TPL': 'RHTML',         #   RHTML template code
    #        }
    #        lang_from_udl_family = {   # A plain XML can just contain
    #           'M': 'XML',             #   XML
    #        }
