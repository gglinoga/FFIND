# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.3
#
# <auto-generated>
#
# Generated from file `Exporter.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_ServerErrors_ice
import omero_ServicesF_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Included module omero.grid
_M_omero.grid = Ice.openModule('omero.grid')

# Start of module omero
__name__ = 'omero'

# Start of module omero.api
__name__ = 'omero.api'

if 'Exporter' not in _M_omero.api.__dict__:
    _M_omero.api.Exporter = Ice.createTempClass()
    class Exporter(_M_omero.api.StatefulServiceInterface):
        """
        Stateful service for generating OME-XML or OME-TIFF from data stored
        in OMERO. Intended usage:
        ExporterPrx e = sf.createExporter();
        // Exporter is currently in the configuration state
        // Objects can be added by id which should be present
        // in the output.
        e.addImage(1);
        // As soon as a generate method is called, the objects
        // added to the Exporter are converted to the specified
        // format. The length of the file produced is returned.
        // No more objects can be added to the Exporter, nor can
        // another generate method be called.
        long length = e.generateTiff();
        // As soon as the server-side file is generated, read()
        // can be called to get file segments. To create another
        // file, create a second Exporter. Be sure to close all
        // Exporter instances.
        long read = 0
        byte\[] buf;
        while (true) {
        buf = e.read(read, 1000000);
        // Store to file locally here
        if (buf.length
        """
        def __init__(self):
            if Ice.getType(self) == _M_omero.api.Exporter:
                raise RuntimeError('omero.api.Exporter is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::api::Exporter', '::omero::api::ServiceInterface', '::omero::api::StatefulServiceInterface')

        def ice_id(self, current=None):
            return '::omero::api::Exporter'

        def ice_staticId():
            return '::omero::api::Exporter'
        ice_staticId = staticmethod(ice_staticId)

        def addImage_async(self, _cb, id, current=None):
            """
            Adds a single image with basic metadata to the Exporter for inclusion
            on the next call to getBytes().
            Arguments:
            _cb -- The asynchronous callback object.
            id -- 
            current -- The Current object for the invocation.
            """
            pass

        def generateXml_async(self, _cb, current=None):
            """
            Generates an OME-XML file. The return value is the length
            of the file produced.
            Arguments:
            _cb -- The asynchronous callback object.
            current -- The Current object for the invocation.
            """
            pass

        def generateTiff_async(self, _cb, current=None):
            """
            Generates an OME-TIFF file. The return value is the length
            of the file produced. This method ends configuration.
            Arguments:
            _cb -- The asynchronous callback object.
            current -- The Current object for the invocation.
            """
            pass

        def read_async(self, _cb, position, length, current=None):
            """
            Returns length bytes from the output file. The
            file can be safely read until reset() is called.
            Arguments:
            _cb -- The asynchronous callback object.
            position -- 
            length -- 
            current -- The Current object for the invocation.
            """
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.api._t_Exporter)

        __repr__ = __str__

    _M_omero.api.ExporterPrx = Ice.createTempClass()
    class ExporterPrx(_M_omero.api.StatefulServiceInterfacePrx):

        """
        Adds a single image with basic metadata to the Exporter for inclusion
        on the next call to getBytes().
        Arguments:
        id -- 
        _ctx -- The request context for the invocation.
        """
        def addImage(self, id, _ctx=None):
            return _M_omero.api.Exporter._op_addImage.invoke(self, ((id, ), _ctx))

        """
        Adds a single image with basic metadata to the Exporter for inclusion
        on the next call to getBytes().
        Arguments:
        id -- 
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_addImage(self, id, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.Exporter._op_addImage.begin(self, ((id, ), _response, _ex, _sent, _ctx))

        """
        Adds a single image with basic metadata to the Exporter for inclusion
        on the next call to getBytes().
        Arguments:
        id -- 
        """
        def end_addImage(self, _r):
            return _M_omero.api.Exporter._op_addImage.end(self, _r)

        """
        Generates an OME-XML file. The return value is the length
        of the file produced.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def generateXml(self, _ctx=None):
            return _M_omero.api.Exporter._op_generateXml.invoke(self, ((), _ctx))

        """
        Generates an OME-XML file. The return value is the length
        of the file produced.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_generateXml(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.Exporter._op_generateXml.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Generates an OME-XML file. The return value is the length
        of the file produced.
        Arguments:
        """
        def end_generateXml(self, _r):
            return _M_omero.api.Exporter._op_generateXml.end(self, _r)

        """
        Generates an OME-TIFF file. The return value is the length
        of the file produced. This method ends configuration.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def generateTiff(self, _ctx=None):
            return _M_omero.api.Exporter._op_generateTiff.invoke(self, ((), _ctx))

        """
        Generates an OME-TIFF file. The return value is the length
        of the file produced. This method ends configuration.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_generateTiff(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.Exporter._op_generateTiff.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Generates an OME-TIFF file. The return value is the length
        of the file produced. This method ends configuration.
        Arguments:
        """
        def end_generateTiff(self, _r):
            return _M_omero.api.Exporter._op_generateTiff.end(self, _r)

        """
        Returns length bytes from the output file. The
        file can be safely read until reset() is called.
        Arguments:
        position -- 
        length -- 
        _ctx -- The request context for the invocation.
        """
        def read(self, position, length, _ctx=None):
            return _M_omero.api.Exporter._op_read.invoke(self, ((position, length), _ctx))

        """
        Returns length bytes from the output file. The
        file can be safely read until reset() is called.
        Arguments:
        position -- 
        length -- 
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_read(self, position, length, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.Exporter._op_read.begin(self, ((position, length), _response, _ex, _sent, _ctx))

        """
        Returns length bytes from the output file. The
        file can be safely read until reset() is called.
        Arguments:
        position -- 
        length -- 
        """
        def end_read(self, _r):
            return _M_omero.api.Exporter._op_read.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.api.ExporterPrx.ice_checkedCast(proxy, '::omero::api::Exporter', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.api.ExporterPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::api::Exporter'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.api._t_ExporterPrx = IcePy.defineProxy('::omero::api::Exporter', ExporterPrx)

    _M_omero.api._t_Exporter = IcePy.defineClass('::omero::api::Exporter', Exporter, -1, (), True, False, None, (_M_omero.api._t_StatefulServiceInterface,), ())
    Exporter._ice_type = _M_omero.api._t_Exporter

    Exporter._op_addImage = IcePy.Operation('addImage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_long, False, 0),), (), None, (_M_omero._t_ServerError,))
    Exporter._op_generateXml = IcePy.Operation('generateXml', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (), (), ((), IcePy._t_long, False, 0), (_M_omero._t_ServerError,))
    Exporter._op_generateTiff = IcePy.Operation('generateTiff', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (), (), ((), IcePy._t_long, False, 0), (_M_omero._t_ServerError,))
    Exporter._op_read = IcePy.Operation('read', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_long, False, 0), ((), IcePy._t_int, False, 0)), (), ((), _M_Ice._t_ByteSeq, False, 0), (_M_omero._t_ServerError,))

    _M_omero.api.Exporter = Exporter
    del Exporter

    _M_omero.api.ExporterPrx = ExporterPrx
    del ExporterPrx

# End of module omero.api

__name__ = 'omero'

# End of module omero