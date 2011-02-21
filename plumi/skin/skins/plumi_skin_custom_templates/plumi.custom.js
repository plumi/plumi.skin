function addInput() {
    var ni = document.getElementById('homepage-inputs');
    var numi = document.getElementById('theValue');
    var num = (document.getElementById("theValue").value -1)+ 2;
    numi.value = num;
    var divIdName = "my"+num+"Div";
    var newdiv = document.createElement('div');
    newdiv.setAttribute("id",divIdName);
    newdiv.innerHTML = "<input type=\"text\" name=\"homepages:list\"/> <a href=\"javascript:;\" onclick=\"removeElement(\'"+divIdName+"\')\">x<" + "/a>";
    ni.appendChild(newdiv);
    }

function removeElement(divNum) {
    var d = document.getElementById('homepage-inputs');
    var olddiv = document.getElementById(divNum);
    d.removeChild(olddiv);
    }

jq(document).ready(function(){
	jq('.formHelp a')
    		.prepOverlay({
            subtype: 'ajax',
            filter: '.popup-formHelp'
	});
});

