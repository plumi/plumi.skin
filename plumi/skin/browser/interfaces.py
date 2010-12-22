# -*- coding: utf-8 -*-
from z3c.form import interfaces
from zope import schema
from zope.interface import Interface, Attribute
from zope.publisher.interfaces.browser import IBrowserView
from zope.i18nmessageid import MessageFactory
from plonetheme.classic.browser.interfaces import IThemeSpecific as IClassicTheme

_ = MessageFactory('plumi.skin')

class IThemeSpecific(IClassicTheme):
    """theme-specific layer"""

class IPlumiSettings(Interface):
    """Global plumi settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    private_favorites = schema.Bool(title=_(u"Private Favourites"),
                                  description=_(u"help_private_favourites",
                                                default=u"Select if you wish members favorites "
                                                         "folders to be private."),
                                  required=False,
                                  default=False,)

