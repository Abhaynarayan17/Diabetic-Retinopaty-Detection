>> % Load the retinal image
img = imread('ret.jpg');

% Convert to grayscale
gray_img = rgb2gray(img);

% Apply contrast adjustment for better detection
contrast_img = imadjust(gray_img);

% Apply blob detection using the 'detectMSERFeatures' function
regions = detectMSERFeatures(contrast_img, 'RegionAreaRange', [30 1400]);

% Display the detected microaneurysms
figure, imshow(gray_img), title('Grayscale Image');
hold on;
plot(regions, 'showPixelList', true, 'showEllipses', false);
title('Microaneurysm Detection using Blob Detection');
