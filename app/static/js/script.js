$(document).ready(function() {
    var current_effect = 'bounce';

    function getStatus() {
        run_waitMe(current_effect);
        $.ajax({
            url: "http://" + window.location.host + "/api/v1/heater/state"
        }).then(function(data) {
            if (data.state === 1) {
                $("input[name=toggle]").prop('checked', true);
                $('#content').waitMe('hide');
            } else {
                $("input[name=toggle]").prop('checked', false);
                $('#content').waitMe('hide');
            }
        });
    }

    $("input[name=toggle]").change(function() {
        if ($(this).prop('checked')) {
            $.ajax({
                url: "http://" + window.location.host + "/api/v1/heater/turn/on",
                type: 'PUT',
                success: function(response) {
                    //...
                }
            });
        } else {
            $.ajax({
                url: "http://" + window.location.host + "/api/v1/heater/turn/off",
                type: 'PUT',
                success: function(response) {
                    //...
                }
            });
        }
    });

    setInterval(function() {
        getStatus();
    }, 60000);

    getStatus();

    function run_waitMe(effect) {
        $('#content').waitMe({
            effect: 'bounce',
            text: '',
            bg: 'rgba(255,255,255,0.7)',
            color: '#000',
            maxSize: '',
            waitTime: -1,
            source: '',
            textPos: 'vertical',
            fontSize: '',
            onClose: function() {}
        });
    }
});