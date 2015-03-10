# -*- coding: utf-8 -*-

import urllib

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool

from aldryn_apphooks_config.utils import get_app_instance
from .models import Article


@toolbar_pool.register
class NewsBlogToolbar(CMSToolbar):
    watch_models = (Article, )
    supported_apps = ('aldryn_newsblog',)

    def populate(self):
        if not (self.is_current_app and self.request.user.has_perm(
                'aldryn_newsblog.add_article')):
            return

        menu = self.toolbar.get_or_create_menu('newsblog-app', _('News Blog'))
        menu.add_modal_item(_('Add Article'),
                            self.__build_article_admin_url(
                                'admin:aldryn_newsblog_article_add'))

        article = getattr(self.request, 'article', None)
        if article and self.request.user.has_perm(
                'aldryn_newsblog.change_article'):
            menu.add_modal_item(_('Edit Article'),
                                reverse('admin:aldryn_newsblog_article_change',
                                        args=(article.pk,)),
                                active=True
            )

    def __build_article_admin_url(self, *args, **kwargs):
        get = kwargs.pop('get', {})
        if not get:
            try:
                app_config_id = get_app_instance(self.request)[1].pk
                get = {'app_config': app_config_id}
            except AttributeError:
                pass
        url = reverse(*args, **kwargs)
        if get:
            url += '?' + urllib.urlencode(get)
        return url