# import pyaudio
# import numpy as np
# import matplotlib.pyplot as plt

# # set up PyAudio
# p = pyaudio.PyAudio()

# # set parameters for recording
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024

# # start recording
# stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# print("Speak now:")

# # initialize variables for recording and plotting
# frames = []
# fig, ax = plt.subplots()

# # continuously record and plot audio data
# while True:
#     # read audio data from stream
#     data = stream.read(CHUNK)
    
#     # convert data to numpy array
#     data_np = np.frombuffer(data, dtype=np.int16)
    
#     # append data to frames list
#     frames.append(data_np)
    
#     # plot sound wave
#     ax.clear()
#     ax.plot(np.concatenate(frames))
#     ax.set_xlabel("Time (s)")
#     ax.set_ylabel("Amplitude")
#     ax.set_title("Sound Wave Visualization")
#     plt.pause(0.001)
    
#     # check for keyboard interrupt to stop recording and plotting
#     try:
#         if plt.get_fignums():
#             plt.show(block=False)
#         else:
#             break
#     except KeyboardInterrupt:
#         break

# # stop recording and close stream
# stream.stop_stream()
# stream.close()
# p.terminate()

# # concatenate recorded frames into a single numpy array
# audio_data = np.concatenate(frames)

# # plot final sound wave
# fig, ax = plt.subplots()
# ax.plot(audio_data)
# ax.set_xlabel("Time (s)")
# ax.set_ylabel("Amplitude")
# ax.set_title("Sound Wave Visualization")

# # show final plot
# plt.show()
import pyaudio
import numpy as np
import pygame
import math

# set up PyAudio
p = pyaudio.PyAudio()

# set parameters for recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# start recording
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# set up Pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# set up circle parameters
circle_pos = np.array([WIDTH / 2, HEIGHT / 2])
circle_min_radius = 10
circle_max_radius = 200
circle_color = (255, 255, 255)

# continuously record audio data and update circle radius
while True:
    # read audio data from stream
    data = stream.read(CHUNK)
    
    # convert data to numpy array
    data_np = np.frombuffer(data, dtype=np.int16)
    
    # calculate root mean square (RMS) amplitude of audio data
    if(math.isnan(data_np)):
        data_np = 1.0
    rms_amplitude = np.sqrt(np.mean(np.square(data_np)))
    
    # map RMS amplitude to circle radius
    circle_radius = int(np.interp(rms_amplitude, [0, 500], [circle_min_radius, circle_max_radius]))
    
    # clear screen and draw circle
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
    
    # update display
    pygame.display.update()
    
    # check for keyboard interrupt to stop recording and quit Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
    
    # limit frame rate to 60 fps
    clock.tick(60)

# stop recording and close stream
stream.stop_stream()
stream.close()
p.terminate()
