from zope.interface import (
    Attribute,
    Interface,
    )


class IPreProcess(Interface):
    def __call__(fileobj):
        """Initial processing for target file.

        :param fileobj:
        :rtype: file like object
        :return fileobj: file object (seeked to top)
        """


class IParser(Interface):
    def __call__(fileobj):
        """Parse fileobj

        :param fileobj:
        :rtype: unkown
        :return obj: parsed object
        """


class IPostProcess(Interface):
    def __call__(obj):
        """Post process to obj

        :param fileobj:
        :rtype: unkown
        :return obj: post processed object
        """


class IReader(Interface):
    pre = Attribute('pre process')
    parse = Attribute('parser process')
    post = Attribute('post process')

    def __call__(obj):
        """Read formatted file"""
