{
    'name': 'Filter In_Stock Variants',
    'version': '19.0.1.0.0',
    'category': 'Website',
    'summary': 'Auto-select in-stock product variant as default on website',
    'description': """
        Overrides the default variant selection on the website product page
        to prefer variants that are in stock. If the default variant (first
        in sequence) is out of stock, the module selects the first available
        in-stock variant instead. Falls back to standard behavior if all
        variants are out of stock.
    """,
    'author': 'Implefy AB',
    'website': 'https://github.com/Implefy_AB/filter_instock_variants',
    'license': 'LGPL-3',
    'depends': ['website_sale_stock'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
