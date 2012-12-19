# *****************************************************************************
# precompressed/utils.py
# *****************************************************************************

"""
Defines useful methods and variables used throughout precompressed, each
configurable via the settings.PRECOMPRESSED_SETTINGS dictionary

"""

from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

from django.conf import settings
from django.contrib.staticfiles.utils import matches_patterns

SETTINGS = getattr(settings, 'PRECOMPRESSED_SETTINGS', {})
GZIP_PATTERNS = SETTINGS.get('GZIP_PATTERNS', ('*.css', '*.js'))
DEFAULT_COMPRESS_LEVEL = SETTINGS.get('DEFAULT_COMPRESS_LEVEL', 9)


# *****************************************************************************
# accepts_gzip
# *****************************************************************************

def accepts_gzip(request):

    """
    returns True if the request accepts Content-Encoding: gzip

    """

    return 'gzip' in request.META['HTTP_ACCEPT_ENCODING']


if 'accepts_gzip' in SETTINGS:
    accepts_gzip = SETTINGS['accepts_gzip']


# *****************************************************************************
# get_gzipped_name
# *****************************************************************************

def get_gzipped_name(name):

    """
    returns the location of the gzipped version of a specified file

    """

    file_ext_index = name.rfind('.')
    file_name, file_ext = name[:file_ext_index], name[file_ext_index:]
    return '%s.gz%s' % (file_name, file_ext)


if 'get_gzipped_name' in SETTINGS:
    get_gzipped_name = SETTINGS['get_gzipped_name']


# *****************************************************************************
# should_save_gzipped_copy
# *****************************************************************************

def should_save_gzipped_copy(path):

    """
    returns True if the file specified by path should
    also have a copy gzipped and saved as get_gzipped_name(path)

    """

    return matches_patterns(path, GZIP_PATTERNS)


if 'should_save_gzipped_copy' in SETTINGS:
    should_save_gzipped_copy = SETTINGS['should_save_gzipped_copy']
