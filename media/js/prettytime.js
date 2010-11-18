
function prettytime(date) {
	
	date = new Date(date);

	var diff = (((new Date()).getTime() - date.getTime()) / 1000),
		 future = diff < 0,
		 day_diff = Math.abs(Math.floor(diff / 86400));

	diff = Math.abs(diff);

	function str(futur, past, val)  {
		return (future ? futur : past).replace("_", val);		
	} 
	
	return diff < 86400 && (
			 diff < 60 && "just now" ||
			 diff < 120 && (future ? "after a minute" : "1 minute ago") ||
			 diff < 3600 && str("after _ minutes", "_ minutes ago", Math.floor( diff / 60 )) ||
			 diff < 7200 && (future ? "after one hour" : "1 hour ago") ||
			 diff < 86400 && str("after _ hours", "_ hours ago", Math.floor(diff / 3600))) ||
			 day_diff == 1 && (future ? "Tomorrow" : "Yesterday") ||
			 day_diff < 7 && str("after _ days", "_ days ago", day_diff) ||
			 str("after _ weeks", "_ weeks ago", Math.ceil( day_diff / 7 ))
}

