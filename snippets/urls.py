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

from django.urls import path

from . import views


urlpatterns = [
    path('',
         view=views.IndexView.as_view(),
         name='snippets.index'),
    path('folders/'
         '<int:workbook_id>/',
         view=views.FoldersView.as_view(),
         name='snippets.folders'),
    path('snippets/'
         '<int:workbook_id>/'
         '<int:folder_id>/',
         view=views.SnippetsView.as_view(),
         name='snippets.snippets'),
    path('snippet/'
         '<int:workbook_id>/'
         '<int:folder_id>/'
         '<int:snippet_id>/',
         view=views.SnippetView.as_view(),
         name='snippets.snippet'),
]
