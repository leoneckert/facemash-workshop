import cv2
import dlib
import sys, os, time, random
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

def warp_im(im, M, dshape):
    output_im = np.ones(dshape, dtype=im.dtype)*255
    cv2.warpAffine(im,
                   M[:2],
                   (dshape[1], dshape[0]),
                   dst=output_im,
                   borderMode=cv2.BORDER_TRANSPARENT,
                   flags=cv2.WARP_INVERSE_MAP)
    return output_im


folder = sys.argv[1]

count = 0
for img_file in os.listdir(folder):
    if img_file.startswith(".DS"):
        continue

    path = folder + "/" + img_file
    print count, ":", path
    if count == 0:
        # get our reference image
        ref_img = get_img(path)
        rects = get_rects(ref_img)
        if len(rects) > 0:
            ref_rect = rects[0]
        else:
            continue
        ref_landmarks = get_landmarks(ref_img, ref_rect)
        average = ref_img.copy()

        cv2.imshow('average', average)
        # cv2.waitKey(0)


    else:
        # do the thing
        img = get_img(path)
        rects = get_rects(img)
        if len(rects) > 0:
            rect = rects[0]
        else:
            continue

        landmarks = get_landmarks(img, rect)

        transformation_matrix = transformation_from_points(ref_landmarks, landmarks)
        warped_img = warp_im(img, transformation_matrix, ref_img.shape)


        average = average/255.0
        warped_img = warped_img/255.0
        average = ((average * count) + warped_img) / (count+1)
        average = average*255.0

        if random.random()>0.5:
            average = np.ceil(average)
        else:
            average = np.floor(average)
        average = average.astype('uint8')


        cv2.imshow('average', average)
        cv2.waitKey(1)

        # if count > 1:
        #     break

    count += 1

cv2.waitKey(0)
