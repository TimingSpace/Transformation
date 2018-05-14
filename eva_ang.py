import sys
import numpy as np


def ang2mat(angle_data):
    alpha = angle_data[0]
    beta  = angle_data[1]
    gama  = angle_data[2]

    alpha_mat = np.matrix(np.eye(3))
    beta_mat = np.matrix(np.eye(3))
    gama_mat = np.matrix(np.eye(3))
    alpha_mat[1,1] =  np.cos(alpha)
    alpha_mat[1,2] = -np.sin(alpha)
    alpha_mat[2,1] =  np.sin(alpha)
    alpha_mat[2,2] =  np.cos(alpha)

    beta_mat[0,0] =  np.cos(beta)
    beta_mat[0,2] = -np.sin(beta)
    beta_mat[2,0] =  np.sin(beta)
    beta_mat[2,2] =  np.cos(beta)

    gama_mat[0,0] =  np.cos(gama)
    gama_mat[0,1] = -np.sin(gama)
    gama_mat[1,0] =  np.sin(gama)
    gama_mat[1,1] =  np.cos(gama)

    result_mat = gama_mat*beta_mat*alpha_mat
    return result_mat
def mat2ang(mat_data):
    alpha = np.arctan2(mat_data[2,1],mat_data[2,2])
    beta  = np.arctan2(mat_data[2,0],np.sqrt(mat_data[2,2]*mat_data[2,2]+mat_data[2,1]*mat_data[2,1]))
    gama  = np.arctan2(mat_data[1,0],mat_data[0,0])
    return [alpha,beta,gama]
def angpos2mat(angpos_data):
    result_mat = np.matrix(np.eye(4))
    result_mat[0:3,0:3] = ang2mat(angpos_data[3:6])
    result_mat[0:3,3]   = np.matrix(angpos_data[0:3]).T
    return result_mat

if True:
    file_name = sys.argv[1]

    data = np.loadtxt(file_name)

    data_size = data.shape[0]
    data_degs = np.zeros((data_size,3))
    print(data_degs.shape)
    for i in range(0,data_size):
        data_deg = data[i,3:6]*180/np.pi
        data_degs[i] = data_deg
    print(np.max(data_degs,0))
    print(np.min(data_degs,0))





