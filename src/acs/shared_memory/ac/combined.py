import ctypes

from acs.shared_memory.ac.graphics import GraphicsSharedMemory
from acs.shared_memory.ac.physics import PhysicsSharedMemory

COMBINED_DATA_TYPES = GraphicsSharedMemory.dtypes
COMBINED_DATA_TYPES.extend(PhysicsSharedMemory._fields_)

COMBINED_CTYPES = GraphicsSharedMemory._fields_
COMBINED_CTYPES.extend(PhysicsSharedMemory._fields_)


class CombinedSharedMemory(ctypes.Structure):
    _fields_ = COMBINED_CTYPES
