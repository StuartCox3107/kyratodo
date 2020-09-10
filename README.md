in base.html

add below to bottom in script
document.getElementById("matfix").addEventListener("click", function(e) {
	e.stopPropagation();
});

In addtask.html

give div surrounding date picker the id of matfix

