# *****************************************************************************
# precompressed/context_processors.py
# *****************************************************************************

"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.

"""

from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

from precompressed import utils


# *****************************************************************************
# accepts_gzip
# *****************************************************************************

def accepts_gzip(request):

    """
    defines ACCEPTS_GZIP -- a boolean which reflects whether
    the request accepts Content-Type: gzip.

    """

    return {'ACCEPTS_GZIP': utils.accepts_gzip(request)}
