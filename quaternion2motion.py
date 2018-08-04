import sys
import numpy as np
from pyrr import Quaternion, Matrix33, Matrix44, Vector3, Vector4


if True:
    file_name = sys.argv[1]

    data = np.loadtxt(file_name)

    data_size = data.shape[0]
    all_motion = np.zeros((data_size-1,7))
    pose_last = Matrix44(np.eye(4))
    pose_last[0:3,0:3] = Matrix33(data[0,3:7])
    pose_last[0:3,3] = data[0,0:3].T
    for i in range(1,data_size):
        pose_curr = Matrix44(np.eye(4))
        pose_curr[0:3,0:3] = Matrix33(data[i,3:7])
        pose_curr[0:3,3] = data[i,0:3].T
        print(pose_last)
        motion = ~pose_last*pose_curr
        quaternion = Quaternion(motion[0:3,0:3])
        trans = motion[0:3,3].T
        trans_quat = np.zeros(7)
        trans_quat[0:3] = trans
        trans_quat[3:7] = quaternion
        all_motion[i-1,:] = trans_quat
        pose_last = pose_curr.copy()
        #print pose_line
    np.savetxt(sys.argv[2],all_motion)
    print('done')





