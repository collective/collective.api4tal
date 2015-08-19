.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.api4tal
==============================================================================

Plone.api for TAL, use in pt file.

The plone.api is an elegant and simple API, built for humans wishing to develop with Plone.

But, at template file(*.pt), these useful functions can not be used directly, such as 'api.portal.get()'

Through browerview's design, so that these functions can be used on the pt file.

Features
--------

- **@@portal_get** mapping to **api.portal.get()**
- **@@user_get_current** mapping to **api.user.get_current()**
- **@@user_is_anonymous** mapping to **api.user.is_anonymous()**

Examples
--------

For example, you can use **@@user_is_anonymous** at template, such as:

    <div tal:condition="context/@@user_is_anonymous">
    ...
    </div>

or, you can use **@@portal_get** at template, such as:

    <div tal:define="portal context/@@portal_get">
    ...
    </div>

Installation
------------

Install collective.api4tal by adding it to your buildout::

   [buildout]

    ...

    eggs =
        collective.api4tal

and then running "bin/buildout"


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.api4tal/issues
- Source Code: https://github.com/collective/collective.api4tal


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: andy@mingtak.com.tw


License
-------

The project is licensed under the GPLv2.
