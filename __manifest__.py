{
    'name'          : "Rating Widget",
    'version'       : "1.0",
    'depends'       : ['base'], 
    'category'      : 'Widget',
    'author'        : "Drownie",
    'description'   : "Rating Widget to Support Integer fields",
    'assets': {
        'web.assets_backend': [
            'rating_widget/static/src/style/rating.scss',
            'rating_widget/static/src/xml/rating.xml',
            'rating_widget/static/src/js/rating.js',
        ],
    },
    'application': False,
    "lisence":"LGPL-3"
}