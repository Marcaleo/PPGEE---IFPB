# -*- coding: utf-8 -*-

"""
INSTITUTO FEDERAL DA PARAÍBA - PPGEE
  DISCIPLINA: PROCESSAMENTO DIGITAL DE IMAGENS
  DOCENTE: DANILO REGIS

  DISCENTE: LEONARDO MARÇAL DA SILVA
  
  ATIVIDADE 1
"""

# -------------------------------------------------- #
import numpy as np
import cv2

# -------------------------------------------------- #
# LOAD AN IMAGE AND DISPLAY THAT
img = cv2.imread('chi_itza.png')
cv2.imshow('Original image',img)

# LOAD AND SAVE THE SAME IMAGE WITH GRAYSCALE
img2 = cv2.imread('chi_itza.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale image',img2)
cv2.imwrite('Grayscale.png',img2)

# -------------------------------------------------- #
# GIVE DIMENSIONS WITH SHAPE ATTRIBUTE
row,col,plane = img.shape

# -------------------------------------------------- #
# CREATE A ZERO MATRIX WITH THE ACQUIRED DIMENSIONS
temp = np.zeros((row,col,plane),np.uint8)
# STORE THE VALUES FOR THE BLUE PLANE
temp[:,:,0] = img[:,:,0]
# DISPLAYING THE BLUE PLANE IMAGE
cv2.imshow('Blue plane image',temp)
# SAVE IMAGE WITH BLUE PLANE
cv2.imwrite('Blue_plane.png',temp)

# -------------------------------------------------- #
# RESTORE DE VALUES FOR temp VARIABLE
temp = np.zeros((row,col,plane),np.uint8)
# STORE THE VALUES FOR THE GREEN PLANE
temp[:,:,1] = img[:,:,1]
# DISPLAYING THE GREEN PLANE IMAGE
cv2.imshow('Green plane image',temp)
# SAVE IMAGE WITH GREEN PLANE
cv2.imwrite('Green_plane.png',temp)

# -------------------------------------------------- #
# RESTORE DE VALUES FOR temp VARIABLE AGAIN
temp = np.zeros((row,col,plane),np.uint8)
# STORE THE VALUES FOR THE RED PLANE
temp[:,:,2] = img[:,:,2]
# DISPLAYING THE RED PLANE IMAGE
cv2.imshow('Red plane image',temp)
# SAVE IMAGE WITH RED PLANE
cv2.imwrite('Red_plane.png',temp)

# -------------------------------------------------- #
# WAIT FOR NON CRASH PYTHON KERNEL
cv2.waitKey(0)
# CLOSE ALL WINDOWS
cv2.destroyAllWindows()