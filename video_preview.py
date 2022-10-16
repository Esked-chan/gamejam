from moviepy.editor import *
import pygame

pygame.init()

display_width = 1920
display_height = 1080 # size of the screen

display = pygame.display.set_mode((display_width, display_height))

# DO NOT forget import the video to the game folder
pygame.display.set_caption('Flame Frame')

video = VideoFileClip('preview.mp4').resize((1920, 1080)) # size for the video
video.preview()

pygame.quit()