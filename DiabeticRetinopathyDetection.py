% Load the retinal image from file
img = imread('ret.jpg');

% Display the original image
figure, imshow(img);
title('Original Image');

% Convert the RGB image to grayscale
gray_img = rgb2gray(img);

% Display the grayscale image
figure, imshow(gray_img);
title('Grayscale Image');

% Enhance the contrast of the grayscale image
% Obtain the lower and upper intensity limits that can be used for contrast stretching
lower_limit = stretchlim(gray_img);
upper_limit = [0; 1];

% Apply contrast adjustment using the calculated limits
contrast_adjusted_img = imadjust(gray_img, lower_limit, upper_limit);

% Display the contrast-adjusted image
figure, imshow(contrast_adjusted_img);
title('Contrast Adjusted Image');

% Apply median filtering to reduce noise
% Define the size of the filter window (3x3)
filter_window_size = [3 3];

% Perform median filtering on the contrast-adjusted image
filtered_img = medfilt2(contrast_adjusted_img, filter_window_size);

% Display the filtered image
figure, imshow(filtered_img);
title('Median Filtered Image');

% Apply watershed segmentation to separate blood vessels and other structures
% Use the filtered image as input for the watershed algorithm
segmented_img = watershed(filtered_img);

% Display the segmented image
figure, imshow(label2rgb(segmented_img));
title('Segmented Image (Watershed)');

% Detect the optic disc using circular Hough transform
% Define the range of radii to search for circles (corresponding to the optic disc)
min_radius = 50;
max_radius = 100;

% Apply the imfindcircles function to find circles with bright polarity
[centers, radii] = imfindcircles(segmented_img, [min_radius max_radius], 'ObjectPolarity', 'bright');

% Draw the detected circles on the original image
figure, imshow(img);
hold on;
viscircles(centers, radii, 'EdgeColor', 'b');
hold off;
title('Optic Disc Detection');

% Calculate the area of the detected optic disc
% The area of a circle is calculated as π * radius^2
optic_disc_area = pi * radii.^2;

% Calculate the number of microaneurysms in the segmented image
% Label connected components in the segmented image
microaneurysms = bwlabel(segmented_img);

% Determine the maximum label, which corresponds to the number of objects
num_microaneurysms = max(microaneurysms(:));

% Display the calculated results
fprintf('Optic disc area: %f\n', optic_disc_area);
fprintf('Number of microaneurysms: %d\n', num_microaneurysms);
