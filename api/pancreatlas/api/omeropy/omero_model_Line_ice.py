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
# Generated from file `Line.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_model_RTypes_ice
import omero_System_ice
import omero_Collections_ice
import omero_model_Shape_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if 'Roi' not in _M_omero.model.__dict__:
    _M_omero.model._t_Roi = IcePy.declareClass('::omero::model::Roi')
    _M_omero.model._t_RoiPrx = IcePy.declareProxy('::omero::model::Roi')

if 'AffineTransform' not in _M_omero.model.__dict__:
    _M_omero.model._t_AffineTransform = IcePy.declareClass('::omero::model::AffineTransform')
    _M_omero.model._t_AffineTransformPrx = IcePy.declareProxy('::omero::model::AffineTransform')

if 'Length' not in _M_omero.model.__dict__:
    _M_omero.model._t_Length = IcePy.declareClass('::omero::model::Length')
    _M_omero.model._t_LengthPrx = IcePy.declareProxy('::omero::model::Length')

if 'ShapeAnnotationLink' not in _M_omero.model.__dict__:
    _M_omero.model._t_ShapeAnnotationLink = IcePy.declareClass('::omero::model::ShapeAnnotationLink')
    _M_omero.model._t_ShapeAnnotationLinkPrx = IcePy.declareProxy('::omero::model::ShapeAnnotationLink')

if 'Annotation' not in _M_omero.model.__dict__:
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'Line' not in _M_omero.model.__dict__:
    _M_omero.model.Line = Ice.createTempClass()
    class Line(_M_omero.model.Shape):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _theZ=None, _theT=None, _theC=None, _roi=None, _locked=None, _transform=None, _fillColor=None, _fillRule=None, _strokeColor=None, _strokeDashArray=None, _strokeWidth=None, _fontFamily=None, _fontSize=None, _fontStyle=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None, _x1=None, _y1=None, _x2=None, _y2=None, _markerStart=None, _markerEnd=None, _textValue=None):
            if Ice.getType(self) == _M_omero.model.Line:
                raise RuntimeError('omero.model.Line is an abstract class')
            _M_omero.model.Shape.__init__(self, _id, _details, _loaded, _version, _theZ, _theT, _theC, _roi, _locked, _transform, _fillColor, _fillRule, _strokeColor, _strokeDashArray, _strokeWidth, _fontFamily, _fontSize, _fontStyle, _annotationLinksSeq, _annotationLinksLoaded, _annotationLinksCountPerOwner)
            self._x1 = _x1
            self._y1 = _y1
            self._x2 = _x2
            self._y2 = _y2
            self._markerStart = _markerStart
            self._markerEnd = _markerEnd
            self._textValue = _textValue

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::Line', '::omero::model::Shape')

        def ice_id(self, current=None):
            return '::omero::model::Line'

        def ice_staticId():
            return '::omero::model::Line'
        ice_staticId = staticmethod(ice_staticId)

        def getX1(self, current=None):
            pass

        def setX1(self, theX1, current=None):
            pass

        def getY1(self, current=None):
            pass

        def setY1(self, theY1, current=None):
            pass

        def getX2(self, current=None):
            pass

        def setX2(self, theX2, current=None):
            pass

        def getY2(self, current=None):
            pass

        def setY2(self, theY2, current=None):
            pass

        def getMarkerStart(self, current=None):
            pass

        def setMarkerStart(self, theMarkerStart, current=None):
            pass

        def getMarkerEnd(self, current=None):
            pass

        def setMarkerEnd(self, theMarkerEnd, current=None):
            pass

        def getTextValue(self, current=None):
            pass

        def setTextValue(self, theTextValue, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Line)

        __repr__ = __str__

    _M_omero.model.LinePrx = Ice.createTempClass()
    class LinePrx(_M_omero.model.ShapePrx):

        def getX1(self, _ctx=None):
            return _M_omero.model.Line._op_getX1.invoke(self, ((), _ctx))

        def begin_getX1(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_getX1.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getX1(self, _r):
            return _M_omero.model.Line._op_getX1.end(self, _r)

        def setX1(self, theX1, _ctx=None):
            return _M_omero.model.Line._op_setX1.invoke(self, ((theX1, ), _ctx))

        def begin_setX1(self, theX1, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_setX1.begin(self, ((theX1, ), _response, _ex, _sent, _ctx))

        def end_setX1(self, _r):
            return _M_omero.model.Line._op_setX1.end(self, _r)

        def getY1(self, _ctx=None):
            return _M_omero.model.Line._op_getY1.invoke(self, ((), _ctx))

        def begin_getY1(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_getY1.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getY1(self, _r):
            return _M_omero.model.Line._op_getY1.end(self, _r)

        def setY1(self, theY1, _ctx=None):
            return _M_omero.model.Line._op_setY1.invoke(self, ((theY1, ), _ctx))

        def begin_setY1(self, theY1, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_setY1.begin(self, ((theY1, ), _response, _ex, _sent, _ctx))

        def end_setY1(self, _r):
            return _M_omero.model.Line._op_setY1.end(self, _r)

        def getX2(self, _ctx=None):
            return _M_omero.model.Line._op_getX2.invoke(self, ((), _ctx))

        def begin_getX2(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_getX2.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getX2(self, _r):
            return _M_omero.model.Line._op_getX2.end(self, _r)

        def setX2(self, theX2, _ctx=None):
            return _M_omero.model.Line._op_setX2.invoke(self, ((theX2, ), _ctx))

        def begin_setX2(self, theX2, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_setX2.begin(self, ((theX2, ), _response, _ex, _sent, _ctx))

        def end_setX2(self, _r):
            return _M_omero.model.Line._op_setX2.end(self, _r)

        def getY2(self, _ctx=None):
            return _M_omero.model.Line._op_getY2.invoke(self, ((), _ctx))

        def begin_getY2(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_getY2.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getY2(self, _r):
            return _M_omero.model.Line._op_getY2.end(self, _r)

        def setY2(self, theY2, _ctx=None):
            return _M_omero.model.Line._op_setY2.invoke(self, ((theY2, ), _ctx))

        def begin_setY2(self, theY2, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_setY2.begin(self, ((theY2, ), _response, _ex, _sent, _ctx))

        def end_setY2(self, _r):
            return _M_omero.model.Line._op_setY2.end(self, _r)

        def getMarkerStart(self, _ctx=None):
            return _M_omero.model.Line._op_getMarkerStart.invoke(self, ((), _ctx))

        def begin_getMarkerStart(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_getMarkerStart.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getMarkerStart(self, _r):
            return _M_omero.model.Line._op_getMarkerStart.end(self, _r)

        def setMarkerStart(self, theMarkerStart, _ctx=None):
            return _M_omero.model.Line._op_setMarkerStart.invoke(self, ((theMarkerStart, ), _ctx))

        def begin_setMarkerStart(self, theMarkerStart, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_setMarkerStart.begin(self, ((theMarkerStart, ), _response, _ex, _sent, _ctx))

        def end_setMarkerStart(self, _r):
            return _M_omero.model.Line._op_setMarkerStart.end(self, _r)

        def getMarkerEnd(self, _ctx=None):
            return _M_omero.model.Line._op_getMarkerEnd.invoke(self, ((), _ctx))

        def begin_getMarkerEnd(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_getMarkerEnd.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getMarkerEnd(self, _r):
            return _M_omero.model.Line._op_getMarkerEnd.end(self, _r)

        def setMarkerEnd(self, theMarkerEnd, _ctx=None):
            return _M_omero.model.Line._op_setMarkerEnd.invoke(self, ((theMarkerEnd, ), _ctx))

        def begin_setMarkerEnd(self, theMarkerEnd, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_setMarkerEnd.begin(self, ((theMarkerEnd, ), _response, _ex, _sent, _ctx))

        def end_setMarkerEnd(self, _r):
            return _M_omero.model.Line._op_setMarkerEnd.end(self, _r)

        def getTextValue(self, _ctx=None):
            return _M_omero.model.Line._op_getTextValue.invoke(self, ((), _ctx))

        def begin_getTextValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_getTextValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTextValue(self, _r):
            return _M_omero.model.Line._op_getTextValue.end(self, _r)

        def setTextValue(self, theTextValue, _ctx=None):
            return _M_omero.model.Line._op_setTextValue.invoke(self, ((theTextValue, ), _ctx))

        def begin_setTextValue(self, theTextValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Line._op_setTextValue.begin(self, ((theTextValue, ), _response, _ex, _sent, _ctx))

        def end_setTextValue(self, _r):
            return _M_omero.model.Line._op_setTextValue.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.LinePrx.ice_checkedCast(proxy, '::omero::model::Line', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.LinePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::Line'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_LinePrx = IcePy.defineProxy('::omero::model::Line', LinePrx)

    _M_omero.model._t_Line = IcePy.declareClass('::omero::model::Line')

    _M_omero.model._t_Line = IcePy.defineClass('::omero::model::Line', Line, -1, (), True, False, _M_omero.model._t_Shape, (), (
        ('_x1', (), _M_omero._t_RDouble, False, 0),
        ('_y1', (), _M_omero._t_RDouble, False, 0),
        ('_x2', (), _M_omero._t_RDouble, False, 0),
        ('_y2', (), _M_omero._t_RDouble, False, 0),
        ('_markerStart', (), _M_omero._t_RString, False, 0),
        ('_markerEnd', (), _M_omero._t_RString, False, 0),
        ('_textValue', (), _M_omero._t_RString, False, 0)
    ))
    Line._ice_type = _M_omero.model._t_Line

    Line._op_getX1 = IcePy.Operation('getX1', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Line._op_setX1 = IcePy.Operation('setX1', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Line._op_getY1 = IcePy.Operation('getY1', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Line._op_setY1 = IcePy.Operation('setY1', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Line._op_getX2 = IcePy.Operation('getX2', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Line._op_setX2 = IcePy.Operation('setX2', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Line._op_getY2 = IcePy.Operation('getY2', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RDouble, False, 0), ())
    Line._op_setY2 = IcePy.Operation('setY2', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RDouble, False, 0),), (), None, ())
    Line._op_getMarkerStart = IcePy.Operation('getMarkerStart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Line._op_setMarkerStart = IcePy.Operation('setMarkerStart', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Line._op_getMarkerEnd = IcePy.Operation('getMarkerEnd', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Line._op_setMarkerEnd = IcePy.Operation('setMarkerEnd', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Line._op_getTextValue = IcePy.Operation('getTextValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Line._op_setTextValue = IcePy.Operation('setTextValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())

    _M_omero.model.Line = Line
    del Line

    _M_omero.model.LinePrx = LinePrx
    del LinePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
