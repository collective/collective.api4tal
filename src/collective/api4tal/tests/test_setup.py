# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.api4tal.testing import COLLECTIVE_API4TAL_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.api4tal is properly installed."""

    layer = COLLECTIVE_API4TAL_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.api4tal is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.api4tal'))

    def test_browserlayer(self):
        """Test that ICollectiveApi4TalLayer is registered."""
        from collective.api4tal.interfaces import ICollectiveApi4TalLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveApi4TalLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_API4TAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.api4tal'])

    def test_product_uninstalled(self):
        """Test if collective.api4tal is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('collective.api4tal'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveApi4TalLayer is removed."""
        from collective.api4tal.interfaces import ICollectiveApi4TalLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveApi4TalLayer, utils.registered_layers())
