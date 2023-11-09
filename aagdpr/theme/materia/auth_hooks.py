from urllib.parse import urljoin

from django.conf import settings

from allianceauth import hooks
from allianceauth.theme.hooks import ThemeHook


class MateriaThemeHook(ThemeHook):
    """
    Bootswatch Materia Theme
    https://bootswatch.com/materia/
    """

    def __init__(self):
        ThemeHook.__init__(
            self,
            "Materia",
            "Material is the metaphor (AA-GDPR)",
            css=[{
                "url": urljoin(settings.STATIC_URL, 'aagdpr/ajax/libs/bootswatch/5.3.2/materia/bootstrap.min.css'),
                "integrity": "FQVjsLzp4glZLzSSBQJt5e3j1cFwHg7H3m2ukfXWH4AShnnCjdKMCPCpxfPREhQsQv34a9E0IfiC5Z0ZKgakDw=="
            }],
            js=[{
                "url": urljoin(settings.STATIC_URL, 'aagdpr/ajax/libs/popper.js/2.11.8/umd/popper.min.js'),
                "integrity": "sha512-TPh2Oxlg1zp+kz3nFA0C5vVC6leG/6mm1z9+mA81MI5eaUVqasPLO8Cuk4gMF4gUfP5etR73rgU/8PNMsSesoQ=="
            }, {
                "url": urljoin(settings.STATIC_URL, 'aagdpr/ajax/libs/bootstrap/5.3.2/js/bootstrap.min.js'),
                "integrity": "sha512-WW8/jxkELe2CAiE4LvQfwm1rajOS8PHasCCx+knHG0gBHt8EXxS6T6tJRTGuDQVnluuAvMxWF4j8SNFDKceLFg=="
            }],
            header_padding="5.25em"
        )


@hooks.register('theme_hook')
def register_materia_hook():
    return MateriaThemeHook()
