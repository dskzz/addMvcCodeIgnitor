<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class CONTROLLERNAMEHERE extends MY_Controller {

	/**
	 * Controller.
	 */
	public function __construct()
	{
			parent::__construct();
			$this->data['name']  = 'CONTROLLERNAMEHERE';
			$this->data['SITE_URL'] = SITE_URL;
			$this->data['ACTIVE_CONTROLLER'] = 'CONTROLLERNAMEHERE';
			$this->load->model( 'MODELNAMEHERE' );
			// Your own constructor code
	}

	private function _finish( $result )
	{
		return json_encode( $result );
	}

	public function index()
	{
		$this->MODELNAMEHERE->getMODELNAMEHERE();
		$this->_finish(  );
	}


}
