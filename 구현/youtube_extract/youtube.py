import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=HQzPya3a-Hk") #�ٿ���� ������ URL ����

vids= yt.streams.all()

#���� ���� ����Ʈ Ȯ��
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("�ٿ� ���� ȭ����? "))

parent_dir = "D:\문서\4학년\1학기\창의융합종합설계\구현\youtube-download"
vids[vnum].download(parent_dir) #�ٿ�ε� ����

new_filename = input("��ȯ �� mp3 ���ϸ���?")

default_filename = vids[vnum].default_filename
subprocess.call(['ffmpeg', '-i',                 #cmd ��ɾ� ����
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('������ �ٿ�ε� �� mp3 ��ȯ �Ϸ�!')
