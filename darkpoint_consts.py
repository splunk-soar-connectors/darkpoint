# File: darkpoint_consts.py
#
# Copyright (c) 2019-2024 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
# amount of seconds to sleep in between poll attempts for report status
DARKPOINT_SLEEP_SECS = 3
DARKPOINT_MSG_MAX_POLLS_REACHED = 'Reached max polling attempts'

ERROR_AUTHENTICATING_TO_SERVER = "Error authenticating with DarkPoint service. Details: {0}"
ERROR_CONNECTING_TO_SERVER = "Error while connecting to the server. Details: {0}"
ERROR_RETRIEVING_ARTIFACT = "Error encountered while retrieving artifact entries.\r\n{0}"
ERROR_WHILE_FATCHING_WORKFLOW = "Error occurred while fetching the workflow status of the user: {0} and SHA1 hash: {1}. Error: {2}"
