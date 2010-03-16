jq(document).ready(function(){

  jq('#plumivideo-base-edit').submit(function(){            
    jq('form#plumivideo-base-edit').find('#video_file_file').each(function() {
        var loading_html = '<p>Please be patient while your file is uploading. It may take a long time. Thanks.</p> <img src="ajax-loader.gif"/>';
        jq('#video_file_file').after(loading_html);
        alert("You are about to start uploading. Please be patient, as this may take some time. Don't close your browser or click 'Save' again. Thanks!");
    });
  });
        
  jq('#toggleBookmarks').click(function() {
    if (jq('#toggledBookmarks').is(":hidden"))
 	{
   	     	    jq('#toggledBookmarks').fadeIn("slow");
  	} else {
     	    jq('#toggledBookmarks').fadeOut("slow");
 	}
  });
	         	
  jq('.rounded').corners();

  jq('.rounded').corners(); /* test for double rounding */

  jq('.portlet').corners();

  jq('.portlet').corners();

  jq('#visual-portal-wrapper').corners();

  jq('#visual-portal-wrapper').corners();

  jq('table', jq('#featureTabsContainer .tab')[0]).each(function(){jq('.native').hide();});

  jq('#featureTabsContainer').show();

  tab(0);

});

function tab(n) {

  jq('#featureTabsContainer .tab').removeClass('tab_selected');

  jq(jq('#featureTabsContainer .tab')[n]).addClass('tab_selected');

  jq('#featureElementsContainer .feature').hide();

  jq(jq('#featureElementsContainer .feature')[n]).show();

}


    
