$(document).ready(utc2local);

function utc2local() {
    $('.UTCTime').text( (i, v) => new Date(v).toLocaleString())
}