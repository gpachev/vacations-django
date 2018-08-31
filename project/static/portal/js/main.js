$(function () {
    $('#id_from_date').datetimepicker();
    $('#id_to_date').datetimepicker();
    $('#id_from_date').data("DateTimePicker").locale("bg").format("YYYY-MM-DD HH:mm");
    $('#id_to_date').data("DateTimePicker").locale("bg").format("YYYY-MM-DD HH:mm");
});