# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook that loads defines all the available actions, broken down by publish type. 
"""
import os

import sgtk

from syntheyes import get_existing_connection

HookBaseClass = sgtk.get_hook_baseclass()

class SyntheyesActions(HookBaseClass):

    ##############################################################################################################
    # public interface - to be overridden by deriving classes 

    def generate_actions(self, sg_publish_data, actions, ui_area):
        """
        Returns a list of action instances for a particular publish.
        This method is called each time a user clicks a publish somewhere in the UI.
        The data returned from this hook will be used to populate the actions menu for a publish.

        The mapping between Publish types and actions are kept in a different place
        (in the configuration) so at the point when this hook is called, the loader app
        has already established *which* actions are appropriate for this object.

        The hook should return at least one action for each item passed in via the 
        actions parameter.

        This method needs to return detailed data for those actions, in the form of a list
        of dictionaries, each with name, params, caption and description keys.

        Because you are operating on a particular publish, you may tailor the output 
        (caption, tooltip etc) to contain custom information suitable for this publish.

        The ui_area parameter is a string and indicates where the publish is to be shown. 
        - If it will be shown in the main browsing area, "main" is passed. 
        - If it will be shown in the details area, "details" is passed.
        - If it will be shown in the history area, "history" is passed. 

        Please note that it is perfectly possible to create more than one action "instance" for 
        an action! You can for example do scene introspection - if the action passed in 
        is "character_attachment" you may for example scan the scene, figure out all the nodes
        where this object can be attached and return a list of action instances:
        "attach to left hand", "attach to right hand" etc. In this case, when more than 
        one object is returned for an action, use the params key to pass additional 
        data into the run_action hook.

        :param sg_publish_data: Shotgun data dictionary with all the standard publish fields.
        :param actions: List of action strings which have been defined in the app configuration.
        :param ui_area: String denoting the UI Area (see above).
        :returns List of dictionaries, each with keys name, params, caption and description
        """
        app = self.parent
        app.log_debug("Generate actions called for UI element %s. "
                      "Actions: %s. Publish Data: %s" % (ui_area, actions, sg_publish_data))

        action_instances = []

        if "import_shot" in actions:
            action_instances.append( {"name": "import_shot", 
                                      "params": None,
                                      "caption": "Import Shot into Scene", 
                                      "description": "This will import the shot item into the current scene."} )

        if "import_mesh" in actions:
            action_instances.append( {"name": "import_mesh", 
                                      "params": None,
                                      "caption": "Import Mesh into Scene", 
                                      "description": "This will import the mesh item into the current scene."} )

        if "merge" in actions:
            action_instances.append( {"name": "merge", 
                                      "params": None,
                                      "caption": "Merge into Scene", 
                                      "description": "This will merge the item into the current scene."} )

        return action_instances

    def execute_action(self, name, params, sg_publish_data):
        """
        Execute a given action. The data sent to this be method will
        represent one of the actions enumerated by the generate_actions method.

        :param name: Action name string representing one of the items returned by generate_actions.
        :param params: Params data, as specified by generate_actions.
        :param sg_publish_data: Shotgun data dictionary with all the standard publish fields.
        :returns: No return value expected.
        """
        app = self.parent
        app.log_debug("Execute action called for action %s. "
                      "Parameters: %s. Publish Data: %s" % (name, params, sg_publish_data))

        # resolve path
        path = self.get_publish_path(sg_publish_data)

        if name == "import_mesh":
            self._do_import_mesh(path, sg_publish_data)

        if name == "import_shot":
            self._do_import_shot(path, sg_publish_data)

        if name == "merge":
            self._do_merge(path, sg_publish_data)

    ##############################################################################################################
    # helper methods which can be subclassed in custom hooks to fine tune the behaviour of things

    def _do_import_shot(self, path, sg_publish_data):
        """
        Import shot item into SynthEyes.

        :param path: Path to file.
        :param sg_publish_data: Shotgun data dictionary with all the standard publish fields.
        """
        if not os.path.exists(path):
            raise Exception("File not found on disk - '%s'" % path)

        hlev = get_existing_connection()
        hlev.AddShot(path)

    # TODO: AddStereoShot
    # TODO: AddSurveyShot

    def _do_import_mesh(self, path, sg_publish_data):
        """
        Import mesh item into SynthEyes.

        :param path: Path to file.
        :param sg_publish_data: Shotgun data dictionary with all the standard publish fields.
        """
        if not os.path.exists(path):
            raise Exception("File not found on disk - '%s'" % path)

        hlev = get_existing_connection()
        hlev.ReadObj(path)

    def _do_merge(self, path, sg_publish_data):
        """
        Merge item into SynthEyes.

        :param path: Path to file.
        :param sg_publish_data: Shotgun data dictionary with all the standard publish fields.
        """
        if not os.path.exists(path):
            raise Exception("File not found on disk - '%s'" % path)

        hlev = get_existing_connection()

        # Merge SNI with unique tracker names
        uni = 1
        hlev.MergeSNI(path, uni)
