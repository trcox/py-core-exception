# *******************************************************************************
# Copyright 2017 Dell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
#
# @microservice: py-core-exception library
# @author: Tyler Cox, Dell
# @version: 1.0.0
# *******************************************************************************

from http import HTTPStatus


class NotFoundException(RuntimeError):

    def __init__(self, type, identifier):
        super(NotFoundException, self).__init__(
            "could not find " + type + " with id: " + identifier)
        self.status = HTTPStatus.NOT_FOUND
