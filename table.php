<html lang="en">
<head>
    <meta charset="utf-8">

    <title>am I connected to internet</title>

    <?php include 'header.php'; ?>

</head>

<body>
<table class="table table-light table-sm table-striped
              table-bordered  table-hover table-responsive" 
id="table"
data-search="true"
>
<div class="table-responsive">

<thead class="thead-light">
        <tr>
        <th scope="col">status</th>
        <th scope="col">time</th>
        <th scope="col">completed process</th>
        </tr>
</thead>

<tbody>

<?php
$command = escapeshellcmd("python3 ./bodyBetter.py");
$output = shell_exec($command);
echo $output;
?>

</tbody>
</table>
</div>


</body>

<?php include 'footer.php'; ?>

</html>