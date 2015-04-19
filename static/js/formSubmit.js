function submitForm() {
	var data = document.getElementById("inputlg").innertext;;
	xmlhttp.open("GET","/search?pincode=data",true);
	xmlhttp.send();
}