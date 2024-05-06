% video = VideoReader('src/l_6.mp4');
% if ~exist('left', 'dir')
%     mkdir('left');
% end
% k = 0;
% while hasFrame(video)
%     k = k + 1;
%     frame = readFrame(video);
%     filename = ['./left/' sprintf('%03d',k) '.jpg'];
%     imwrite(frame, filename);
% end

video = VideoReader('C:\Code\VideoProcess\VideoStitchingViaShakinessRemoving\cut\right_top.avi');
if ~exist('right_top', 'dir')
    mkdir('right_top');
end
k = 0;
while hasFrame(video)
    k = k + 1;
    frame = readFrame(video);
    filename = ['./right_top/' sprintf('%03d',k) '.jpg'];
    imwrite(frame, filename);
end