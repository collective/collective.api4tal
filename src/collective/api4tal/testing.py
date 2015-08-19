# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.api4tal


class CollectiveApi4TalLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.api4tal)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.api4tal:default')


COLLECTIVE_API4TAL_FIXTURE = CollectiveApi4TalLayer()


COLLECTIVE_API4TAL_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_API4TAL_FIXTURE,),
    name='CollectiveApi4TalLayer:IntegrationTesting'
)


COLLECTIVE_API4TAL_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_API4TAL_FIXTURE,),
    name='CollectiveApi4TalLayer:FunctionalTesting'
)


COLLECTIVE_API4TAL_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_API4TAL_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveApi4TalLayer:AcceptanceTesting'
)
