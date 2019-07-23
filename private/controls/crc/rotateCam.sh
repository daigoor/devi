#!/bin/bash

# set variables for horizontal movements
CamHorPosFile=commands/crc/cam_H_position
HPin=18
LowerHLim=80
UpperHLim=280
HStep=5

# set variables for vertical movements
CamVerPosFile=commands/crc/cam_V_position
VPin=19
LowerVLim=100
UpperVLim=250
VStep=10

usageMsg='usage: ./rotateHorizontal.sh [left|right|up|down]'

#echo $#
#echo $1
if [ $# -lt 1 ]
then
	echo $usageMsg
	exit 1
elif [ $1 == 'left' ]
then
	op=+
	activeMovFile=$CamHorPosFile
	activePin=$HPin
	lowerLimit=$LowerHLim
	upperLimit=$UpperHLim
	step=$HStep
elif [ $1 == 'right' ]
then
	op=-
	activeMovFile=$CamHorPosFile
	activePin=$HPin
	lowerLimit=$LowerHLim
	upperLimit=$UpperHLim
	step=$HStep
elif [ $1 == 'up' ]
then
	op=-
	activeMovFile=$CamVerPosFile
	activePin=$VPin
	lowerLimit=$LowerVLim
	upperLimit=$UpperVLim
	step=$VStep
elif [ $1 == 'down' ]
then
	op=+
	activeMovFile=$CamVerPosFile
	activePin=$VPin
	lowerLimit=$LowerVLim
	upperLimit=$UpperVLim
	step=$VStep
else
	echo $usageMsg
	exit 1
fi

echo $activeMovFile
# set new position
currentPos=`cat $activeMovFile`
newPos=`expr $currentPos $op $step` 
echo $newPos

# move camera to new position
if [ $newPos -le $upperLimit ] && [ $newPos -ge $lowerLimit ]
then
	gpio -g pwm $activePin $newPos

	# update new position
	echo $newPos > $activeMovFile
fi
