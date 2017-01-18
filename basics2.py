import cv2
import dlib
import sys
import numpy as np
detector = dlib.get_frontal_face_detector()
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(PREDICTOR_PATH)


def get_img(path):
    print "[+] Opened image from:", path
    return cv2.imread(path)

def get_rects(img):
    rects = detector(img)
    print "[+] Number of faces found:", len(rects)
    return rects

def get_landmarks(img, rect):
    return np.matrix([[p.x, p.y] for p in predictor(img, rect).parts()])

img1 = get_img(sys.argv[1])
cv2.imshow('img1', img1)
img2 = get_img(sys.argv[2])
cv2.imshow('img2_pre_warp', img2)
rect1 = get_rects(img1)[0]
rect2 = get_rects(img2)[0]
landmarks1 = get_landmarks(img1, rect1)
landmarks2 = get_landmarks(img2, rect2)

# https://matthewearl.github.io/2015/07/28/switching-eds-with-python/
def transformation_from_points(points1, points2):
    points1 = points1.astype(np.float64)
    points2 = points2.astype(np.float64)

    c1 = np.mean(points1, axis=0)
    c2 = np.mean(points2, axis=0)
    points1 -= c1
    points2 -= c2

    s1 = np.std(points1)
    s2 = np.std(points2)
    points1 /= s1
    points2 /= s2

    U, S, Vt = np.linalg.svd(points1.T * points2)
    R = (U * Vt).T

    return np.vstack([np.hstack(((s2 / s1) * R,
                                       c2.T - (s2 / s1) * R * c1.T)),
                         np.matrix([0., 0., 1.])])


mat = transformation_from_points(landmarks1, landmarks2)

def warp_im(im, M, dshape):
    output_im = np.zeros(dshape, dtype=im.dtype)
    cv2.warpAffine(im,
                   M[:2],
                   (dshape[1], dshape[0]),
                   dst=output_im,
                   borderMode=cv2.BORDER_TRANSPARENT,
                   flags=cv2.WARP_INVERSE_MAP)
    return output_im

warped_img2 = warp_im(img2, mat, img1.shape)
cv2.imshow('img2_after_warp', warped_img2)

average = img1

average = average/255.0
warped_img2 = warped_img2/255.0
average = (average + warped_img2) / 2.0

average = average*255.0
average = average.astype('uint8')

cv2.imshow('average', average)
cv2.waitKey(0)
