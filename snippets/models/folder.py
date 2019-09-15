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


class Folder(BaseModel):
    workbook = models.ForeignKey('Workbook',
                                 on_delete=models.PROTECT,
                                 verbose_name=pgettext_lazy('Folder',
                                                            'workbook'))
    name = models.CharField(max_length=255,
                            verbose_name=pgettext_lazy('Folder',
                                                       'name'))
    description = models.TextField(blank=True,
                                   verbose_name=pgettext_lazy('Folder',
                                                              'description'))
    order = models.PositiveIntegerField(default=0,
                                        verbose_name=pgettext_lazy('Folder',
                                                                   'order'))

    class Meta:
        # Define the database table
        db_table = 'snippets_folders'
        ordering = ['workbook', 'order', 'name']
        unique_together = ('workbook', 'name')
        verbose_name = pgettext_lazy('Folder', 'Folder')
        verbose_name_plural = pgettext_lazy('Folder', 'Folders')

    def __str__(self):
        return '{WORKBOOK} > {NAME}'.format(WORKBOOK=self.workbook,
                                            NAME=self.name)


class FolderAdmin(BaseModelAdmin):
    pass
