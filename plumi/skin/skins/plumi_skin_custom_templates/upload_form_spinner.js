//andycat
//andy@engagemedia.org
$(document).ready(function(){

        $('form#plumivideo-base-edit').submit(function(){
                //var loading_html = '<div style="margin-left:auto; margin-right:auto;text-align:center;"><b>Please be patient while your file is uploaded. It may take a long time. Thanks.</b> <div style="display:block;margin-left:auto; margin-right:auto;"> <img src="ajax-loader.gif"/> </div> </div> ';

                //make a check that we are on the last step
                $('form#plumivideo-base-edit').find('#video_file_file').each(function() {
                        var loading_html = '<p><b>Please be patient while your file is uploading. It may take a long time. Thanks.</b> <p> <img src="ajax-loader.gif"/> </p> </p> ';
                        $('#video_file_file').after(loading_html);
                        alert("You are about to start uploading. Please be patient, as this may take some time. Don't close your browser or click 'Save' again. Thanks!");
                });

        });


});
