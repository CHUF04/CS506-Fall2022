import cv2
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(100, 100))
def draw_school():
    Image1 = cv2.imread('school.jpg')
    plt.imshow(Image1)
    plt.axis('off')
    plt.title("school")
    return
draw_school()