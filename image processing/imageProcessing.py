#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:33:47 2024

@author: ilker
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Resim yolu
image_path = '/Users/ilker/Downloads/download.jpeg'

# Görüntüyü aç
image = Image.open(image_path)

# Görüntüyü numpy dizisine dönüştür
image_matrix = np.array(image)

# RGB ağırlıkları (kırmızı, yeşil, mavi için) göz duyarlılığına göre ayarlandı
weights = [0.1989, 0.6870, 0.1140]  # Bu değerler insan gözünün kırmızı, yeşil ve maviye duyarlılığını temsil eder

# RGB görüntüsünü siyah beyaza dönüştürmek için ağırlıkları uygula
gray_image = np.dot(image_matrix[..., :3], weights)

# Orijinal ve gri tonlamalı görüntüleri göster
plt.figure(figsize=(5, ))

# Orijinal görüntü
plt.subplot(1, 2, 1)
plt.imshow(image_matrix)
plt.title("Orijinal Görüntü")
plt.axis('off')
plt.show()

# Siyah-beyaz (grayscale) görüntü
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')  # Siyah-beyaz görüntü için cmap='gray' kullanıyoruz
plt.title("Siyah-Beyaz Görüntü")
plt.axis('off')


plt.show()
