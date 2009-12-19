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


from urllib import urlencode
from urllib2 import urlopen, Request


class Pastebin(object):

    """ Base Pastebin Controller """
    
    def __init__(self):
        """ Constructor """
        self.provider_url = ""
       
    def _request(self, url=None, params=None, outputs=None):        
        """ Make HTTP Request """        
        if url is None:
            url = self.provider_url
        if outputs is None:
            outputs = {}        
        if params is not None:    
            response_raw = urlopen(Request(url), urlencode(params)).read()
        else:
            response_raw = urlopen(Request(url)).read()
        output = {
            "raw": response_raw
        }
        for key, func in outputs.iteritems():
            output[key] = func(response_raw)                      
        return output

    def post_text(self, text):    
        """ Post Text to Pastebin Provider """        
        pass        
    
    def get_text(self, code):    
        """ Get Text from Pastebin Provider """        
        pass
        
        
class SprungePastebin(Pastebin):
    
    """ Controller for 'sprunge.us' Pastebin """

    def __init__(self):
        """ Constructor """     
        self.provider_url = "http://sprunge.us"

    def post_text(self, text):   
        """ Post Text to Pastebin Provider """
        params = {"sprunge": text}        
        outputs = {
            "code": lambda x: x.split("/")[-1].replace("\n",""),
            "url": lambda x: "%s/%s" % (self.provider_url, x.split("/")[-1].replace("\n","")),
            "success": lambda x: "http://sprunge.us" in x
        }
        response = self._request(params=params, outputs=outputs)
        return response
        
    def get_text(self, code):
        """ Get Text from Pastebin Provider """
        url = "%s/%s" % (self.provider_url, code)
        response = self._request(url=url)
        return response.get("raw")

     
        
