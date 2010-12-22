# -*- coding: utf-8 -*-
from zope.interface import Interface, Attribute
from zope.publisher.interfaces.browser import IBrowserView
from plonetheme.classic.browser.interfaces import IThemeSpecific as IClassicTheme

class IThemeSpecific(IClassicTheme):
    """theme-specific layer"""
