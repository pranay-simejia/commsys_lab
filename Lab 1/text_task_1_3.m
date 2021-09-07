clear all; close all; clc;

fh = fopen('text.txt');
fread(fh);
text_to_bit = dec2bin(fh);
r = reshape(text_to_bit,1,[]);
