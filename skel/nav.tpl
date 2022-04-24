
<nav class="navbar  navbar-expand  sticky-top sticky-offset navbar-dark bg-dark  mb-4 ml-n3">
	<div class='container-fluid'>
		<span class="border-right border-info  p-1 mr-2">
		<a class="navbar-brand" href="#">{$name}</a>
		</span>
		{* <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
			<span class="navbar-toggler-icon"></span>
		</button> *}

		<div class="collapse navbar-collapse" id="navbarSupportedContent">
			<ul class="navbar-nav mr-auto">
				<li class="nav-item {if $ACTION==''}active{/if}">
					<a class="nav-link" href="{$smarty.const.SITE_URL}{$CONTROLLER}/">Page List</a>
				</li>
				{* <li class="nav-item">
					<a class="nav-link" href="#">Page</a>
				</li>
				<li class="nav-item {if $ACTION=='SOMEACTION'}active{/if}">
					<a class="nav-link" href="#">Page</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="#">Log</a>
				</li> *}
			</ul>

			
			{if $ACTION == 'dictionary'}
				<div class='col-5 dict-nav-btn'>
					<span class='dict-save-edits mr-3'>
						<input type='button' class='btn btn-secondary dict-edit-button-save' data-toggle='modal' data-target='#save-dict-modal' value='Save Changes'>
						<input type='button' class='btn btn-outline-secondary dict-edit-button-reset' value='Reset'>
					</span>
					<input type='button' class='btn btn-secondary dict-add-btn float-right' value='New Filter'>
				</div>
			{else if $ACTION == '' }  {* ACTION empty is the default page *}
				<div class='col-5 filter-nav-btn'>
					<input type='button' class='btn btn-secondary filter-run-auto float-right' value='Configure'>
				</div>
			{/if}

		</div>
	</div>
</nav>

