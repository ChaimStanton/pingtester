<?php
/*
Error reporting helps you understand what's wrong with your code, remove in production.
*/

$command = escapeshellcmd("python3 /home/chaim/Documents/development/speedtest/bodyBetter.py");
$output = shell_exec($command);
echo $output;

