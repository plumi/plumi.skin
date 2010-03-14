from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from collective.plonebookmarklets.browser.viewlets import BookmarkletsActionsViewlet as BAViewlet

class BookmarkletsActionsViewlet(BAViewlet):
    render = ViewPageTemplateFile("templates/document_actions.pt")
