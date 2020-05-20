<?php

echo '
<body>
<table class="table table-light table-sm table-striped
              table-bordered  table-hover table-responsive" 
id="table"
>
<div class="table-responsive">

<thead class="thead-light">
        <tr>
        <th scope="col">status</th>
        <th scope="col">remark</th>
        <th scope="col">time (day/month/year hour/minute/second)</th>
        </tr>
</thead>

<tbody>
';

$command = escapeshellcmd("python3 ./bodyBetter.py");
$output = shell_exec($command);
echo $output;

echo '
</tbody>
</table>
</div>

</body>
';
