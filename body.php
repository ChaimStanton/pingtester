<?php
echo '<html>
<body>
<table class="table table-light table-sm table-striped table-bordered table-hover">

<thead class="thead-light">
        <tr>
        <th scope="col">#</th>
        <th scope="col">First</th>
        <th scope="col">Last</th>
        <th scope="col">Handle</th>
        </tr>
</thead>

<tbody>
';

$f = fopen("sample.csv", "r");
while (($line = fgetcsv($f)) !== false) {
        echo "<tr>";
        foreach ($line as $cell) {
                echo "<td>" . htmlspecialchars($cell) . "</td>";
        }
        echo "</tr>\n";
}
fclose($f);

echo "
</tbody>
</table></body></html>";