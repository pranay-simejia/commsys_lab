close all; clear all; clc;

t=0:1/300:100;
signal_x=sin(2*pi*400*t)+sin(2*pi*600);
plot(t,signal_x);
sound(signal_x,2500);
