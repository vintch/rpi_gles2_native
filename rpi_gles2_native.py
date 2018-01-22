# Simple transparent wrapper of the Raspberry Pi's GLESv2 library for python
# Code was auto generated from RPi's /opt/vc/include/GLES2/gl2.h
# License: Copyleft

GLES2_LIB = "/opt/vc/lib/libbrcmGLESv2.so"

#####################################################################

from ctypes import CDLL, POINTER, c_void_p, c_char, c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint, c_long, c_float

GLvoid_p = c_void_p
GLvoid_p_p = POINTER(GLvoid_p)
GLenum = c_uint
GLenum_p = POINTER(GLenum)
GLboolean = c_ubyte
GLboolean_p = POINTER(GLboolean)
GLbyte = c_byte
GLbyte_p = POINTER(GLbyte)
GLchar = c_char
GLchar_p = POINTER(c_char)
GLchar_p_p = POINTER(GLchar_p)
GLshort = c_short
GLshort_p = POINTER(GLshort)
GLint = c_int
GLint_p = POINTER(GLint)
GLubyte = c_ubyte
GLubyte_p = POINTER(GLubyte)
GLushort = c_ushort
GLushort_p = POINTER(GLushort)
GLuint = c_uint
GLuint_p = POINTER(GLuint)
GLbitfield = c_uint
GLfloat = c_float
GLfloat_p = POINTER(GLfloat)
GLclampf = c_float
GLintptr = c_long
GLintptr_p = POINTER(GLintptr)
GLsizeiptr = c_long
GLsizeiptr_p = POINTER(GLsizeiptr)
GLsizei = c_int
GLsizei_p = POINTER(GLsizei)

gles2 = CDLL(GLES2_LIB)

#####################################################################

GL_ES_VERSION_2_0 = 1
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_COLOR_BUFFER_BIT = 0x00004000
GL_POINTS = 0x0000
GL_LINES = 0x0001
GL_LINE_LOOP = 0x0002
GL_LINE_STRIP = 0x0003
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_TRIANGLE_FAN = 0x0006
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 0x0300
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_SRC_ALPHA = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_DST_ALPHA = 0x0304
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308
GL_FUNC_ADD = 0x8006
GL_BLEND_EQUATION = 0x8009
GL_BLEND_EQUATION_RGB = 0x8009
GL_BLEND_EQUATION_ALPHA = 0x883D
GL_FUNC_SUBTRACT = 0x800A
GL_FUNC_REVERSE_SUBTRACT = 0x800B
GL_BLEND_DST_RGB = 0x80C8
GL_BLEND_SRC_RGB = 0x80C9
GL_BLEND_DST_ALPHA = 0x80CA
GL_BLEND_SRC_ALPHA = 0x80CB
GL_CONSTANT_COLOR = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
GL_CONSTANT_ALPHA = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
GL_BLEND_COLOR = 0x8005
GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_ARRAY_BUFFER_BINDING = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
GL_STREAM_DRAW = 0x88E0
GL_STATIC_DRAW = 0x88E4
GL_DYNAMIC_DRAW = 0x88E8
GL_BUFFER_SIZE = 0x8764
GL_BUFFER_USAGE = 0x8765
GL_CURRENT_VERTEX_ATTRIB = 0x8626
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_FRONT_AND_BACK = 0x0408
GL_TEXTURE_2D = 0x0DE1
GL_CULL_FACE = 0x0B44
GL_BLEND = 0x0BE2
GL_DITHER = 0x0BD0
GL_STENCIL_TEST = 0x0B90
GL_DEPTH_TEST = 0x0B71
GL_SCISSOR_TEST = 0x0C11
GL_POLYGON_OFFSET_FILL = 0x8037
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
GL_SAMPLE_COVERAGE = 0x80A0
GL_NO_ERROR = 0
GL_INVALID_ENUM = 0x0500
GL_INVALID_VALUE = 0x0501
GL_INVALID_OPERATION = 0x0502
GL_OUT_OF_MEMORY = 0x0505
GL_CW = 0x0900
GL_CCW = 0x0901
GL_LINE_WIDTH = 0x0B21
GL_ALIASED_POINT_SIZE_RANGE = 0x846D
GL_ALIASED_LINE_WIDTH_RANGE = 0x846E
GL_CULL_FACE_MODE = 0x0B45
GL_FRONT_FACE = 0x0B46
GL_DEPTH_RANGE = 0x0B70
GL_DEPTH_WRITEMASK = 0x0B72
GL_DEPTH_CLEAR_VALUE = 0x0B73
GL_DEPTH_FUNC = 0x0B74
GL_STENCIL_CLEAR_VALUE = 0x0B91
GL_STENCIL_FUNC = 0x0B92
GL_STENCIL_FAIL = 0x0B94
GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
GL_STENCIL_REF = 0x0B97
GL_STENCIL_VALUE_MASK = 0x0B93
GL_STENCIL_WRITEMASK = 0x0B98
GL_STENCIL_BACK_FUNC = 0x8800
GL_STENCIL_BACK_FAIL = 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
GL_STENCIL_BACK_REF = 0x8CA3
GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
GL_STENCIL_BACK_WRITEMASK = 0x8CA5
GL_VIEWPORT = 0x0BA2
GL_SCISSOR_BOX = 0x0C10
GL_COLOR_CLEAR_VALUE = 0x0C22
GL_COLOR_WRITEMASK = 0x0C23
GL_UNPACK_ALIGNMENT = 0x0CF5
GL_PACK_ALIGNMENT = 0x0D05
GL_MAX_TEXTURE_SIZE = 0x0D33
GL_MAX_VIEWPORT_DIMS = 0x0D3A
GL_SUBPIXEL_BITS = 0x0D50
GL_RED_BITS = 0x0D52
GL_GREEN_BITS = 0x0D53
GL_BLUE_BITS = 0x0D54
GL_ALPHA_BITS = 0x0D55
GL_DEPTH_BITS = 0x0D56
GL_STENCIL_BITS = 0x0D57
GL_POLYGON_OFFSET_UNITS = 0x2A00
GL_POLYGON_OFFSET_FACTOR = 0x8038
GL_TEXTURE_BINDING_2D = 0x8069
GL_SAMPLE_BUFFERS = 0x80A8
GL_SAMPLES = 0x80A9
GL_SAMPLE_COVERAGE_VALUE = 0x80AA
GL_SAMPLE_COVERAGE_INVERT = 0x80AB
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102
GL_GENERATE_MIPMAP_HINT = 0x8192
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_FIXED = 0x140C
GL_DEPTH_COMPONENT = 0x1902
GL_ALPHA = 0x1906
GL_RGB = 0x1907
GL_RGBA = 0x1908
GL_LUMINANCE = 0x1909
GL_LUMINANCE_ALPHA = 0x190A
GL_UNSIGNED_SHORT_4_4_4_4 = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1 = 0x8034
GL_UNSIGNED_SHORT_5_6_5 = 0x8363
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_MAX_VERTEX_ATTRIBS = 0x8869
GL_MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
GL_MAX_VARYING_VECTORS = 0x8DFC
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
GL_SHADER_TYPE = 0x8B4F
GL_DELETE_STATUS = 0x8B80
GL_LINK_STATUS = 0x8B82
GL_VALIDATE_STATUS = 0x8B83
GL_ATTACHED_SHADERS = 0x8B85
GL_ACTIVE_UNIFORMS = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
GL_ACTIVE_ATTRIBUTES = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
GL_SHADING_LANGUAGE_VERSION = 0x8B8C
GL_CURRENT_PROGRAM = 0x8B8D
GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207
GL_KEEP = 0x1E00
GL_REPLACE = 0x1E01
GL_INCR = 0x1E02
GL_DECR = 0x1E03
GL_INVERT = 0x150A
GL_INCR_WRAP = 0x8507
GL_DECR_WRAP = 0x8508
GL_VENDOR = 0x1F00
GL_RENDERER = 0x1F01
GL_VERSION = 0x1F02
GL_EXTENSIONS = 0x1F03
GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_TEXTURE = 0x1702
GL_TEXTURE_CUBE_MAP = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE2 = 0x84C2
GL_TEXTURE3 = 0x84C3
GL_TEXTURE4 = 0x84C4
GL_TEXTURE5 = 0x84C5
GL_TEXTURE6 = 0x84C6
GL_TEXTURE7 = 0x84C7
GL_TEXTURE8 = 0x84C8
GL_TEXTURE9 = 0x84C9
GL_TEXTURE10 = 0x84CA
GL_TEXTURE11 = 0x84CB
GL_TEXTURE12 = 0x84CC
GL_TEXTURE13 = 0x84CD
GL_TEXTURE14 = 0x84CE
GL_TEXTURE15 = 0x84CF
GL_TEXTURE16 = 0x84D0
GL_TEXTURE17 = 0x84D1
GL_TEXTURE18 = 0x84D2
GL_TEXTURE19 = 0x84D3
GL_TEXTURE20 = 0x84D4
GL_TEXTURE21 = 0x84D5
GL_TEXTURE22 = 0x84D6
GL_TEXTURE23 = 0x84D7
GL_TEXTURE24 = 0x84D8
GL_TEXTURE25 = 0x84D9
GL_TEXTURE26 = 0x84DA
GL_TEXTURE27 = 0x84DB
GL_TEXTURE28 = 0x84DC
GL_TEXTURE29 = 0x84DD
GL_TEXTURE30 = 0x84DE
GL_TEXTURE31 = 0x84DF
GL_ACTIVE_TEXTURE = 0x84E0
GL_REPEAT = 0x2901
GL_CLAMP_TO_EDGE = 0x812F
GL_MIRRORED_REPEAT = 0x8370
GL_FLOAT_VEC2 = 0x8B50
GL_FLOAT_VEC3 = 0x8B51
GL_FLOAT_VEC4 = 0x8B52
GL_INT_VEC2 = 0x8B53
GL_INT_VEC3 = 0x8B54
GL_INT_VEC4 = 0x8B55
GL_BOOL = 0x8B56
GL_BOOL_VEC2 = 0x8B57
GL_BOOL_VEC3 = 0x8B58
GL_BOOL_VEC4 = 0x8B59
GL_FLOAT_MAT2 = 0x8B5A
GL_FLOAT_MAT3 = 0x8B5B
GL_FLOAT_MAT4 = 0x8B5C
GL_SAMPLER_2D = 0x8B5E
GL_SAMPLER_CUBE = 0x8B60
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
GL_FALSE = 0
GL_TRUE = 1
GL_COMPILE_STATUS = 0x8B81
GL_INFO_LOG_LENGTH = 0x8B84
GL_SHADER_SOURCE_LENGTH = 0x8B88
GL_SHADER_COMPILER = 0x8DFA
GL_SHADER_BINARY_FORMATS = 0x8DF8
GL_NUM_SHADER_BINARY_FORMATS = 0x8DF9
GL_LOW_FLOAT = 0x8DF0
GL_MEDIUM_FLOAT = 0x8DF1
GL_HIGH_FLOAT = 0x8DF2
GL_LOW_INT = 0x8DF3
GL_MEDIUM_INT = 0x8DF4
GL_HIGH_INT = 0x8DF5
GL_FRAMEBUFFER = 0x8D40
GL_RENDERBUFFER = 0x8D41
GL_RGBA4 = 0x8056
GL_RGB5_A1 = 0x8057
GL_RGB565 = 0x8D62
GL_DEPTH_COMPONENT16 = 0x81A5
GL_STENCIL_INDEX = 0x1901
GL_STENCIL_INDEX8 = 0x8D48
GL_RENDERBUFFER_WIDTH = 0x8D42
GL_RENDERBUFFER_HEIGHT = 0x8D43
GL_RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
GL_RENDERBUFFER_RED_SIZE = 0x8D50
GL_RENDERBUFFER_GREEN_SIZE = 0x8D51
GL_RENDERBUFFER_BLUE_SIZE = 0x8D52
GL_RENDERBUFFER_ALPHA_SIZE = 0x8D53
GL_RENDERBUFFER_DEPTH_SIZE = 0x8D54
GL_RENDERBUFFER_STENCIL_SIZE = 0x8D55
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
GL_COLOR_ATTACHMENT0 = 0x8CE0
GL_DEPTH_ATTACHMENT = 0x8D00
GL_STENCIL_ATTACHMENT = 0x8D20
GL_NONE = 0
GL_FRAMEBUFFER_COMPLETE = 0x8CD5
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 0x8CD9
GL_FRAMEBUFFER_UNSUPPORTED = 0x8CDD
GL_FRAMEBUFFER_BINDING = 0x8CA6
GL_RENDERBUFFER_BINDING = 0x8CA7
GL_MAX_RENDERBUFFER_SIZE = 0x84E8
GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506

###############################################################################

GLES2_ERRORS_CHECK = True

class GLES2Error(Exception):
    def __init__(self, errcode, func_name, func_res):
        err_consts = [key for key, value in globals().items() if type(value) is int and value == errcode]
        msg = "OpenGL error {:#04x} ({}) in function '{}', returned '{}'".format(errcode, err_consts, func_name, func_res)
        super().__init__(msg)


def gles2_errcheck(res, func, *args):
    if GLES2_ERRORS_CHECK:
        err = glGetError()
        if err != GL_NO_ERROR:
            raise GLES2Error(err, func.__name__, res)
    return res

###############################################################################

""" GL_APICALL void         GL_APIENTRY glActiveTexture (GLenum texture); """
gles2.glActiveTexture.restype = None
gles2.glActiveTexture.argtypes = (GLenum,)  # texture
gles2.glActiveTexture.errcheck = gles2_errcheck
glActiveTexture = gles2.glActiveTexture

""" GL_APICALL void         GL_APIENTRY glAttachShader (GLuint program, GLuint shader); """
gles2.glAttachShader.restype = None
gles2.glAttachShader.argtypes = (GLuint, GLuint)  # program, shader
gles2.glAttachShader.errcheck = gles2_errcheck
glAttachShader = gles2.glAttachShader

""" GL_APICALL void         GL_APIENTRY glBindAttribLocation (GLuint program, GLuint index, const GLchar* name); """
gles2.glBindAttribLocation.restype = None
gles2.glBindAttribLocation.argtypes = (GLuint, GLuint, GLchar_p)  # program, index, name
gles2.glBindAttribLocation.errcheck = gles2_errcheck
glBindAttribLocation = gles2.glBindAttribLocation

""" GL_APICALL void         GL_APIENTRY glBindBuffer (GLenum target, GLuint buffer); """
gles2.glBindBuffer.restype = None
gles2.glBindBuffer.argtypes = (GLenum, GLuint)  # target, buffer
gles2.glBindBuffer.errcheck = gles2_errcheck
glBindBuffer = gles2.glBindBuffer

""" GL_APICALL void         GL_APIENTRY glBindFramebuffer (GLenum target, GLuint framebuffer); """
gles2.glBindFramebuffer.restype = None
gles2.glBindFramebuffer.argtypes = (GLenum, GLuint)  # target, framebuffer
gles2.glBindFramebuffer.errcheck = gles2_errcheck
glBindFramebuffer = gles2.glBindFramebuffer

""" GL_APICALL void         GL_APIENTRY glBindRenderbuffer (GLenum target, GLuint renderbuffer); """
gles2.glBindRenderbuffer.restype = None
gles2.glBindRenderbuffer.argtypes = (GLenum, GLuint)  # target, renderbuffer
gles2.glBindRenderbuffer.errcheck = gles2_errcheck
glBindRenderbuffer = gles2.glBindRenderbuffer

""" GL_APICALL void         GL_APIENTRY glBindTexture (GLenum target, GLuint texture); """
gles2.glBindTexture.restype = None
gles2.glBindTexture.argtypes = (GLenum, GLuint)  # target, texture
gles2.glBindTexture.errcheck = gles2_errcheck
glBindTexture = gles2.glBindTexture

""" GL_APICALL void         GL_APIENTRY glBlendColor (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha); """
gles2.glBlendColor.restype = None
gles2.glBlendColor.argtypes = (GLclampf, GLclampf, GLclampf, GLclampf)  # red, green, blue, alpha
gles2.glBlendColor.errcheck = gles2_errcheck
glBlendColor = gles2.glBlendColor

""" GL_APICALL void         GL_APIENTRY glBlendEquation ( GLenum mode ); """
gles2.glBlendEquation.restype = None
gles2.glBlendEquation.argtypes = (GLenum,)  # mode
gles2.glBlendEquation.errcheck = gles2_errcheck
glBlendEquation = gles2.glBlendEquation

""" GL_APICALL void         GL_APIENTRY glBlendEquationSeparate (GLenum modeRGB, GLenum modeAlpha); """
gles2.glBlendEquationSeparate.restype = None
gles2.glBlendEquationSeparate.argtypes = (GLenum, GLenum)  # modeRGB, modeAlpha
gles2.glBlendEquationSeparate.errcheck = gles2_errcheck
glBlendEquationSeparate = gles2.glBlendEquationSeparate

""" GL_APICALL void         GL_APIENTRY glBlendFunc (GLenum sfactor, GLenum dfactor); """
gles2.glBlendFunc.restype = None
gles2.glBlendFunc.argtypes = (GLenum, GLenum)  # sfactor, dfactor
gles2.glBlendFunc.errcheck = gles2_errcheck
glBlendFunc = gles2.glBlendFunc

""" GL_APICALL void         GL_APIENTRY glBlendFuncSeparate (GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha); """
gles2.glBlendFuncSeparate.restype = None
gles2.glBlendFuncSeparate.argtypes = (GLenum, GLenum, GLenum, GLenum)  # srcRGB, dstRGB, srcAlpha, dstAlpha
gles2.glBlendFuncSeparate.errcheck = gles2_errcheck
glBlendFuncSeparate = gles2.glBlendFuncSeparate

""" GL_APICALL void         GL_APIENTRY glBufferData (GLenum target, GLsizeiptr size, const GLvoid* data, GLenum usage); """
gles2.glBufferData.restype = None
gles2.glBufferData.argtypes = (GLenum, GLsizeiptr, GLvoid_p, GLenum)  # target, size, data, usage
gles2.glBufferData.errcheck = gles2_errcheck
glBufferData = gles2.glBufferData

""" GL_APICALL void         GL_APIENTRY glBufferSubData (GLenum target, GLintptr offset, GLsizeiptr size, const GLvoid* data); """
gles2.glBufferSubData.restype = None
gles2.glBufferSubData.argtypes = (GLenum, GLintptr, GLsizeiptr, GLvoid_p)  # target, offset, size, data
gles2.glBufferSubData.errcheck = gles2_errcheck
glBufferSubData = gles2.glBufferSubData

""" GL_APICALL GLenum       GL_APIENTRY glCheckFramebufferStatus (GLenum target); """
gles2.glCheckFramebufferStatus.restype = GLenum
gles2.glCheckFramebufferStatus.argtypes = (GLenum,)  # target
gles2.glCheckFramebufferStatus.errcheck = gles2_errcheck
glCheckFramebufferStatus = gles2.glCheckFramebufferStatus

""" GL_APICALL void         GL_APIENTRY glClear (GLbitfield mask); """
gles2.glClear.restype = None
gles2.glClear.argtypes = (GLbitfield,)  # mask
gles2.glClear.errcheck = gles2_errcheck
glClear = gles2.glClear

""" GL_APICALL void         GL_APIENTRY glClearColor (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha); """
gles2.glClearColor.restype = None
gles2.glClearColor.argtypes = (GLclampf, GLclampf, GLclampf, GLclampf)  # red, green, blue, alpha
gles2.glClearColor.errcheck = gles2_errcheck
glClearColor = gles2.glClearColor

""" GL_APICALL void         GL_APIENTRY glClearDepthf (GLclampf depth); """
gles2.glClearDepthf.restype = None
gles2.glClearDepthf.argtypes = (GLclampf,)  # depth
gles2.glClearDepthf.errcheck = gles2_errcheck
glClearDepthf = gles2.glClearDepthf

""" GL_APICALL void         GL_APIENTRY glClearStencil (GLint s); """
gles2.glClearStencil.restype = None
gles2.glClearStencil.argtypes = (GLint,)  # s
gles2.glClearStencil.errcheck = gles2_errcheck
glClearStencil = gles2.glClearStencil

""" GL_APICALL void         GL_APIENTRY glColorMask (GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha); """
gles2.glColorMask.restype = None
gles2.glColorMask.argtypes = (GLboolean, GLboolean, GLboolean, GLboolean)  # red, green, blue, alpha
gles2.glColorMask.errcheck = gles2_errcheck
glColorMask = gles2.glColorMask

""" GL_APICALL void         GL_APIENTRY glCompileShader (GLuint shader); """
gles2.glCompileShader.restype = None
gles2.glCompileShader.argtypes = (GLuint,)  # shader
gles2.glCompileShader.errcheck = gles2_errcheck
glCompileShader = gles2.glCompileShader

""" GL_APICALL void         GL_APIENTRY glCompressedTexImage2D (GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const GLvoid* data); """
gles2.glCompressedTexImage2D.restype = None
gles2.glCompressedTexImage2D.argtypes = (GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, GLvoid_p)  # target, level, internalformat, width, height, border, imageSize, data
gles2.glCompressedTexImage2D.errcheck = gles2_errcheck
glCompressedTexImage2D = gles2.glCompressedTexImage2D

""" GL_APICALL void         GL_APIENTRY glCompressedTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const GLvoid* data); """
gles2.glCompressedTexSubImage2D.restype = None
gles2.glCompressedTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, GLvoid_p)  # target, level, xoffset, yoffset, width, height, format, imageSize, data
gles2.glCompressedTexSubImage2D.errcheck = gles2_errcheck
glCompressedTexSubImage2D = gles2.glCompressedTexSubImage2D

""" GL_APICALL void         GL_APIENTRY glCopyTexImage2D (GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border); """
gles2.glCopyTexImage2D.restype = None
gles2.glCopyTexImage2D.argtypes = (GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint)  # target, level, internalformat, x, y, width, height, border
gles2.glCopyTexImage2D.errcheck = gles2_errcheck
glCopyTexImage2D = gles2.glCopyTexImage2D

""" GL_APICALL void         GL_APIENTRY glCopyTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height); """
gles2.glCopyTexSubImage2D.restype = None
gles2.glCopyTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei)  # target, level, xoffset, yoffset, x, y, width, height
gles2.glCopyTexSubImage2D.errcheck = gles2_errcheck
glCopyTexSubImage2D = gles2.glCopyTexSubImage2D

""" GL_APICALL GLuint       GL_APIENTRY glCreateProgram (void); """
gles2.glCreateProgram.restype = GLuint
gles2.glCreateProgram.argtypes = ()  #
gles2.glCreateProgram.errcheck = gles2_errcheck
glCreateProgram = gles2.glCreateProgram

""" GL_APICALL GLuint       GL_APIENTRY glCreateShader (GLenum type); """
gles2.glCreateShader.restype = GLuint
gles2.glCreateShader.argtypes = (GLenum,)  # type
gles2.glCreateShader.errcheck = gles2_errcheck
glCreateShader = gles2.glCreateShader

""" GL_APICALL void         GL_APIENTRY glCullFace (GLenum mode); """
gles2.glCullFace.restype = None
gles2.glCullFace.argtypes = (GLenum,)  # mode
gles2.glCullFace.errcheck = gles2_errcheck
glCullFace = gles2.glCullFace

""" GL_APICALL void         GL_APIENTRY glDeleteBuffers (GLsizei n, const GLuint* buffers); """
gles2.glDeleteBuffers.restype = None
gles2.glDeleteBuffers.argtypes = (GLsizei, GLuint_p)  # n, buffers
gles2.glDeleteBuffers.errcheck = gles2_errcheck
glDeleteBuffers = gles2.glDeleteBuffers

""" GL_APICALL void         GL_APIENTRY glDeleteFramebuffers (GLsizei n, const GLuint* framebuffers); """
gles2.glDeleteFramebuffers.restype = None
gles2.glDeleteFramebuffers.argtypes = (GLsizei, GLuint_p)  # n, framebuffers
gles2.glDeleteFramebuffers.errcheck = gles2_errcheck
glDeleteFramebuffers = gles2.glDeleteFramebuffers

""" GL_APICALL void         GL_APIENTRY glDeleteProgram (GLuint program); """
gles2.glDeleteProgram.restype = None
gles2.glDeleteProgram.argtypes = (GLuint,)  # program
gles2.glDeleteProgram.errcheck = gles2_errcheck
glDeleteProgram = gles2.glDeleteProgram

""" GL_APICALL void         GL_APIENTRY glDeleteRenderbuffers (GLsizei n, const GLuint* renderbuffers); """
gles2.glDeleteRenderbuffers.restype = None
gles2.glDeleteRenderbuffers.argtypes = (GLsizei, GLuint_p)  # n, renderbuffers
gles2.glDeleteRenderbuffers.errcheck = gles2_errcheck
glDeleteRenderbuffers = gles2.glDeleteRenderbuffers

""" GL_APICALL void         GL_APIENTRY glDeleteShader (GLuint shader); """
gles2.glDeleteShader.restype = None
gles2.glDeleteShader.argtypes = (GLuint,)  # shader
gles2.glDeleteShader.errcheck = gles2_errcheck
glDeleteShader = gles2.glDeleteShader

""" GL_APICALL void         GL_APIENTRY glDeleteTextures (GLsizei n, const GLuint* textures); """
gles2.glDeleteTextures.restype = None
gles2.glDeleteTextures.argtypes = (GLsizei, GLuint_p)  # n, textures
gles2.glDeleteTextures.errcheck = gles2_errcheck
glDeleteTextures = gles2.glDeleteTextures

""" GL_APICALL void         GL_APIENTRY glDepthFunc (GLenum func); """
gles2.glDepthFunc.restype = None
gles2.glDepthFunc.argtypes = (GLenum,)  # func
gles2.glDepthFunc.errcheck = gles2_errcheck
glDepthFunc = gles2.glDepthFunc

""" GL_APICALL void         GL_APIENTRY glDepthMask (GLboolean flag); """
gles2.glDepthMask.restype = None
gles2.glDepthMask.argtypes = (GLboolean,)  # flag
gles2.glDepthMask.errcheck = gles2_errcheck
glDepthMask = gles2.glDepthMask

""" GL_APICALL void         GL_APIENTRY glDepthRangef (GLclampf zNear, GLclampf zFar); """
gles2.glDepthRangef.restype = None
gles2.glDepthRangef.argtypes = (GLclampf, GLclampf)  # zNear, zFar
gles2.glDepthRangef.errcheck = gles2_errcheck
glDepthRangef = gles2.glDepthRangef

""" GL_APICALL void         GL_APIENTRY glDetachShader (GLuint program, GLuint shader); """
gles2.glDetachShader.restype = None
gles2.glDetachShader.argtypes = (GLuint, GLuint)  # program, shader
gles2.glDetachShader.errcheck = gles2_errcheck
glDetachShader = gles2.glDetachShader

""" GL_APICALL void         GL_APIENTRY glDisable (GLenum cap); """
gles2.glDisable.restype = None
gles2.glDisable.argtypes = (GLenum,)  # cap
gles2.glDisable.errcheck = gles2_errcheck
glDisable = gles2.glDisable

""" GL_APICALL void         GL_APIENTRY glDisableVertexAttribArray (GLuint index); """
gles2.glDisableVertexAttribArray.restype = None
gles2.glDisableVertexAttribArray.argtypes = (GLuint,)  # index
gles2.glDisableVertexAttribArray.errcheck = gles2_errcheck
glDisableVertexAttribArray = gles2.glDisableVertexAttribArray

""" GL_APICALL void         GL_APIENTRY glDrawArrays (GLenum mode, GLint first, GLsizei count); """
gles2.glDrawArrays.restype = None
gles2.glDrawArrays.argtypes = (GLenum, GLint, GLsizei)  # mode, first, count
gles2.glDrawArrays.errcheck = gles2_errcheck
glDrawArrays = gles2.glDrawArrays

""" GL_APICALL void         GL_APIENTRY glDrawElements (GLenum mode, GLsizei count, GLenum type, const GLvoid* indices); """
gles2.glDrawElements.restype = None
gles2.glDrawElements.argtypes = (GLenum, GLsizei, GLenum, GLvoid_p)  # mode, count, type, indices
gles2.glDrawElements.errcheck = gles2_errcheck
glDrawElements = gles2.glDrawElements

""" GL_APICALL void         GL_APIENTRY glEnable (GLenum cap); """
gles2.glEnable.restype = None
gles2.glEnable.argtypes = (GLenum,)  # cap
gles2.glEnable.errcheck = gles2_errcheck
glEnable = gles2.glEnable

""" GL_APICALL void         GL_APIENTRY glEnableVertexAttribArray (GLuint index); """
gles2.glEnableVertexAttribArray.restype = None
gles2.glEnableVertexAttribArray.argtypes = (GLuint,)  # index
gles2.glEnableVertexAttribArray.errcheck = gles2_errcheck
glEnableVertexAttribArray = gles2.glEnableVertexAttribArray

""" GL_APICALL void         GL_APIENTRY glFinish (void); """
gles2.glFinish.restype = None
gles2.glFinish.argtypes = ()  #
gles2.glFinish.errcheck = gles2_errcheck
glFinish = gles2.glFinish

""" GL_APICALL void         GL_APIENTRY glFlush (void); """
gles2.glFlush.restype = None
gles2.glFlush.argtypes = ()  #
gles2.glFlush.errcheck = gles2_errcheck
glFlush = gles2.glFlush

""" GL_APICALL void         GL_APIENTRY glFramebufferRenderbuffer (GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer); """
gles2.glFramebufferRenderbuffer.restype = None
gles2.glFramebufferRenderbuffer.argtypes = (GLenum, GLenum, GLenum, GLuint)  # target, attachment, renderbuffertarget, renderbuffer
gles2.glFramebufferRenderbuffer.errcheck = gles2_errcheck
glFramebufferRenderbuffer = gles2.glFramebufferRenderbuffer

""" GL_APICALL void         GL_APIENTRY glFramebufferTexture2D (GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level); """
gles2.glFramebufferTexture2D.restype = None
gles2.glFramebufferTexture2D.argtypes = (GLenum, GLenum, GLenum, GLuint, GLint)  # target, attachment, textarget, texture, level
gles2.glFramebufferTexture2D.errcheck = gles2_errcheck
glFramebufferTexture2D = gles2.glFramebufferTexture2D

""" GL_APICALL void         GL_APIENTRY glFrontFace (GLenum mode); """
gles2.glFrontFace.restype = None
gles2.glFrontFace.argtypes = (GLenum,)  # mode
gles2.glFrontFace.errcheck = gles2_errcheck
glFrontFace = gles2.glFrontFace

""" GL_APICALL void         GL_APIENTRY glGenBuffers (GLsizei n, GLuint* buffers); """
gles2.glGenBuffers.restype = None
gles2.glGenBuffers.argtypes = (GLsizei, GLuint_p)  # n, buffers
gles2.glGenBuffers.errcheck = gles2_errcheck
glGenBuffers = gles2.glGenBuffers

""" GL_APICALL void         GL_APIENTRY glGenerateMipmap (GLenum target); """
gles2.glGenerateMipmap.restype = None
gles2.glGenerateMipmap.argtypes = (GLenum,)  # target
gles2.glGenerateMipmap.errcheck = gles2_errcheck
glGenerateMipmap = gles2.glGenerateMipmap

""" GL_APICALL void         GL_APIENTRY glGenFramebuffers (GLsizei n, GLuint* framebuffers); """
gles2.glGenFramebuffers.restype = None
gles2.glGenFramebuffers.argtypes = (GLsizei, GLuint_p)  # n, framebuffers
gles2.glGenFramebuffers.errcheck = gles2_errcheck
glGenFramebuffers = gles2.glGenFramebuffers

""" GL_APICALL void         GL_APIENTRY glGenRenderbuffers (GLsizei n, GLuint* renderbuffers); """
gles2.glGenRenderbuffers.restype = None
gles2.glGenRenderbuffers.argtypes = (GLsizei, GLuint_p)  # n, renderbuffers
gles2.glGenRenderbuffers.errcheck = gles2_errcheck
glGenRenderbuffers = gles2.glGenRenderbuffers

""" GL_APICALL void         GL_APIENTRY glGenTextures (GLsizei n, GLuint* textures); """
gles2.glGenTextures.restype = None
gles2.glGenTextures.argtypes = (GLsizei, GLuint_p)  # n, textures
gles2.glGenTextures.errcheck = gles2_errcheck
glGenTextures = gles2.glGenTextures

""" GL_APICALL void         GL_APIENTRY glGetActiveAttrib (GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name); """
gles2.glGetActiveAttrib.restype = None
gles2.glGetActiveAttrib.argtypes = (GLuint, GLuint, GLsizei, GLsizei_p, GLint_p, GLenum_p, GLchar_p)  # program, index, bufsize, length, size, type, name
gles2.glGetActiveAttrib.errcheck = gles2_errcheck
glGetActiveAttrib = gles2.glGetActiveAttrib

""" GL_APICALL void         GL_APIENTRY glGetActiveUniform (GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name); """
gles2.glGetActiveUniform.restype = None
gles2.glGetActiveUniform.argtypes = (GLuint, GLuint, GLsizei, GLsizei_p, GLint_p, GLenum_p, GLchar_p)  # program, index, bufsize, length, size, type, name
gles2.glGetActiveUniform.errcheck = gles2_errcheck
glGetActiveUniform = gles2.glGetActiveUniform

""" GL_APICALL void         GL_APIENTRY glGetAttachedShaders (GLuint program, GLsizei maxcount, GLsizei* count, GLuint* shaders); """
gles2.glGetAttachedShaders.restype = None
gles2.glGetAttachedShaders.argtypes = (GLuint, GLsizei, GLsizei_p, GLuint_p)  # program, maxcount, count, shaders
gles2.glGetAttachedShaders.errcheck = gles2_errcheck
glGetAttachedShaders = gles2.glGetAttachedShaders

""" GL_APICALL int          GL_APIENTRY glGetAttribLocation (GLuint program, const GLchar* name); """
gles2.glGetAttribLocation.restype = int
gles2.glGetAttribLocation.argtypes = (GLuint, GLchar_p)  # program, name
gles2.glGetAttribLocation.errcheck = gles2_errcheck
glGetAttribLocation = gles2.glGetAttribLocation

""" GL_APICALL void         GL_APIENTRY glGetBooleanv (GLenum pname, GLboolean* params); """
gles2.glGetBooleanv.restype = None
gles2.glGetBooleanv.argtypes = (GLenum, GLboolean_p)  # pname, params
gles2.glGetBooleanv.errcheck = gles2_errcheck
glGetBooleanv = gles2.glGetBooleanv

""" GL_APICALL void         GL_APIENTRY glGetBufferParameteriv (GLenum target, GLenum pname, GLint* params); """
gles2.glGetBufferParameteriv.restype = None
gles2.glGetBufferParameteriv.argtypes = (GLenum, GLenum, GLint_p)  # target, pname, params
gles2.glGetBufferParameteriv.errcheck = gles2_errcheck
glGetBufferParameteriv = gles2.glGetBufferParameteriv

""" GL_APICALL GLenum       GL_APIENTRY glGetError (void); """
gles2.glGetError.restype = GLenum
gles2.glGetError.argtypes = ()  #
gles2.glGetError.errcheck = gles2_errcheck
glGetError = gles2.glGetError

""" GL_APICALL void         GL_APIENTRY glGetFloatv (GLenum pname, GLfloat* params); """
gles2.glGetFloatv.restype = None
gles2.glGetFloatv.argtypes = (GLenum, GLfloat_p)  # pname, params
gles2.glGetFloatv.errcheck = gles2_errcheck
glGetFloatv = gles2.glGetFloatv

""" GL_APICALL void         GL_APIENTRY glGetFramebufferAttachmentParameteriv (GLenum target, GLenum attachment, GLenum pname, GLint* params); """
gles2.glGetFramebufferAttachmentParameteriv.restype = None
gles2.glGetFramebufferAttachmentParameteriv.argtypes = (GLenum, GLenum, GLenum, GLint_p)  # target, attachment, pname, params
gles2.glGetFramebufferAttachmentParameteriv.errcheck = gles2_errcheck
glGetFramebufferAttachmentParameteriv = gles2.glGetFramebufferAttachmentParameteriv

""" GL_APICALL void         GL_APIENTRY glGetIntegerv (GLenum pname, GLint* params); """
gles2.glGetIntegerv.restype = None
gles2.glGetIntegerv.argtypes = (GLenum, GLint_p)  # pname, params
gles2.glGetIntegerv.errcheck = gles2_errcheck
glGetIntegerv = gles2.glGetIntegerv

""" GL_APICALL void         GL_APIENTRY glGetProgramiv (GLuint program, GLenum pname, GLint* params); """
gles2.glGetProgramiv.restype = None
gles2.glGetProgramiv.argtypes = (GLuint, GLenum, GLint_p)  # program, pname, params
gles2.glGetProgramiv.errcheck = gles2_errcheck
glGetProgramiv = gles2.glGetProgramiv

""" GL_APICALL void         GL_APIENTRY glGetProgramInfoLog (GLuint program, GLsizei bufsize, GLsizei* length, GLchar* infolog); """
gles2.glGetProgramInfoLog.restype = None
gles2.glGetProgramInfoLog.argtypes = (GLuint, GLsizei, GLsizei_p, GLchar_p)  # program, bufsize, length, infolog
gles2.glGetProgramInfoLog.errcheck = gles2_errcheck
glGetProgramInfoLog = gles2.glGetProgramInfoLog

""" GL_APICALL void         GL_APIENTRY glGetRenderbufferParameteriv (GLenum target, GLenum pname, GLint* params); """
gles2.glGetRenderbufferParameteriv.restype = None
gles2.glGetRenderbufferParameteriv.argtypes = (GLenum, GLenum, GLint_p)  # target, pname, params
gles2.glGetRenderbufferParameteriv.errcheck = gles2_errcheck
glGetRenderbufferParameteriv = gles2.glGetRenderbufferParameteriv

""" GL_APICALL void         GL_APIENTRY glGetShaderiv (GLuint shader, GLenum pname, GLint* params); """
gles2.glGetShaderiv.restype = None
gles2.glGetShaderiv.argtypes = (GLuint, GLenum, GLint_p)  # shader, pname, params
gles2.glGetShaderiv.errcheck = gles2_errcheck
glGetShaderiv = gles2.glGetShaderiv

""" GL_APICALL void         GL_APIENTRY glGetShaderInfoLog (GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* infolog); """
gles2.glGetShaderInfoLog.restype = None
gles2.glGetShaderInfoLog.argtypes = (GLuint, GLsizei, GLsizei_p, GLchar_p)  # shader, bufsize, length, infolog
gles2.glGetShaderInfoLog.errcheck = gles2_errcheck
glGetShaderInfoLog = gles2.glGetShaderInfoLog

""" GL_APICALL void         GL_APIENTRY glGetShaderPrecisionFormat (GLenum shadertype, GLenum precisiontype, GLint* range, GLint* precision); """
gles2.glGetShaderPrecisionFormat.restype = None
gles2.glGetShaderPrecisionFormat.argtypes = (GLenum, GLenum, GLint_p, GLint_p)  # shadertype, precisiontype, range, precision
gles2.glGetShaderPrecisionFormat.errcheck = gles2_errcheck
glGetShaderPrecisionFormat = gles2.glGetShaderPrecisionFormat

""" GL_APICALL void         GL_APIENTRY glGetShaderSource (GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* source); """
gles2.glGetShaderSource.restype = None
gles2.glGetShaderSource.argtypes = (GLuint, GLsizei, GLsizei_p, GLchar_p)  # shader, bufsize, length, source
gles2.glGetShaderSource.errcheck = gles2_errcheck
glGetShaderSource = gles2.glGetShaderSource

""" GL_APICALL const GLubyte* GL_APIENTRY glGetString (GLenum name); """
gles2.glGetString.restype = GLubyte_p
gles2.glGetString.argtypes = (GLenum,)  # name
gles2.glGetString.errcheck = gles2_errcheck
glGetString = gles2.glGetString

""" GL_APICALL void         GL_APIENTRY glGetTexParameterfv (GLenum target, GLenum pname, GLfloat* params); """
gles2.glGetTexParameterfv.restype = None
gles2.glGetTexParameterfv.argtypes = (GLenum, GLenum, GLfloat_p)  # target, pname, params
gles2.glGetTexParameterfv.errcheck = gles2_errcheck
glGetTexParameterfv = gles2.glGetTexParameterfv

""" GL_APICALL void         GL_APIENTRY glGetTexParameteriv (GLenum target, GLenum pname, GLint* params); """
gles2.glGetTexParameteriv.restype = None
gles2.glGetTexParameteriv.argtypes = (GLenum, GLenum, GLint_p)  # target, pname, params
gles2.glGetTexParameteriv.errcheck = gles2_errcheck
glGetTexParameteriv = gles2.glGetTexParameteriv

""" GL_APICALL void         GL_APIENTRY glGetUniformfv (GLuint program, GLint location, GLfloat* params); """
gles2.glGetUniformfv.restype = None
gles2.glGetUniformfv.argtypes = (GLuint, GLint, GLfloat_p)  # program, location, params
gles2.glGetUniformfv.errcheck = gles2_errcheck
glGetUniformfv = gles2.glGetUniformfv

""" GL_APICALL void         GL_APIENTRY glGetUniformiv (GLuint program, GLint location, GLint* params); """
gles2.glGetUniformiv.restype = None
gles2.glGetUniformiv.argtypes = (GLuint, GLint, GLint_p)  # program, location, params
gles2.glGetUniformiv.errcheck = gles2_errcheck
glGetUniformiv = gles2.glGetUniformiv

""" GL_APICALL int          GL_APIENTRY glGetUniformLocation (GLuint program, const GLchar* name); """
gles2.glGetUniformLocation.restype = int
gles2.glGetUniformLocation.argtypes = (GLuint, GLchar_p)  # program, name
gles2.glGetUniformLocation.errcheck = gles2_errcheck
glGetUniformLocation = gles2.glGetUniformLocation

""" GL_APICALL void         GL_APIENTRY glGetVertexAttribfv (GLuint index, GLenum pname, GLfloat* params); """
gles2.glGetVertexAttribfv.restype = None
gles2.glGetVertexAttribfv.argtypes = (GLuint, GLenum, GLfloat_p)  # index, pname, params
gles2.glGetVertexAttribfv.errcheck = gles2_errcheck
glGetVertexAttribfv = gles2.glGetVertexAttribfv

""" GL_APICALL void         GL_APIENTRY glGetVertexAttribiv (GLuint index, GLenum pname, GLint* params); """
gles2.glGetVertexAttribiv.restype = None
gles2.glGetVertexAttribiv.argtypes = (GLuint, GLenum, GLint_p)  # index, pname, params
gles2.glGetVertexAttribiv.errcheck = gles2_errcheck
glGetVertexAttribiv = gles2.glGetVertexAttribiv

""" GL_APICALL void         GL_APIENTRY glGetVertexAttribPointerv (GLuint index, GLenum pname, GLvoid** pointer); """
gles2.glGetVertexAttribPointerv.restype = None
gles2.glGetVertexAttribPointerv.argtypes = (GLuint, GLenum, GLvoid_p_p)  # index, pname, pointer
gles2.glGetVertexAttribPointerv.errcheck = gles2_errcheck
glGetVertexAttribPointerv = gles2.glGetVertexAttribPointerv

""" GL_APICALL void         GL_APIENTRY glHint (GLenum target, GLenum mode); """
gles2.glHint.restype = None
gles2.glHint.argtypes = (GLenum, GLenum)  # target, mode
gles2.glHint.errcheck = gles2_errcheck
glHint = gles2.glHint

""" GL_APICALL GLboolean    GL_APIENTRY glIsBuffer (GLuint buffer); """
gles2.glIsBuffer.restype = GLboolean
gles2.glIsBuffer.argtypes = (GLuint,)  # buffer
gles2.glIsBuffer.errcheck = gles2_errcheck
glIsBuffer = gles2.glIsBuffer

""" GL_APICALL GLboolean    GL_APIENTRY glIsEnabled (GLenum cap); """
gles2.glIsEnabled.restype = GLboolean
gles2.glIsEnabled.argtypes = (GLenum,)  # cap
gles2.glIsEnabled.errcheck = gles2_errcheck
glIsEnabled = gles2.glIsEnabled

""" GL_APICALL GLboolean    GL_APIENTRY glIsFramebuffer (GLuint framebuffer); """
gles2.glIsFramebuffer.restype = GLboolean
gles2.glIsFramebuffer.argtypes = (GLuint,)  # framebuffer
gles2.glIsFramebuffer.errcheck = gles2_errcheck
glIsFramebuffer = gles2.glIsFramebuffer

""" GL_APICALL GLboolean    GL_APIENTRY glIsProgram (GLuint program); """
gles2.glIsProgram.restype = GLboolean
gles2.glIsProgram.argtypes = (GLuint,)  # program
gles2.glIsProgram.errcheck = gles2_errcheck
glIsProgram = gles2.glIsProgram

""" GL_APICALL GLboolean    GL_APIENTRY glIsRenderbuffer (GLuint renderbuffer); """
gles2.glIsRenderbuffer.restype = GLboolean
gles2.glIsRenderbuffer.argtypes = (GLuint,)  # renderbuffer
gles2.glIsRenderbuffer.errcheck = gles2_errcheck
glIsRenderbuffer = gles2.glIsRenderbuffer

""" GL_APICALL GLboolean    GL_APIENTRY glIsShader (GLuint shader); """
gles2.glIsShader.restype = GLboolean
gles2.glIsShader.argtypes = (GLuint,)  # shader
gles2.glIsShader.errcheck = gles2_errcheck
glIsShader = gles2.glIsShader

""" GL_APICALL GLboolean    GL_APIENTRY glIsTexture (GLuint texture); """
gles2.glIsTexture.restype = GLboolean
gles2.glIsTexture.argtypes = (GLuint,)  # texture
gles2.glIsTexture.errcheck = gles2_errcheck
glIsTexture = gles2.glIsTexture

""" GL_APICALL void         GL_APIENTRY glLineWidth (GLfloat width); """
gles2.glLineWidth.restype = None
gles2.glLineWidth.argtypes = (GLfloat,)  # width
gles2.glLineWidth.errcheck = gles2_errcheck
glLineWidth = gles2.glLineWidth

""" GL_APICALL void         GL_APIENTRY glLinkProgram (GLuint program); """
gles2.glLinkProgram.restype = None
gles2.glLinkProgram.argtypes = (GLuint,)  # program
gles2.glLinkProgram.errcheck = gles2_errcheck
glLinkProgram = gles2.glLinkProgram

""" GL_APICALL void         GL_APIENTRY glPixelStorei (GLenum pname, GLint param); """
gles2.glPixelStorei.restype = None
gles2.glPixelStorei.argtypes = (GLenum, GLint)  # pname, param
gles2.glPixelStorei.errcheck = gles2_errcheck
glPixelStorei = gles2.glPixelStorei

""" GL_APICALL void         GL_APIENTRY glPolygonOffset (GLfloat factor, GLfloat units); """
gles2.glPolygonOffset.restype = None
gles2.glPolygonOffset.argtypes = (GLfloat, GLfloat)  # factor, units
gles2.glPolygonOffset.errcheck = gles2_errcheck
glPolygonOffset = gles2.glPolygonOffset

""" GL_APICALL void         GL_APIENTRY glReadPixels (GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid* pixels); """
gles2.glReadPixels.restype = None
gles2.glReadPixels.argtypes = (GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, GLvoid_p)  # x, y, width, height, format, type, pixels
gles2.glReadPixels.errcheck = gles2_errcheck
glReadPixels = gles2.glReadPixels

""" GL_APICALL void         GL_APIENTRY glReleaseShaderCompiler (void); """
gles2.glReleaseShaderCompiler.restype = None
gles2.glReleaseShaderCompiler.argtypes = ()  #
gles2.glReleaseShaderCompiler.errcheck = gles2_errcheck
glReleaseShaderCompiler = gles2.glReleaseShaderCompiler

""" GL_APICALL void         GL_APIENTRY glRenderbufferStorage (GLenum target, GLenum internalformat, GLsizei width, GLsizei height); """
gles2.glRenderbufferStorage.restype = None
gles2.glRenderbufferStorage.argtypes = (GLenum, GLenum, GLsizei, GLsizei)  # target, internalformat, width, height
gles2.glRenderbufferStorage.errcheck = gles2_errcheck
glRenderbufferStorage = gles2.glRenderbufferStorage

""" GL_APICALL void         GL_APIENTRY glSampleCoverage (GLclampf value, GLboolean invert); """
gles2.glSampleCoverage.restype = None
gles2.glSampleCoverage.argtypes = (GLclampf, GLboolean)  # value, invert
gles2.glSampleCoverage.errcheck = gles2_errcheck
glSampleCoverage = gles2.glSampleCoverage

""" GL_APICALL void         GL_APIENTRY glScissor (GLint x, GLint y, GLsizei width, GLsizei height); """
gles2.glScissor.restype = None
gles2.glScissor.argtypes = (GLint, GLint, GLsizei, GLsizei)  # x, y, width, height
gles2.glScissor.errcheck = gles2_errcheck
glScissor = gles2.glScissor

""" GL_APICALL void         GL_APIENTRY glShaderBinary (GLsizei n, const GLuint* shaders, GLenum binaryformat, const GLvoid* binary, GLsizei length); """
gles2.glShaderBinary.restype = None
gles2.glShaderBinary.argtypes = (GLsizei, GLuint_p, GLenum, GLvoid_p, GLsizei)  # n, shaders, binaryformat, binary, length
gles2.glShaderBinary.errcheck = gles2_errcheck
glShaderBinary = gles2.glShaderBinary

""" GL_APICALL void         GL_APIENTRY glShaderSource (GLuint shader, GLsizei count, const GLchar** string, const GLint* length); """
gles2.glShaderSource.restype = None
gles2.glShaderSource.argtypes = (GLuint, GLsizei, GLchar_p_p, GLint_p)  # shader, count, string, length
gles2.glShaderSource.errcheck = gles2_errcheck
glShaderSource = gles2.glShaderSource

""" GL_APICALL void         GL_APIENTRY glStencilFunc (GLenum func, GLint ref, GLuint mask); """
gles2.glStencilFunc.restype = None
gles2.glStencilFunc.argtypes = (GLenum, GLint, GLuint)  # func, ref, mask
gles2.glStencilFunc.errcheck = gles2_errcheck
glStencilFunc = gles2.glStencilFunc

""" GL_APICALL void         GL_APIENTRY glStencilFuncSeparate (GLenum face, GLenum func, GLint ref, GLuint mask); """
gles2.glStencilFuncSeparate.restype = None
gles2.glStencilFuncSeparate.argtypes = (GLenum, GLenum, GLint, GLuint)  # face, func, ref, mask
gles2.glStencilFuncSeparate.errcheck = gles2_errcheck
glStencilFuncSeparate = gles2.glStencilFuncSeparate

""" GL_APICALL void         GL_APIENTRY glStencilMask (GLuint mask); """
gles2.glStencilMask.restype = None
gles2.glStencilMask.argtypes = (GLuint,)  # mask
gles2.glStencilMask.errcheck = gles2_errcheck
glStencilMask = gles2.glStencilMask

""" GL_APICALL void         GL_APIENTRY glStencilMaskSeparate (GLenum face, GLuint mask); """
gles2.glStencilMaskSeparate.restype = None
gles2.glStencilMaskSeparate.argtypes = (GLenum, GLuint)  # face, mask
gles2.glStencilMaskSeparate.errcheck = gles2_errcheck
glStencilMaskSeparate = gles2.glStencilMaskSeparate

""" GL_APICALL void         GL_APIENTRY glStencilOp (GLenum fail, GLenum zfail, GLenum zpass); """
gles2.glStencilOp.restype = None
gles2.glStencilOp.argtypes = (GLenum, GLenum, GLenum)  # fail, zfail, zpass
gles2.glStencilOp.errcheck = gles2_errcheck
glStencilOp = gles2.glStencilOp

""" GL_APICALL void         GL_APIENTRY glStencilOpSeparate (GLenum face, GLenum fail, GLenum zfail, GLenum zpass); """
gles2.glStencilOpSeparate.restype = None
gles2.glStencilOpSeparate.argtypes = (GLenum, GLenum, GLenum, GLenum)  # face, fail, zfail, zpass
gles2.glStencilOpSeparate.errcheck = gles2_errcheck
glStencilOpSeparate = gles2.glStencilOpSeparate

""" GL_APICALL void         GL_APIENTRY glTexImage2D (GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid* pixels); """
gles2.glTexImage2D.restype = None
gles2.glTexImage2D.argtypes = (GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, GLvoid_p)  # target, level, internalformat, width, height, border, format, type, pixels
gles2.glTexImage2D.errcheck = gles2_errcheck
glTexImage2D = gles2.glTexImage2D

""" GL_APICALL void         GL_APIENTRY glTexParameterf (GLenum target, GLenum pname, GLfloat param); """
gles2.glTexParameterf.restype = None
gles2.glTexParameterf.argtypes = (GLenum, GLenum, GLfloat)  # target, pname, param
gles2.glTexParameterf.errcheck = gles2_errcheck
glTexParameterf = gles2.glTexParameterf

""" GL_APICALL void         GL_APIENTRY glTexParameterfv (GLenum target, GLenum pname, const GLfloat* params); """
gles2.glTexParameterfv.restype = None
gles2.glTexParameterfv.argtypes = (GLenum, GLenum, GLfloat_p)  # target, pname, params
gles2.glTexParameterfv.errcheck = gles2_errcheck
glTexParameterfv = gles2.glTexParameterfv

""" GL_APICALL void         GL_APIENTRY glTexParameteri (GLenum target, GLenum pname, GLint param); """
gles2.glTexParameteri.restype = None
gles2.glTexParameteri.argtypes = (GLenum, GLenum, GLint)  # target, pname, param
gles2.glTexParameteri.errcheck = gles2_errcheck
glTexParameteri = gles2.glTexParameteri

""" GL_APICALL void         GL_APIENTRY glTexParameteriv (GLenum target, GLenum pname, const GLint* params); """
gles2.glTexParameteriv.restype = None
gles2.glTexParameteriv.argtypes = (GLenum, GLenum, GLint_p)  # target, pname, params
gles2.glTexParameteriv.errcheck = gles2_errcheck
glTexParameteriv = gles2.glTexParameteriv

""" GL_APICALL void         GL_APIENTRY glTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid* pixels); """
gles2.glTexSubImage2D.restype = None
gles2.glTexSubImage2D.argtypes = (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, GLvoid_p)  # target, level, xoffset, yoffset, width, height, format, type, pixels
gles2.glTexSubImage2D.errcheck = gles2_errcheck
glTexSubImage2D = gles2.glTexSubImage2D

""" GL_APICALL void         GL_APIENTRY glUniform1f (GLint location, GLfloat x); """
gles2.glUniform1f.restype = None
gles2.glUniform1f.argtypes = (GLint, GLfloat)  # location, x
gles2.glUniform1f.errcheck = gles2_errcheck
glUniform1f = gles2.glUniform1f

""" GL_APICALL void         GL_APIENTRY glUniform1fv (GLint location, GLsizei count, const GLfloat* v); """
gles2.glUniform1fv.restype = None
gles2.glUniform1fv.argtypes = (GLint, GLsizei, GLfloat_p)  # location, count, v
gles2.glUniform1fv.errcheck = gles2_errcheck
glUniform1fv = gles2.glUniform1fv

""" GL_APICALL void         GL_APIENTRY glUniform1i (GLint location, GLint x); """
gles2.glUniform1i.restype = None
gles2.glUniform1i.argtypes = (GLint, GLint)  # location, x
gles2.glUniform1i.errcheck = gles2_errcheck
glUniform1i = gles2.glUniform1i

""" GL_APICALL void         GL_APIENTRY glUniform1iv (GLint location, GLsizei count, const GLint* v); """
gles2.glUniform1iv.restype = None
gles2.glUniform1iv.argtypes = (GLint, GLsizei, GLint_p)  # location, count, v
gles2.glUniform1iv.errcheck = gles2_errcheck
glUniform1iv = gles2.glUniform1iv

""" GL_APICALL void         GL_APIENTRY glUniform2f (GLint location, GLfloat x, GLfloat y); """
gles2.glUniform2f.restype = None
gles2.glUniform2f.argtypes = (GLint, GLfloat, GLfloat)  # location, x, y
gles2.glUniform2f.errcheck = gles2_errcheck
glUniform2f = gles2.glUniform2f

""" GL_APICALL void         GL_APIENTRY glUniform2fv (GLint location, GLsizei count, const GLfloat* v); """
gles2.glUniform2fv.restype = None
gles2.glUniform2fv.argtypes = (GLint, GLsizei, GLfloat_p)  # location, count, v
gles2.glUniform2fv.errcheck = gles2_errcheck
glUniform2fv = gles2.glUniform2fv

""" GL_APICALL void         GL_APIENTRY glUniform2i (GLint location, GLint x, GLint y); """
gles2.glUniform2i.restype = None
gles2.glUniform2i.argtypes = (GLint, GLint, GLint)  # location, x, y
gles2.glUniform2i.errcheck = gles2_errcheck
glUniform2i = gles2.glUniform2i

""" GL_APICALL void         GL_APIENTRY glUniform2iv (GLint location, GLsizei count, const GLint* v); """
gles2.glUniform2iv.restype = None
gles2.glUniform2iv.argtypes = (GLint, GLsizei, GLint_p)  # location, count, v
gles2.glUniform2iv.errcheck = gles2_errcheck
glUniform2iv = gles2.glUniform2iv

""" GL_APICALL void         GL_APIENTRY glUniform3f (GLint location, GLfloat x, GLfloat y, GLfloat z); """
gles2.glUniform3f.restype = None
gles2.glUniform3f.argtypes = (GLint, GLfloat, GLfloat, GLfloat)  # location, x, y, z
gles2.glUniform3f.errcheck = gles2_errcheck
glUniform3f = gles2.glUniform3f

""" GL_APICALL void         GL_APIENTRY glUniform3fv (GLint location, GLsizei count, const GLfloat* v); """
gles2.glUniform3fv.restype = None
gles2.glUniform3fv.argtypes = (GLint, GLsizei, GLfloat_p)  # location, count, v
gles2.glUniform3fv.errcheck = gles2_errcheck
glUniform3fv = gles2.glUniform3fv

""" GL_APICALL void         GL_APIENTRY glUniform3i (GLint location, GLint x, GLint y, GLint z); """
gles2.glUniform3i.restype = None
gles2.glUniform3i.argtypes = (GLint, GLint, GLint, GLint)  # location, x, y, z
gles2.glUniform3i.errcheck = gles2_errcheck
glUniform3i = gles2.glUniform3i

""" GL_APICALL void         GL_APIENTRY glUniform3iv (GLint location, GLsizei count, const GLint* v); """
gles2.glUniform3iv.restype = None
gles2.glUniform3iv.argtypes = (GLint, GLsizei, GLint_p)  # location, count, v
gles2.glUniform3iv.errcheck = gles2_errcheck
glUniform3iv = gles2.glUniform3iv

""" GL_APICALL void         GL_APIENTRY glUniform4f (GLint location, GLfloat x, GLfloat y, GLfloat z, GLfloat w); """
gles2.glUniform4f.restype = None
gles2.glUniform4f.argtypes = (GLint, GLfloat, GLfloat, GLfloat, GLfloat)  # location, x, y, z, w
gles2.glUniform4f.errcheck = gles2_errcheck
glUniform4f = gles2.glUniform4f

""" GL_APICALL void         GL_APIENTRY glUniform4fv (GLint location, GLsizei count, const GLfloat* v); """
gles2.glUniform4fv.restype = None
gles2.glUniform4fv.argtypes = (GLint, GLsizei, GLfloat_p)  # location, count, v
gles2.glUniform4fv.errcheck = gles2_errcheck
glUniform4fv = gles2.glUniform4fv

""" GL_APICALL void         GL_APIENTRY glUniform4i (GLint location, GLint x, GLint y, GLint z, GLint w); """
gles2.glUniform4i.restype = None
gles2.glUniform4i.argtypes = (GLint, GLint, GLint, GLint, GLint)  # location, x, y, z, w
gles2.glUniform4i.errcheck = gles2_errcheck
glUniform4i = gles2.glUniform4i

""" GL_APICALL void         GL_APIENTRY glUniform4iv (GLint location, GLsizei count, const GLint* v); """
gles2.glUniform4iv.restype = None
gles2.glUniform4iv.argtypes = (GLint, GLsizei, GLint_p)  # location, count, v
gles2.glUniform4iv.errcheck = gles2_errcheck
glUniform4iv = gles2.glUniform4iv

""" GL_APICALL void         GL_APIENTRY glUniformMatrix2fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value); """
gles2.glUniformMatrix2fv.restype = None
gles2.glUniformMatrix2fv.argtypes = (GLint, GLsizei, GLboolean, GLfloat_p)  # location, count, transpose, value
gles2.glUniformMatrix2fv.errcheck = gles2_errcheck
glUniformMatrix2fv = gles2.glUniformMatrix2fv

""" GL_APICALL void         GL_APIENTRY glUniformMatrix3fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value); """
gles2.glUniformMatrix3fv.restype = None
gles2.glUniformMatrix3fv.argtypes = (GLint, GLsizei, GLboolean, GLfloat_p)  # location, count, transpose, value
gles2.glUniformMatrix3fv.errcheck = gles2_errcheck
glUniformMatrix3fv = gles2.glUniformMatrix3fv

""" GL_APICALL void         GL_APIENTRY glUniformMatrix4fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value); """
gles2.glUniformMatrix4fv.restype = None
gles2.glUniformMatrix4fv.argtypes = (GLint, GLsizei, GLboolean, GLfloat_p)  # location, count, transpose, value
gles2.glUniformMatrix4fv.errcheck = gles2_errcheck
glUniformMatrix4fv = gles2.glUniformMatrix4fv

""" GL_APICALL void         GL_APIENTRY glUseProgram (GLuint program); """
gles2.glUseProgram.restype = None
gles2.glUseProgram.argtypes = (GLuint,)  # program
gles2.glUseProgram.errcheck = gles2_errcheck
glUseProgram = gles2.glUseProgram

""" GL_APICALL void         GL_APIENTRY glValidateProgram (GLuint program); """
gles2.glValidateProgram.restype = None
gles2.glValidateProgram.argtypes = (GLuint,)  # program
gles2.glValidateProgram.errcheck = gles2_errcheck
glValidateProgram = gles2.glValidateProgram

""" GL_APICALL void         GL_APIENTRY glVertexAttrib1f (GLuint indx, GLfloat x); """
gles2.glVertexAttrib1f.restype = None
gles2.glVertexAttrib1f.argtypes = (GLuint, GLfloat)  # indx, x
gles2.glVertexAttrib1f.errcheck = gles2_errcheck
glVertexAttrib1f = gles2.glVertexAttrib1f

""" GL_APICALL void         GL_APIENTRY glVertexAttrib1fv (GLuint indx, const GLfloat* values); """
gles2.glVertexAttrib1fv.restype = None
gles2.glVertexAttrib1fv.argtypes = (GLuint, GLfloat_p)  # indx, values
gles2.glVertexAttrib1fv.errcheck = gles2_errcheck
glVertexAttrib1fv = gles2.glVertexAttrib1fv

""" GL_APICALL void         GL_APIENTRY glVertexAttrib2f (GLuint indx, GLfloat x, GLfloat y); """
gles2.glVertexAttrib2f.restype = None
gles2.glVertexAttrib2f.argtypes = (GLuint, GLfloat, GLfloat)  # indx, x, y
gles2.glVertexAttrib2f.errcheck = gles2_errcheck
glVertexAttrib2f = gles2.glVertexAttrib2f

""" GL_APICALL void         GL_APIENTRY glVertexAttrib2fv (GLuint indx, const GLfloat* values); """
gles2.glVertexAttrib2fv.restype = None
gles2.glVertexAttrib2fv.argtypes = (GLuint, GLfloat_p)  # indx, values
gles2.glVertexAttrib2fv.errcheck = gles2_errcheck
glVertexAttrib2fv = gles2.glVertexAttrib2fv

""" GL_APICALL void         GL_APIENTRY glVertexAttrib3f (GLuint indx, GLfloat x, GLfloat y, GLfloat z); """
gles2.glVertexAttrib3f.restype = None
gles2.glVertexAttrib3f.argtypes = (GLuint, GLfloat, GLfloat, GLfloat)  # indx, x, y, z
gles2.glVertexAttrib3f.errcheck = gles2_errcheck
glVertexAttrib3f = gles2.glVertexAttrib3f

""" GL_APICALL void         GL_APIENTRY glVertexAttrib3fv (GLuint indx, const GLfloat* values); """
gles2.glVertexAttrib3fv.restype = None
gles2.glVertexAttrib3fv.argtypes = (GLuint, GLfloat_p)  # indx, values
gles2.glVertexAttrib3fv.errcheck = gles2_errcheck
glVertexAttrib3fv = gles2.glVertexAttrib3fv

""" GL_APICALL void         GL_APIENTRY glVertexAttrib4f (GLuint indx, GLfloat x, GLfloat y, GLfloat z, GLfloat w); """
gles2.glVertexAttrib4f.restype = None
gles2.glVertexAttrib4f.argtypes = (GLuint, GLfloat, GLfloat, GLfloat, GLfloat)  # indx, x, y, z, w
gles2.glVertexAttrib4f.errcheck = gles2_errcheck
glVertexAttrib4f = gles2.glVertexAttrib4f

""" GL_APICALL void         GL_APIENTRY glVertexAttrib4fv (GLuint indx, const GLfloat* values); """
gles2.glVertexAttrib4fv.restype = None
gles2.glVertexAttrib4fv.argtypes = (GLuint, GLfloat_p)  # indx, values
gles2.glVertexAttrib4fv.errcheck = gles2_errcheck
glVertexAttrib4fv = gles2.glVertexAttrib4fv

""" GL_APICALL void         GL_APIENTRY glVertexAttribPointer (GLuint indx, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const GLvoid* ptr); """
gles2.glVertexAttribPointer.restype = None
gles2.glVertexAttribPointer.argtypes = (GLuint, GLint, GLenum, GLboolean, GLsizei, GLvoid_p)  # indx, size, type, normalized, stride, ptr
gles2.glVertexAttribPointer.errcheck = gles2_errcheck
glVertexAttribPointer = gles2.glVertexAttribPointer

""" GL_APICALL void         GL_APIENTRY glViewport (GLint x, GLint y, GLsizei width, GLsizei height); """
gles2.glViewport.restype = None
gles2.glViewport.argtypes = (GLint, GLint, GLsizei, GLsizei)  # x, y, width, height
gles2.glViewport.errcheck = gles2_errcheck
glViewport = gles2.glViewport

