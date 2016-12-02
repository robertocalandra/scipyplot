# import R.log as rlog
import matplotlib.pyplot as plt
import numpy as np


def RGB2video(data, nameFile='video', verbosity=1, indent=0, framerate=24, codec='mpeg4', threads=4):
    """

    :param data: np.array N x H x W x 3
    :param nameFile:
    :param verbosity:
    :param indent:
    :return:
    """
    from moviepy.video.io.ffmpeg_writer import FFMPEG_VideoWriter as fwv

    # Write to FFMPEG
    extension = '.mp4'  # '.avi'
    fullNameVideo = nameFile + extension
    n_frame = data.shape[0]
    resolution = (data.shape[2], data.shape[1])  # (W, H)
    print('Resolution: %d x %d fps: %d n_frames: %d' % (resolution[0], resolution[1], framerate, n_frame))
    print('Saving to file: ' + fullNameVideo)
    a = fwv(filename=fullNameVideo, codec=codec, size=resolution, fps=framerate, preset="slower", threads=threads)
    for i in range(n_frame):
        # frame = np.swapaxes(data[i, :], 1, 2)
        frame = data[i, :].astype('uint8')
        assert np.all(0 <= frame) and np.all(frame <= 255), 'Value of the pixels is not in [0-255]'
        a.write_frame(frame)
        # plt.figure()
        # plt.imshow(frame/255)
        # plt.show
    a.close()
    # rlog.cnd_status(current_verbosity=verbosity, necessary_verbosity=1, f=0)
    # TODO: fix circular  import rlog
    return 0
