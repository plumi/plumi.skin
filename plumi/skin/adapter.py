from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_author_paypal(self):
        return self.context.getProperty('author_paypal', '')
    def set_author_paypal(self, value):
        return self.context.setMemberProperties({'author_paypal': value})
    author_paypal = property(get_author_paypal, set_author_paypal)
