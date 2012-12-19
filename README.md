django-precompressed
====================

precompressed is a pluggable application for Django developers who want to serve precompressed (gzipped) static files.

About
=====

+ Alters the behavior of `./manage.py collectstatic` to save gzipped copies of specified static files (by default `*.css` and `*.js`).
+ When the client supports `Content-Encoding: gzip` and `{% static %}` is used then the rendered URI will refer to the precompressed version of the static file.
+ Works with [CachedFilesMixin](https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#cachedstaticfilesstorage) and [storages.backends.s3boto.S3BotoStorage](http://django-storages.readthedocs.org/)

Installation
============

1. `pip install django-precompressed`
2. Add `precompressed` to your `settings.INSTALLED_APPS` before `'django.contrib.staticfiles'` so that precompressed's version of `{% static %}` will be utilized.
3. Set `settings.STATICFILES_STORAGE` to one that suits your needs (see Storages below).
4. Run `./manage.py collectstatic` to generate precompressed copies.
5. Utilize `{% static %}` template tag when referencing static files where applicable.

Configuration
=============

All settings are optional and specified via the `settings.PRECOMPRESSED_SETTINGS` dictionary.

+ `GZIP_PATTERNS` is a tuple of file patterns that are to be gzipped. Defaults to `('*.css', '*.js')`
+ `DEFAULT_COMPRESS_LEVEL` is a number 0-9 that specifies the default compression level. Defaults to 9.
+ `accepts_gzip(request)` is a function that returns True if the client supports `Content-Encoding: gzip`
+ `get_gzipped_name(name)` is a function that translates filenames and URIs to the precompressed version. Defaults to resource.ext becomes resource.gz.ext
+ `should_save_gzipped_copy(path)` is a function that returns True if the specified file should have a precompressed copy saved. Defaults to file matches GZIP_PATTERNS?

Storages
========

    precompressed.storage.PrecompressedStaticFilesStorage
    precompressed.storage.CachedPrecompressedStaticFilesStorage
    
These storages extend Django's builtin StaticFilesStorage to provide the described precompression behavior. If you use this you'll probably want to configure your webserver to add the `Content-Encoding: gzip` header when serving precompressed files.

    precompressed.storage.s3boto.PrecompressedS3BotoStorage
    precompressed.storage.s3boto.CachedPrecompressedS3BotoStorage

These storages extend [django-storages' S3BotoStorage](http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html) to provide described precompression behavior for files stored on [Amazon Simple Storage Service (Amazon S3)](http://aws.amazon.com/s3/)

The Cached prefixed versions of each utilize [CachedFilesMixin](https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#cachedstaticfilesstorage) and therefore store hashed copies of static files in addition to the precompressed versions.
