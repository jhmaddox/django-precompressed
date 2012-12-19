# *****************************************************************************
# precompressed/storage/s3boto.py
# *****************************************************************************

"""
Defines static file storage classes that implement precompression
behavior and subclass storages.backends.s3boto.S3BotoStorage for users
who want to serve precompressed static files from Amazon Web Services S3.

"""

from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

from django.contrib.staticfiles.storage import CachedFilesMixin
from storages.backends.s3boto import S3BotoStorage

from precompressed.storage.base import SaveGzippedCopyMixin


# *****************************************************************************
# SaveGzippedCopyS3BotoMixin
# *****************************************************************************

class SaveGzippedCopyS3BotoMixin(SaveGzippedCopyMixin):

    """
    SaveGzippedCopyS3BotoMixin is a SaveGzippedCopyMixin that when
    used in conjunction with S3BotoStorage correctly sets the
    Content-Encoding header for gzipped files.

    """

    def pre_save_gzipped(self, name, gzipped_name, pregzipped_file):

        """
        S3BotoStorage doesn't allow per file headers, so we will
        temporarily overwrite the default headers to
        set the correct Content-Encoding.

        """

        self.set_s3boto_headers()

        return super(SaveGzippedCopyS3BotoMixin, self).pre_save_gzipped(
            name, gzipped_name, pregzipped_file,
        )

    def post_save_gzipped(self, name, gzipped_name, gzipped_file):

        """
        S3BotoStorage doesn't allow per file headers, so we
        need to restore the default headers that we overwrote
        before we saved the gzipped file.

        """

        self.unset_s3boto_headers()

        return super(SaveGzippedCopyS3BotoMixin, self).post_save_gzipped(
            name, gzipped_name, gzipped_file,
        )

    def set_s3boto_headers(self):

        """
        set_s3boto_headers overwrites default headers to set
        Content-Encoding: gzip for the next saved file.

        """

        self._pregzipped_headers = getattr(self, 'headers', {})
        self.headers = self._pregzipped_headers.copy()
        self.headers.update({'Content-Encoding': 'gzip'})

    def unset_s3boto_headers(self):

        """
        unset_s3boto_headers undoes set_s3boto_headers

        """

        self.headers = self._pregzipped_headers
        del self._pregzipped_headers


# *****************************************************************************
# CachedPrecompressedS3BotoStorage
# *****************************************************************************

class CachedPrecompressedS3BotoStorage(SaveGzippedCopyS3BotoMixin,
                                       CachedFilesMixin, S3BotoStorage):

    """
    CachedPrecompressedS3BotoStorage is an S3BotoStorage backend
    which in addition to saving hashed copies of files it saves
    also saves gzipped copies of configured files.

    """

    pass


# *****************************************************************************
# PrecompressedS3BotoStorage
# *****************************************************************************

class PrecompressedS3BotoStorage(SaveGzippedCopyS3BotoMixin, S3BotoStorage):

    """
    PrecompressedS3BotoStorage is an S3BotoStorage backend
    which also saves gzipped copies of configured files.

    """

    pass
