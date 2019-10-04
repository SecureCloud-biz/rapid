"""
 Copyright (c) 2015 Michael Bright and Bamboo HR LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import logging

from rapid.lib import IOC
from rapid.lib.constants import Constants
from rapid.lib.framework.injectable import Injectable
from rapid.master.master_configuration import MasterConfiguration
from rapid.workflow.action_instances_service import ActionInstanceService
from rapid.workflow.queue_handlers.queue_handler import QueueHandler
from rapid.workflow.queue_handlers.queue_handler_constants import QueueHandlerConstants
from rapid.workflow.queue_service import QueueService

logger = logging.getLogger("rapid")


class Queue(Injectable):
    __injectables__ = {'queue_service': QueueService, 'action_instance_service': ActionInstanceService, 'rapid_config': MasterConfiguration}

    def __init__(self, queue_service, action_instance_service, rapid_config):
        """
        :param queue_service:
        :type queue_service:
        :param action_instance_service:
        :type action_instance_service: rapid.workflow.action_instances_service.ActionInstanceService
        :type rapid_config: rapid.master.master_configuration.MasterConfiguration
        """
        self.queue_service = queue_service
        self.action_instance_service = action_instance_service
        self.rapid_config = rapid_config
        self.queue_handlers = []  # type: list[QueueHandler]
        self.setup_queue_handlers()

    def setup_queue_handlers(self):
        # type: () -> None
        for handler in QueueHandlerConstants.queue_handler_classes:
            self.queue_handlers.append(IOC.get_class_instance(handler))

    def process_queue(self, clients):
        for work_request in self.queue_service.get_current_work():
            for queue_handler in self.queue_handlers:
                if queue_handler.can_process_work_request(work_request):
                    try:
                        queue_handler.process_work_request(work_request, clients)
                    except Exception as exception:
                        logger.exception(exception)
                        self.action_instance_service.edit_action_instance(work_request.action_instance_id, {'status_id': Constants.STATUS_FAILED})
                    break

    def verify_still_working(self, clients):
        for action_instance in self.queue_service.get_verify_working(self.rapid_config.queue_consider_late_time):
            for queue_handler in self.queue_handlers:
                if queue_handler.can_process_action_instance(action_instance):
                    try:
                        queue_handler.process_action_instance(action_instance, clients)
                    except Exception as exception:
                        logger.exception(exception)
                        self.action_instance_service.edit_action_instance(action_instance['id'], {'status_id': Constants.STATUS_FAILED})
                    break
