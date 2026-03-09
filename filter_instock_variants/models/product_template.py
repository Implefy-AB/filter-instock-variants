from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_first_possible_combination(self, parent_combination=None, necessary_values=None):
        """Override to prefer in-stock variants on the website.

        Iterates possible combinations and returns the first one where the
        variant has available stock. Falls back to the standard first
        combination if no in-stock variant is found.
        """
        self.ensure_one()

        website = self.env['website'].get_current_website()
        if not website:
            return super()._get_first_possible_combination(
                parent_combination=parent_combination,
                necessary_values=necessary_values,
            )

        fallback = self.env['product.template.attribute.value']

        for idx, combination in enumerate(
            self._get_possible_combinations(parent_combination, necessary_values)
        ):
            if idx == 0:
                fallback = combination

            variant = self._get_variant_for_combination(combination)
            if not variant:
                continue

            if not variant.is_storable:
                return combination

            free_qty = website._get_product_available_qty(variant.sudo())
            if free_qty > 0:
                return combination

        return fallback
