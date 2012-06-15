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

		// Get ID of last post
		var last_post = $('div.post:last').data('post-id');

		$.get('/api/v1/posts/50/20/', function(data)
		{
			$(data).each(function(i)
			{
				post = data[i]
				$(document.createElement('div'))
					.addClass('post')
					.data('post-id', data[i].id)
					.html('\
							<div class="left">\
								<a class="blog-avatar" href="//derp/"><img src="/asset/' + post.blog.avatar.diskfile + '" alt="' + post.blog.name + '" /></a>\
							</div>\
							<div class="right">\
								<img class="post-image" src="/asset/' + post.asset.diskfile + '" />\
							</div>\
						')
					.appendTo('#content')
			});

			current_height = body_height()
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