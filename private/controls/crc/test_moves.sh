#/bin/bash

#gpio -g pwm 18 80
#sleep 2

for i in {280..80}
do
        echo $i
        gpio -g pwm 18 $i
	#sleep 0.005
done

for i in {80..280}
do
	echo $i
	gpio -g pwm 18 $i
done
