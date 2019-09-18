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

from snippets.models import Snippet, Workbook, Folder

from utility.views import GenericView


class FolderView(GenericView):
    """Folder view"""
    template_name = 'snippets/folder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Folder'
        context['page_content'] = ('Folder',)
        context['workbook'] = Workbook.objects.get(id=context['workbook_id'])
        context['folder'] = Folder.objects.get(id=context['folder_id'])
        context['snippets'] = Snippet.objects.filter(
            folder_id=context['folder_id']
        ).order_by('name')
        return context
