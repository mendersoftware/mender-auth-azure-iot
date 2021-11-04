# Copyright 2021 Northern.tech AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
import os.path

SLEEP_INTERVAL = 60


class Path:
    """Hold all the path configuration for the client

    Usage::

      >>> from daemon.settings import settings
      >>> conf = settings.PATHS.conf


    """

    def __init__(self, data_store="/var/lib/mender"):
        self.conf_file = "/etc/mender/mender-auth-azure-iot.conf"
        self.server_cert = ""
        self.data_store = data_store
        # TODO - where are the identity scripts located (?)
        self.identity_scripts = os.path.join(
            self.data_store, "identity", "mender-device-identity"
        )


# Global singleton
PATHS = Path()
