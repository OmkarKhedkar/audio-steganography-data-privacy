close all; clear all; clc;

[FileName,PathName] = uigetfile({'.wav'}, 'Select stego audio:');
wavin = [PathName FileName];

password = 'mypassword123';

msg = lsb_dec(wavin, password);

fileID = fopen('encrypted.txt', 'w');

fprintf(fileID, 'Retrieved message: %s\n', msg);

fclose(fileID);
