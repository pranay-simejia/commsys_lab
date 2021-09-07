clear all;close all; clc;

p = imread('image.jpg');
image(p);
image_to_bit = dec2bin(p);
r = reshape(image_to_bit,1,[]);
