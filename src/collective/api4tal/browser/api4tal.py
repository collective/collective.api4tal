# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone import api


class User_Get_Roles(BrowserView):

    def __call__(self):
        return api.user.get_roles()


class PortalGet(BrowserView):

    def __call__(self):
        return api.portal.get()


class User_Get_Current(BrowserView):

    def __call__(self):
        return api.user.get_current()


class User_Is_Anonymous(BrowserView):

    def __call__(self):
        return api.user.is_anonymous()
