% Garrett Scholtes
% Graph shit

clear all;
close all;

alldata;

sumdata = zeros(12, 2, size(data,3));

for k = 1:size(data,3)
    sumdata(:,:,k)=[unique(data(:,1,k)) accumarray(data(:,1,k),data(:,3,k))];
end

cols = hsv(13)*0.9;
figure;
for k = 1:12
    plot(1:size(data,3), reshape(sumdata(k, 2, :), [1, size(data,3)]), 'color', cols(k,:));
    hold on;
end
xlabel('Minutes since 03-20 13:30 EDT');
ylabel('Points');
title('Points per team (sum of each account) versus time)');
legend({
    'NSTS2017',
    'Il|lIIIlIIlIIII0IOl',
    'Team-Zero',
    'Synergy',
    'CDARK',
    'MARS2017',
    'Cool Cats',
    'JASH',
    'HSK',
    'REED',
    'FAB5',
    'Strangers',
    
});