# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
from sgtk.platform.qt import QtCore, QtGui

# import the shotgun_model module from the shotgun utils framework
shotgun_model = sgtk.platform.import_framework("tk-framework-shotgunutils", "shotgun_model") 
ShotgunModel = shotgun_model.ShotgunModel 

class SgStatusModel(ShotgunModel):
    """
    This model represents status codes.
    """
    
    def __init__(self, parent):
        """
        Constructor
        """
        # folder icon
        ShotgunModel.__init__(self, parent, download_thumbs=False)
        fields=["bg_color", "icon", "code", "name"]
        order=[]
        self._load_data("Status", [], ["code"], fields, order)
        self._refresh_data()
    
    ############################################################################################
    # public methods
    
    def get_color_str(self, code):
        """
        Returns the color, as a string, for example '202,244,231'
        """
        for idx in range(self.rowCount()):
            item = self.item(idx)
            
            if item.text() == code:
                sg_data = item.data(ShotgunModel.SG_DATA_ROLE)
                return sg_data["bg_color"]
                        
        return None
    
    def get_long_name(self, code):
        """
        Returns the long name for a status, 'Undefined' if not found.
        """
        for idx in range(self.rowCount()):
            item = self.item(idx)
            
            if item.text() == code:
                sg_data = item.data(ShotgunModel.SG_DATA_ROLE)
                return sg_data["name"]
                        
        return "Undefined"

    
        
        