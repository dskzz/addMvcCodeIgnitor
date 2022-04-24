# addMvcCodeIgnitor
CodeIgnitor - Py Script and skeleton files to setup new model, controller, view, nav, js.

Also lets you setup a viewless API type which does not include the view, nav, js

Put all files in application directory.  I always setup CI to use smarty, so for view this moves smarty folders over to view/templates/ 

Also it sets up a default /panels/viewname/viewname.tpl

Sends typescript file down to ../scripts-dev.  scripts.ts_ is named w underscore else ts compiler will dig up the file and try and compile it despite best efforts.

Uses sed to replace stuff for example, in controller, have

$this->load->model("MODELNAME");  

and will replace MODELNAME with whatever_model, the name of the file in the models 

So its sort of specific to my needs, but pretty easy to modify.

BTW to use the TS globals trick to drop in defined global vars from smarty, init a globals_def.tpl with your globals, called from a common smarty file, then reinit them in TS to be called by every TS  file that needs them.  My code below:

**application/view/templates/common/globals_def.tpl**
	<script>
	{literal}
	  window.__INITIAL_DATA__ = {
	{/literal}
	  'siteUrl' : '{$smarty.const.SITE_URL}',
	  'apiUrl'  : '{$smarty.const.API_URL}',
	  'userId' : "{$smarty.session.user_info.id}",
	  'environment' : "{$smarty.const.ENVIRONMENT}"
	{literal}
	 }
	{/literal}

	</script>

**../scripts-dev/globals.ts**
// @ts-check
// enable typescript

	type InitialData = {
		siteUrl: string
		apiUrl:  string
		userId: string
		environment: string
	};

	export    const initialData = (window as any).__INITIAL_DATA__ as InitialData;

	export const DB_DATA = (window as any).DB_DATA as JSON; 




##BTW smarty layout is as such:
**application/view/templates/index.tpl**
	{include file="common\\header.tpl"} 
	{include file="common\\body.tpl"} 
	{include file="common\\footer.tpl"} 

header is the usual stuff.  <head></head>. 

**application/view/templates/common/body.tpm**
Then common body (using bootstrap for example - setting up containers and such), important part is this line:
	{include file=$viewPage}
  
  
 **application/view/templates/common/footer.tpm**
 Footer should include that globals template file I referred to before.  I also have it setup in the skel dir so that the controller assigns a list of js files to an array which are then dynamically loaded from the footer:
 
 
	{if isset( $js_array )}
		{foreach from=$js_array item=js_file}
			<script src="{$smarty.const.SITE_URL}/scripts/{$js_file}" type='module'></script>
		{/foreach}
	{/if}
  
 I think thats what you need to make this plug and play, basically.  Oh yeah there's also a nav - I built it so the nav pulls in from the db.   I have a nav_model that pulls that info in and drops it into views/common/navbar.tpl, that's included in the generated views.  
 
 OH! Important! I also am using custom MY_Controller and MY_model!!  I find I cant use CI without some custom helpers.  Check my gists for the base controller I use.   I also setup the constants file with a bunch of stuff.  Damn I should just upload my base setup. 
 
 Any of these stuff you want to change, change it in the skel/ files, they are the base files.  The magik is in the python file.  Any excuse to code in python...esp when im in php land all day
