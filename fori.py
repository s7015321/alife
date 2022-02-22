import numpy as np

N=1
#A=np.random.random(N)
A=0
FIELD_WIDTH=600
FIELD_HEIGHT=600
sensor_th = np.linspace(0, 2*np.pi, 7, endpoint=False)
SENSOR_POSITION = 1 * np.array([np.cos(sensor_th), np.sin(sensor_th)]).T
agents_th = np.random.random(N).astype(np.float32) * np.pi * 2
agents_pos = np.random.random((N, 2)).astype(np.float32) * FIELD_WIDTH
sensor_data = np.random.random((N, 7))
for ai in range(N):
            th = agents_th[ai]
            rot_mat = np.array([[np.cos(th), -np.sin(th)],[np.sin(th), np.cos(th)]])
            print("agents_th=",agents_th)
            print("agents_pos=",agents_pos)
            print("sensor_data=",sensor_data)
            print("rot_mat=",rot_mat)
            for si, sensor_pos in enumerate(SENSOR_POSITION):
                sx, sy = rot_mat @ sensor_pos
                xi = int((sx + agents_pos[ai][0] + FIELD_WIDTH) % FIELD_WIDTH)
                yi = int((sy + agents_pos[ai][1] + FIELD_HEIGHT) % FIELD_HEIGHT)
                print("sx=",sx)
                print("sy=",sy)
                print("xi=",xi)
                print("yi=",yi)
                #sensor_data[ai, si] = field[yi, xi] + np.random.randn() * 0.01