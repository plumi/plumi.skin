from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_author_paypal(self):
        return self.context.getProperty('author_paypal', '')
    def set_author_paypal(self, value):
        return self.context.setMemberProperties({'author_paypal': value})
    author_paypal = property(get_author_paypal, set_author_paypal)

    def get_genre_interests(self):
        return self.context.getProperty('genre_interests', '')
    def set_genre_interests(self, value):
        return self.context.setMemberProperties({'genre_interests': value})
    genre_interests = property(get_genre_interests, set_genre_interests)

    def get_activities(self):
        return self.context.getProperty('activities', '')
    def set_activities(self, value):
        return self.context.setMemberProperties({'activities': value})
    activities = property(get_activities, set_activities)

    def get_media_formats(self):
        return self.context.getProperty('media_formats', '')
    def set_media_formats(self, value):
        return self.context.setMemberProperties({'media_formats': value})
    media_formats = property(get_media_formats, set_media_formats)

    def get_homepages(self):
        return self.context.getProperty('homepages', '')
    def set_homepages(self, value):
        return self.context.setMemberProperties({'homepages': value})
    homepages = property(get_homepages, set_homepages)
