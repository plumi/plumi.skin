from plone.app.registry.browser import controlpanel
from plumi.skin.browser.interfaces import IPlumiSettings, _


class PlumiSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPlumiSettings
    label = _(u"Plumi settings")
    description = _(u"""""")

    def updateFields(self):
        super(PlumiSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(PlumiSettingsEditForm, self).updateWidgets()

class PlumiSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = PlumiSettingsEditForm

