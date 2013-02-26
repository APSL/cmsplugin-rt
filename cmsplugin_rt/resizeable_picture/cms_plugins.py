from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from models import *

bootstrap_module_name = _("Widgets")
layout_module_name = _("Layout elements")
generic_module_name = _("Generic")
meta_module_name = _("Meta elements")

from cms.plugins.picture.cms_plugins import PicturePlugin

class ResizeablePicturePlugin(PicturePlugin):
    model = ResizeablePicturePluginModel
    name = _("Resizable Picture")
    #module = generic_module_name
    render_template = "resizeable_picture_plugin.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        if instance.url:
            link = instance.url
        elif instance.page_link:
            link = instance.page_link.get_absolute_url()
        else:
            link = ""
        if instance.img_width.endswith("%"):
            context["width_percent"] = instance.img_width
        else:
            context["width"] = instance.img_width
        if instance.img_height.endswith("%"):
            context["height_percent"] = instance.img_height
        else:
            context["height"] = instance.img_height
        context.update({
            'picture': instance,
            'link': link,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(ResizeablePicturePlugin)

