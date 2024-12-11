# -*- coding: utf-8 -*-

{
  "name"                 :  "Odoo Debranding",
  "summary"              :  """This is the base odoo backend debranding module.""",
  "category"             :  "Generic Modules",
  "version"              :  "17.0.1.0.0",
  "sequence"             :  1,
  "author"               :  "HSxTech Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://hsxtech.net",
  "description"          :  """This is the base odoo backend debranding module.""",
  "depends"              :  ['web', 'mail', 'portal', 'website'],
  "data"                 :  [
                             'views/res_config_view.xml',
                             'views/web_client_template.xml',
                             'views/portal_templates.xml',
                             'views/email_templates.xml',
                             'data/data.xml',
                            ],
  "qweb"                 :  [
                             'static/src/xml/base.xml',
                             'static/src/xml/client_action.xml',
                            ],
  "assets"               : {  
                            "web.assets_backend": [
                                '/hsg_debranding/static/src/js/web_client.js',
                                '/hsg_debranding/static/src/js/dialog.js',
                                '/hsg_debranding/static/src/js/my_widget.js',
                                '/hsg_debranding/static/src/js/user_menu.js',
                                '/hsg_debranding/static/src/js/mail_dialog.js'
                            ],
                            'web.assets_qweb': [
                                'hsg_debranding/static/src/xml/dashboard.xml',
                                'hsg_debranding/static/src/xml/base.xml',
                                'hsg_debranding/static/src/xml/client_action.xml',
                            ],
                         },
  "images"               :  ['hsg_debranding/static/description/banner.gif'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  15,
  "currency"             :  "USD",
  "pre_init_hook"        : "pre_init_check",
}
