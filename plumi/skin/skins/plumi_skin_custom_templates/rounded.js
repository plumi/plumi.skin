jq(document).ready(function(){

  jq('.rounded').corners();

  jq('.rounded').corners(); /* test for double rounding */

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
