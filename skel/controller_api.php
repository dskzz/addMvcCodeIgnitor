<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class CONTROLLERNAMEHERE extends MY_Controller {

	/**
	 * Controller.
	 */
	public function __construct()
	{
			parent::__construct();

			$this->data['title'] = 'Listography';
			$this->data['name']  = 'CONTROLLERNAMEHERE';
			$this->data['SITE_URL'] = SITE_URL;
			$this->data['ACTIVE_CONTROLLER'] = 'CONTROLLERNAMEHERE';
			$this->data['js_array']  = array( QUOTESCRIPTNAMEHERE );
			$this->load->model( 'MODELNAMEHERE' );
			// Your own constructor code
	}

	private function _finish(  )
	{
		$this->smarty->view('index.tpl', $this->data);
	}

	public function index()
	{
		$this->MODELNAMEHERE->getMODELNAMEHERE();
		$this->data['viewPage'] = strtolower( 'panels/LOWERNAMEHERE/LOWERNAMEHERE.tpl' )
		$this->_finish(  );
	}


}
