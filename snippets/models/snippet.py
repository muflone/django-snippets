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

from django.db import models
from django.utils.translation import pgettext_lazy

from utility.models import BaseModel, BaseModelAdmin


class Snippet(BaseModel):
    folder = models.ForeignKey('Folder',
                               on_delete=models.PROTECT,
                               verbose_name=pgettext_lazy('Snippet',
                                                          'folder'))
    name = models.CharField(max_length=255,
                            verbose_name=pgettext_lazy('Snippet',
                                                       'name'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy('Snippet',
                                                              'description'))
    code = models.TextField(blank=True,
                            verbose_name=pgettext_lazy('Snippet',
                                                       'code'))
    language = models.ForeignKey('Language',
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True,
                                 verbose_name=pgettext_lazy('Snippet',
                                                            'language'))
    order = models.PositiveIntegerField(default=0,
                                        verbose_name=pgettext_lazy('Snippet',
                                                                    'order'))

    class Meta:
        # Define the database table
        db_table = 'snippets_snippets'
        ordering = ['name']
        unique_together = ('folder', 'name')
        verbose_name = pgettext_lazy('Snippet', 'Snippet')
        verbose_name_plural = pgettext_lazy('Snippet', 'Snippets')

    def __str__(self):
        return self.name


class SnippetAdmin(BaseModelAdmin):
    pass
