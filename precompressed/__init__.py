# *****************************************************************************
# precompressed/__init__.py
# *****************************************************************************

"""
precompressed is a pluggable Django application for developers who want
to serve precompressed (gzipped) static files.

Usage

1. In your templates, use the 'static' tag to resolve URIs for static files.

2. Add 'precompressed' to your settings.INSTALLED_APPS before
  'django.contrib.staticfiles' so its version of the 'static'
  template tag will be utilized. 

3. Set settings.STATICFILES_STORAGE to one that suits your needs:

  'precompressed.storage.PrecompressedStaticFilesStorage'
  'precompressed.storage.CachedPrecompressedStaticFilesStorage'
  'precompressed.storage.s3boto.PrecompressedS3BotoStorage'
  'precompressed.storage.s3boto.CachedPrecompressedS3BotoStorage'

4. Run './manage.py collectstatic' to generate precompressed
  versions of static files.

"""


