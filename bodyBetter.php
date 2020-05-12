<?php

$command = escapeshellcmd("python3 ./bodyBetter.py");
$output = shell_exec($command);
echo $output;

