try:
    from enum import StrEnum
except ImportError:
    # Python < 3.11 fallback
    from enum import Enum

    class StrEnum(str, Enum):
        pass

class SensorLinkData(StrEnum):
    SENSOR_NAME = "sensor_name"
    SENSOR_TYPE = "sensor_type"
    SENSOR_OFFSET_POSE_STR = "sensor_offset_pose"
    OPTICAL_FRAME_POSE_STR = "optical_frame_pose"
    OPTICAL_FRAME_NAME = "optical_frame_name"

class LinkToSensorData(StrEnum):
    LINK_POSE_STR = "link_pose_str"
    SENSORS = "sensors"

class TfData(StrEnum):
    CHILD_FRAME = "child_frame"
    PARENT_FRAME = "parent_frame"
    TF_MATRIX = "tf_matrix"