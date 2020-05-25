<!DOCTYPE html>
<html>

<?php include 'header.php'; ?>

<?php
    // this is a php file for getting the chart data for uptime

    $command = escapeshellcmd("python3 ./uptimeChartBackend.py"); // goes to python program which gets numbers
    $output = shell_exec($command);
?>


<script>
    $(function graphData(){
        console.log("Was here");
        let output = <?php echo $output; ?>;

        let chart = document.querySelector('canvas').chart;

        chart.data.datasets[0].data[1] = output[0];
        chart.data.datasets[0].data[0] = output[1];
        chart.update();
        
    });
</script>

<body onload="graphData()">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.1.1/aos.css">

    <div class="card">
        <div class="card-header">
            <h4>Uptime vs Downtime</h4>
        </div>
        <div class="card-body">
            <div id="chart"><canvas data-bs-chart="{&quot;type&quot;:&quot;pie&quot;,&quot;data&quot;:{&quot;labels&quot;:[&quot;Uptime&quot;,&quot;Downtime&quot;],&quot;datasets&quot;:[{&quot;label&quot;:&quot;UpTime&quot;,&quot;backgroundColor&quot;:[&quot;rgb(51,255,0)&quot;,&quot;rgb(255,0,0)&quot;],&quot;borderColor&quot;:[&quot;rgba(0,0,0,0.1)&quot;,&quot;rgba(0,0,0,0.1)&quot;],&quot;data&quot;:[&quot;100&quot;,&quot;100&quot;]}]},&quot;options&quot;:{&quot;maintainAspectRatio&quot;:true,&quot;legend&quot;:{&quot;display&quot;:true,&quot;reverse&quot;:false},&quot;title&quot;:{&quot;text&quot;:&quot;Uptime vs Downtime&quot;,&quot;display&quot;:true}}}"></canvas></div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>
    <script src="assets/js/smart-forms.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.8.0/Chart.bundle.min.js"></script>
    <script src="assets/js/script.min.js"></script>



</body>

<?php include 'footer.php'; ?>

</html>