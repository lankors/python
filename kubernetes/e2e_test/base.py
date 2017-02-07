# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import copy
import os
import urllib3

from kubernetes.client.configuration import configuration

def is_k8s_running():
    try:
        urllib3.PoolManager().request('GET', '127.0.0.1:8080')
        return True
    except urllib3.exceptions.HTTPError:
        return False


def setSSLConfiguration():
    config = copy.copy(configuration)
    config.verify_ssl = True
    config.ssl_ca_cert = os.path.dirname(__file__) + '/../../scripts/example.pem'
    config.assert_hostname = False
    return config