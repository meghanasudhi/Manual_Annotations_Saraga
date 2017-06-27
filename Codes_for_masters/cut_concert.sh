#!/bin/bash
#!/usr/bin/bash
timeList=$1
concertfile=$2
concertfile_ext=`echo $concertfile | cut -d "." -f2`
concertfile_root=`echo $concertfile | cut -d "." -f1`
output_mp3name=`echo $concertfile_root.mp3`
echo $output_mp3name
if [ "$concertfile_ext" = 'wav' ]
then
lame -V0 $concertfile $output_mp3name
fi

numTime=`wc -l < $timeList`
echo $numTime
numTime=$(($numTime/2))
echo $numTime
cnt=1
for i in `seq 1 $numTime`; do
    echo $i
    nxt=$(expr "$cnt" + 1)
    st_line=`cat $timeList | head -$cnt | tail -1`
    st_time=`echo $st_line | cut -d " " -f1`
    track_name=`echo $st_line | cut -d " " -f2`
    et_line=`cat $timeList | head -$nxt | tail -1`
    et_time=`echo $et_line | cut -d " " -f1`
    echo "$st_time $et_time"
    duration=`echo "$et_time-$st_time" | bc -l`
    echo $duration
    cutfilename=`echo $track_name.mp3`
    ffmpeg -i $output_mp3name -t $duration -ss $st_time -acodec copy $cutfilename -loglevel 'verbose'
    cnt=$(expr "$cnt" + 2)
done
