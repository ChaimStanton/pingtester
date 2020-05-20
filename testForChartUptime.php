<?php
// this is a php file for getting the chart data for uptime

$command = escapeshellcmd("python3 ./uptimeChartBackend.py"); // goes to python program which gets numbers
$output = shell_exec($command);
$outputLIST = explode(",", $output); // converts output to list
$uptime = $outputLIST[0];
$downtime = $outputLIST[1]
?>

<?php echo $downtime?>