# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from drrobot_jaguarV2_player/StandardSensor.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class StandardSensor(genpy.Message):
  _md5sum = "e867c61af4cf779989629edb31d6fbd8"
  _type = "drrobot_jaguarV2_player/StandardSensor"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# standard Sensor information message from DrRobot Robot.

Header header    	# timestamp in the header is the time the driver
		 	# returned the battery/power reading
string robot_type	# robot type, I90 series, sentinel3 or Hawk/H20 Power/Motion

#make sure below sensors on your robot or not
uint32[] humanSensorData		#human sensor
uint32[] tiltingSensorData    #tilting sensor X Y
uint32[] overHeatSensorData   # over heat sensor on the board
uint32 thermoSensorData	    # enviroment temperature
float32 boardPowerVol 			# control board voltage
float32 motorPowerVol			# motor power voltage
float32 servoPowerVol			# servo power voltage
float32 refVol					# AD reference voltage
float32 potVol					# potentialmeter power voltage , not used now
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['header','robot_type','humanSensorData','tiltingSensorData','overHeatSensorData','thermoSensorData','boardPowerVol','motorPowerVol','servoPowerVol','refVol','potVol']
  _slot_types = ['std_msgs/Header','string','uint32[]','uint32[]','uint32[]','uint32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,robot_type,humanSensorData,tiltingSensorData,overHeatSensorData,thermoSensorData,boardPowerVol,motorPowerVol,servoPowerVol,refVol,potVol

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StandardSensor, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.robot_type is None:
        self.robot_type = ''
      if self.humanSensorData is None:
        self.humanSensorData = []
      if self.tiltingSensorData is None:
        self.tiltingSensorData = []
      if self.overHeatSensorData is None:
        self.overHeatSensorData = []
      if self.thermoSensorData is None:
        self.thermoSensorData = 0
      if self.boardPowerVol is None:
        self.boardPowerVol = 0.
      if self.motorPowerVol is None:
        self.motorPowerVol = 0.
      if self.servoPowerVol is None:
        self.servoPowerVol = 0.
      if self.refVol is None:
        self.refVol = 0.
      if self.potVol is None:
        self.potVol = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.robot_type = ''
      self.humanSensorData = []
      self.tiltingSensorData = []
      self.overHeatSensorData = []
      self.thermoSensorData = 0
      self.boardPowerVol = 0.
      self.motorPowerVol = 0.
      self.servoPowerVol = 0.
      self.refVol = 0.
      self.potVol = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.robot_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.humanSensorData)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.humanSensorData))
      length = len(self.tiltingSensorData)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.tiltingSensorData))
      length = len(self.overHeatSensorData)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.overHeatSensorData))
      _x = self
      buff.write(_get_struct_I5f().pack(_x.thermoSensorData, _x.boardPowerVol, _x.motorPowerVol, _x.servoPowerVol, _x.refVol, _x.potVol))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.robot_type = str[start:end].decode('utf-8')
      else:
        self.robot_type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.humanSensorData = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.tiltingSensorData = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.overHeatSensorData = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 24
      (_x.thermoSensorData, _x.boardPowerVol, _x.motorPowerVol, _x.servoPowerVol, _x.refVol, _x.potVol,) = _get_struct_I5f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.robot_type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.humanSensorData)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.humanSensorData.tostring())
      length = len(self.tiltingSensorData)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.tiltingSensorData.tostring())
      length = len(self.overHeatSensorData)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.overHeatSensorData.tostring())
      _x = self
      buff.write(_get_struct_I5f().pack(_x.thermoSensorData, _x.boardPowerVol, _x.motorPowerVol, _x.servoPowerVol, _x.refVol, _x.potVol))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.robot_type = str[start:end].decode('utf-8')
      else:
        self.robot_type = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.humanSensorData = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.tiltingSensorData = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.overHeatSensorData = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      _x = self
      start = end
      end += 24
      (_x.thermoSensorData, _x.boardPowerVol, _x.motorPowerVol, _x.servoPowerVol, _x.refVol, _x.potVol,) = _get_struct_I5f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_I5f = None
def _get_struct_I5f():
    global _struct_I5f
    if _struct_I5f is None:
        _struct_I5f = struct.Struct("<I5f")
    return _struct_I5f
