clear all; close all; clc;

[Y, FS] = audioread('audio.mp3');
sound(Y, FS);
plot(Y);
audio_to_bit = dec2bin(Y);
r = reshape(audio_to_bit,1,[]);
