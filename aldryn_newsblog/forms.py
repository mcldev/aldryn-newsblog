# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.conf import settings

from . import models


def convert_class_to_name(class_self):
    class_name = class_self.__class__.__name__
    return str(class_name).replace('NewsBlog', '').replace('PluginForm', '')


class AutoAppConfigFormMixin(forms.ModelForm):
    """
    If there is only a single AppConfig to choose, automatically select it.
    """
    if hasattr(settings, 'ALDRYN_NEWSBLOG_TEMPLATES'):
        render_template_choice = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        super(AutoAppConfigFormMixin, self).__init__(*args, **kwargs)
        if 'app_config' in self.fields:
            # if has only one choice, select it by default
            if self.fields['app_config'].queryset.count() == 1:
                self.fields['app_config'].empty_label = None

        if hasattr(settings, 'ALDRYN_NEWSBLOG_TEMPLATES'):
            template_choices = ((None, 'Default'),)
            lookup_name = convert_class_to_name(self)
            if lookup_name in settings.ALDRYN_NEWSBLOG_TEMPLATES:
                template_choices += settings.ALDRYN_NEWSBLOG_TEMPLATES.get(lookup_name)
            self.fields['render_template_choice'].choices=template_choices


class NewsBlogArchivePluginForm(AutoAppConfigFormMixin):
    class Meta:
        model = models.NewsBlogArchivePlugin
        fields = ['app_config', 'cache_duration']


class NewsBlogArticleSearchPluginForm(AutoAppConfigFormMixin):
    class Meta:
        model = models.NewsBlogArticleSearchPlugin
        fields = ['app_config', 'max_articles']


class NewsBlogAuthorsPluginForm(AutoAppConfigFormMixin):
    class Meta:
        model = models.NewsBlogAuthorsPlugin
        fields = ['app_config']


class NewsBlogCategoriesPluginForm(AutoAppConfigFormMixin):

    class Meta:
        model = models.NewsBlogCategoriesPlugin
        fields = ['app_config']


class NewsBlogFeaturedArticlesPluginForm(AutoAppConfigFormMixin):
    class Meta:
        model = models.NewsBlogFeaturedArticlesPlugin
        fields = ['app_config', 'article_count']


class NewsBlogLatestArticlesPluginForm(AutoAppConfigFormMixin):
    class Meta:
        model = models.NewsBlogLatestArticlesPlugin
        fields = [
            'app_config', 'latest_articles', 'exclude_featured',
            'cache_duration'
        ]


class NewsBlogTagsPluginForm(AutoAppConfigFormMixin):
    class Meta:
        fields = ['app_config']


class NewsBlogRelatedPluginForm(forms.ModelForm):
    class Meta:
        fields = ['cache_duration']
