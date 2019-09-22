##
#     Project: Django Snippets
# Description: A Django application to organize code snippets
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2019 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def get_workbook_url_by_pk(workbooks, name):
    """
    Get the workbook url by its name
    """
    return reverse('snippets.workbook',
                   kwargs={'workbook_id': [workbook.pk
                                           for workbook
                                           in workbooks
                                           if workbook.name == name][0]})
