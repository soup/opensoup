var current_height = -1;
var counter = -1;
var viewport_height = -1;

function body_height() {
	var D = document;
	return Math.max(
		Math.max(D.body.scrollHeight, D.documentElement.scrollHeight),
		Math.max(D.body.offsetHeight, D.documentElement.offsetHeight),
		Math.max(D.body.clientHeight, D.documentElement.clientHeight)
	);
}

function check_scrollposition()
{
	counter++;

	if($(window).scrollTop() + viewport_height > current_height - 1000 && $(window).scrollTop() != 0) {
		console.log('Cursor is reaching page end, loading new content…')
		console.log('(check ' + counter + ')')
		console.log('Scroll position: ' + $(window).scrollTop());
		console.log('Current height: ' + current_height);

		//for(i = 0; i < 20; i++)
		//	$('#post10').clone().appendTo('#content')

		// Get ID of last post
		var last_post = $('div.post:last').data('post-id');
		console.log('Last post is ' + last_post)

		$.get('/api/v1/posts/' + last_post + '/20/', function(data)
		{
			$(data).each(function(i)
			{
				$(document.createElement('div'))
					.addClass('post')
					.data('post-id', data[i].id)
					.html('This is post #' + data[i].id)
					.appendTo('#content')
			});

			current_height = body_height()

			console.log('New height: ' + current_height);
			console.log('–––––––––––––––––––––––\n\n')

			if(data.length < 20)
			{
				reached_end = true;
				$(document.createElement('div'))
					.html('<h4>You\'ve reached the end.</h4>')
					.appendTo('#content')

				// Don't reschedule
				return;
			}

			// Reschedule check
			window.setTimeout(check_scrollposition, 300);
		});
	} else {
		// Reschedule check
		window.setTimeout(check_scrollposition, 300);
	}
}

$(document).ready(function()
{
	current_height = body_height();
	viewport_height = $(document).height();

	// Start scroll position check loop
	console.log('Initiating endless scrolling loop')
	window.setTimeout(check_scrollposition, 300);
});
/*
0
10

6-0 = 6
10-0/2 = 5

6
6

6-0 = 6
6-0/2
*/