from zope.interface import Interface, Attribute
from plonetheme.classic.browser.interfaces import IThemeSpecific as IClassicTheme


class IThemeSpecific(IClassicTheme):
    """theme-specific layer"""


class ITopicsProvider( Interface ):
    u"""The browser views implementing this interface have for mission
    to retrieve a list of categories with all the linked infos from the
    adapted object.
    """
    def get_categories_info(categories):
        u"""Returns a list of dict representing a category.
        The dict contains 3 strings : title, url and id.
        @params : iterable of category ids
        """

    def get_country_info(countries):
        u"""Returns a list of dict representing a country.
        The dict contains 3 strings : title, url and id.
        @params : iterable of country ids
        """

    __parent__ = Attribute(
        """The view the provider appears in.

        The view is the third discriminator of the content provider. It allows
        that the content can be controlled for different views.

        Having it stored as the parent is also very important for the security
        context to be kept.
        """)
