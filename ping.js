var PING = (function ($) {
	var pingFrequency = 5000;
        var pinging = false;
        var pingInProgress = false;
        var doPingInfo = function () {
            if (!pinging) {
                return;
            }

            pingInProgress = true;
            var startTime = new Date().getTime();
            var cmd = "iz";

            if(typeof ajax_request !== 'undefined')
                ajax_request.abort();
            ajax_request = $.ajax({
                url: cgiUrl + cmd,
                type: "GET",
                dataType: "html",
                cache: false,
                timeout: 5000,
                success: function (data, textStatus, jqXHR) {
                    $("#resp").html(data);
                    //log("s");
                },
                complete: function () {
                    pingInProgress = false;

                    var endTime = new Date().getTime();
                    var latency = endTime - startTime;
					updateLatency(latency)
                    if (pinging) {
                        var nextRun = pingFrequency - latency;
                        //console.log(nextRun);
                        if (nextRun > 0) {
                            setTimeout(doPingInfo, nextRun);
                        } else {
                            doPingInfo();
                        }
                    }


                },
                error: function () {
                    //log("e");
                }
            })
        };

        var pingStart = function() {
            pinging = true;
            if (pingInProgress) {
                return;
            }
            doPingInfo();
        }

        var pingStop = function() {
            pinging = false;
        }

		return {
			pingStart: pingStart,
			pingStop: pingStop
		};
		
}(jQuery));