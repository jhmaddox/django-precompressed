# *****************************************************************************
# precompressed/templatetags/staticfiles.py
# *****************************************************************************

"""
Extends django.contrib.staticfiles.templatetags.staticfiles to allow
the {% static %} template tag to target precompressed versions of configured
files when the client supports it.

"""

from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

from django import template
from django.contrib.staticfiles.templatetags import staticfiles

from precompressed import utils

__all__ = (
    'do_static',
    'StaticFilesNode',
)

register = template.Library()


# *****************************************************************************
# StaticFilesNode
# *****************************************************************************

class StaticFilesNode(staticfiles.StaticFilesNode):

    def url(self, context):
        request = context['request']
        result = super(StaticFilesNode, self).url(context)
        if (utils.accepts_gzip(request) and
                utils.should_save_gzipped_copy(result)):
            return utils.get_gzipped_name(result)
        return result


# *****************************************************************************
# do_static
# *****************************************************************************

@register.tag('static')
def do_static(parser, token):
    return StaticFilesNode.handle_token(parser, token)
