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

from snippets.models import Workbook

from utility.views import GenericView


class BaseView(GenericView):
    """Base view"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['load_bootstrap'] = True
        context['load_jquery'] = True
        context['load_sidebar'] = True
        context['all_workbooks'] = Workbook.objects.all().order_by('name')
        context['all_folders'] = dict([(workbook.name,
                                       list(workbook.folder_set.all()))
                                       for workbook
                                       in context['all_workbooks']])
        return context
