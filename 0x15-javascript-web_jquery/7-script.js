// Fetches character name from a url then displays
// it in the DIV#character tag

let url = 'https://swapi.co/api/people/5/?format=json';
$.get(url, function (data, stat) {
	  $('div#character').text(data.name);
});
