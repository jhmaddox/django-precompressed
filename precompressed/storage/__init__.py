# *****************************************************************************
# precompressed/storage/__init__.py
# *****************************************************************************

"""
Defines various static files storage classes that implement
precompression behavior.

"""

from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

from django.contrib.staticfiles.storage import StaticFilesStorage
from django.contrib.staticfiles.storage import CachedStaticFilesStorage

from precompressed.storage.base import SaveGzippedCopyMixin


# *****************************************************************************
# CachedPrecompressedStaticFilesStorage
# *****************************************************************************

class CachedPrecompressedStaticFilesStorage(SaveGzippedCopyMixin,
                                            CachedStaticFilesStorage):

    """
    CachedPrecompressedStaticFilesStorage is a static file system storage
    backend which in addition to saving hashed copies of files it saves
    also saves gzipped copies of configured files.

    """

    pass


# *****************************************************************************
# PrecompressedStaticFilesStorage
# *****************************************************************************

class PrecompressedStaticFilesStorage(SaveGzippedCopyMixin,
                                      StaticFilesStorage):

    """
    PrecompressedStaticFilesStorage is a static file system storage
    backend which also saves gzipped copies of configured files.

    """

    pass
