function runPyScript(input, file){
    var ajaxObject = ({
        type: "POST",
        url:  file,
        async: false,
        data: {}
    });

    return ajaxObject.responseText;
}

function feedPython(){
    datatosend = 'this is my matrix';
    result = runPyScript(datatosend);
    console.log('Got back ' + result);
}

feedPython("trlala", "/testForChartUptime")