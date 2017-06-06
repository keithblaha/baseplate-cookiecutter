import hvac
from baseplate.secrets import secrets_store_from_config


def configure_vault(app_config):
    secrets = secrets_store_from_config(app_config)
    vault = hvac.Client(
        url=secrets.get_vault_url(),
        token=secrets.get_vault_token(),
    )

    # if you're taking advantage of features that need direct hvac access from
    # the app you'll likely also need to configure vault backends, users,
    # roles, etc. TODO: add your persistent schema-like vault configurations
    # here.
    vault.list_secret_backends()
