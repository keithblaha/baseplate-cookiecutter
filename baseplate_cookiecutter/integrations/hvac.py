from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from cookiecutter.utils import rmtree

from . import Integration


class HvacIntegration(Integration):
    slug = "hvac"
    name = "HVAC (advanced client for Vault, for more than regular secrets)"

    variables = {
        "dependencies": {
            "apt": [
                "python-hvac"
            ],

            "python": [
                "hvac",
            ],
        },

        "imports": {
            "external": [
                "from baseplate.context.hvac import hvac_factory_from_config",
            ],
        },

        "puppet_modules": [
            "vault",
        ],
    }

    def prune(self, variables):
        filename = os.path.join(variables["module_name"], "models", "vault.py")
        os.remove(filename)
        rmtree("puppet/modules/vault")
