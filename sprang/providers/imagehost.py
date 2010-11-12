#!/usr/bin/env python

"""

Sprang

Copyright (C) 2009 JingleManSweep <jinglemansweep@gmail.com>

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your 
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for 
more details. You should have received a copy of the GNU General Public
License along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
    
"""

import base64
import json
from urllib import urlencode
from urllib2 import urlopen, Request

from base import Provider
        
        
class ImgurImageHost(Provider):
    
    """ Controller for 'imgur.com' Image Host """

    _code_ = "imgur"
    _name_ = "Imgur"
    _url_ = "http://imgur.com"
    _mimetypes_ = ["image/png", "image/jpeg", "image/gif", "image/bmp"]
    _api_key_ = "d71d6a4a82e19cff3b5b30b5c2552337"

    def __init__(self):
        """ Constructor """ 
        super(ImgurImageHost, self).__init__()    
        self.provider_url = "http://api.imgur.com/2/upload.json"

    def post_data(self, data, mimetype=None):   
        """ Post Data to Image Host Provider """
        encoded_data = base64.b64encode(data)
        params = {"image": encoded_data, "type": "file", "key": self._api_key_}
        outputs = {
            "code": lambda x: json.loads(x).get("upload").get("image").get("hash"),
            "url": lambda x: json.loads(x).get("upload").get("links").get("original"),
            "success": lambda x: json.loads(x).get("upload")
        }
        response = self._request(params=params, outputs=outputs, multipart=True)
        return response
        
    def get_data(self, data):
        """ Get Data from Image Host Provider """
        url = "%s/%s" % (self.provider_url, code)
        response = self._request(url=url)
        return response.get("raw")

     
        
