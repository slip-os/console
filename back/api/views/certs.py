import certsign

from flask import send_from_directory

from api.views import BaseResource
from api.auth import token_auth
from api.tasks import cron
from api.config import CERT_DIR


ACME_DIR = '/var/tmp/acme/'


@cron('0 0 1,11,21 * *')
def renew_certs():
    """
    Scans CERT_DIR and renews active certs.

    * Certs are named as: <domain>.com.pem
    * The Domain model can be used to determine if a cert is used or not.
    * Unused certs are not renewed.
    * Once unused certs are old enough, they are purged.
    """
    pass


def acme(path):
    """
    Exposes acme-challenges for obtaining certificates.
    """
    return send_from_directory(ACME_DIR, path)


class CertResource(BaseResource):
    "Allows new ceritficate requests, and provides access to certs."
    def is_authenticated(self):
        # Allow read access with token auth.
        if super().is_authenticated():
            return True

        if self.request_method() == 'GET' and token_auth():
            return True

        return False