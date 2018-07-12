import sys
import numpy as np
from pyrr import Quaternion, Matrix33, Matrix44, Vector3, Vector4


if True:
    file_name = sys.argv[1]

    data = np.loadtxt(file_name)

    data_size = data.shape[0]
    all_quaternion = np.zeros((data_size-1,7))
    pose_last =np.matrix(np.eye(4,4))
    pose =np.matrix(np.eye(4,4))
    pose_last[0:3,:] = np.matrix(data[0,:].reshape(3,4))
    for i in range(1,data_size):
        pose[0:3,:] = np.matrix(data[i,:].reshape(3,4))
        motion = pose_last.I*pose
        motion_pyrr = Matrix44(motion)
        quaternion = Quaternion(motion_pyrr[0:3,0:3])
        trans = motion_pyrr[0:3,3].T
        trans_quat = np.zeros(7)
        trans_quat[0:3] = trans
        trans_quat[3:7] = quaternion
        all_quaternion[i-1,:] = trans_quat
        pose_last = pose.copy()
        #print pose_line
    np.savetxt(sys.argv[2],all_quaternion)
    print('done')





