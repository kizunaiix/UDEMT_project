import numpy as np

def pc_normalize(pc):
    '''
    将点云的点归一化并将中心放置在原点
    @param pc: (n,3)float
    '''
    centroid = np.mean(pc, axis=0)
    pc = pc - centroid
    m = np.max(np.sqrt(np.sum(pc ** 2, axis=1)))
    pc = pc / m
    return pc
