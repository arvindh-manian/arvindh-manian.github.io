Title: The Panmacticon: How I set up my computer to take pictures of me
Date: 2022-12-11
Modified: 2022-12-30 2:29 PM
Category: minis
Tags: cs
Slug: taking-pics
Summary: I used cron with a bash script to take images of me at a random time every thirty minutes.

I was recently watching [carykh's video on daily photos](https://www.youtube.com/watch?v=H4ukudIrLxQ) when I decided I would start taking daily photos too.

Unfortunately, I don't have nearly the mental fortitude to remember to do that everyday. So, instead, I've set my computer to (somewhat) do that for me.

Instead of taking photos every day, my computer will take a photo at a random point in time in each 30 minute interval.

Specifically, this entails a cron job which calls a bash script that takes photos of me using [imagesnap](https://github.com/rharder/imagesnap).

Here's the shell script:

    :::bash
    #!/bin/bash
    SCRIPT_DIR="/Users/arvindh/CS/projects/pics"
    statefile="${SCRIPT_DIR}/statefile"

    declare -i persistent_counter

    if [ -f "$statefile" ]; then
      read -r persistent_counter <"$statefile"
    else
      persistent_counter=0
    fi

    persistent_counter="$((persistent_counter + 1))"

    printf '%d\n' "$persistent_counter" >"$statefile"

    rand=$(($RANDOM % 1700 + 1))

    sleep $rand

    /opt/homebrew/bin/imagesnap "${SCRIPT_DIR}/img/${persistent_counter}.jpg"

Basically, I predefined a directory for the script (this instead could've been done by having the bash script find the directory that it was located in, but I wasn't sure how that interacted with cron). Inside of that directory, I have a file called `statefile` that exists to save the current number image that the bash script is on (as it saves them in the format `1.jpg`, `2.jpg`, etc.). The script reads in the file, increments the number found there, sleeps for a random amount of time from 0 to 1700 seconds<sup>[1]</sup> (I could've done 0 to 1800 but I wanted to avoid race conditions), and then takes a picture, saving it in the `/img/` folder.

Then, all we need is a cron job for it. 

    */30 * * * * /Users/arvindh/CS/projects/pics/launch.sh
    
Should work, running `launch.sh` every 30 minutes. 

Unfortunately, it doesn't. Apparently, in newer versions of Mac OS, cron doesn't have permissions to access the camera, which prevents the subsequent call to imagesnap from successfully taking a picture. The worst part is that imagesnap doesn't throw an error about this or output any message about the permissions issues, so any output in my log files in the course of debugging wasn't very helpful.

The workaround, as presented on [Stack Overflow](https://stackoverflow.com/a/52878770/20503988), is to create a wrapper application in Automator and have your cron job open that.

That wasn't very hard. The Automator job consists only of a "Run Shell Script" block, and the only text in there needs to be 

    /Users/arvindh/CS/projects/pics/launch.sh

I saved that Automator app as takepics.app in the /Applications directory. Then, the cron job should be

    */30 * * * * open /Applications/takepic.app

And there we go!

<iframe width="560" height="315" src="https://www.youtube.com/embed/eauOmFHx7H0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Here's the timelapse as of December 30. If I remember, I'll update it again sometime later in 2023. Maybe I'll even use a cron job to automate the creation of the timelapse and the updating of this post. But that's a task for another time.

# Footnotes

[1] This is a bit of a flawed way of doing random number generation. `$RANDOM` generates a number in the range of 0 to 32767. Since 32767 is not divisible by 1700, this means there is a higher chance of `$RANDOM % 1700` being a lower number than a relatively higher one. This is a trivial enough use case where it doesn't matter, though.