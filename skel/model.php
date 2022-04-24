<?php  
  
class MODELNAMEHERE extends MY_Model {  
  
	public function __construct()
	{
			parent::__construct();

			$this->db = $this->dbLive();
			
			// Your own constructor code
	}


    public function getMODELNAMEHERE() {  
		$sql = "SELECT ";
		
		$result = $this->fetchAllAssoc( $sql );
    }  
  
      
}  
?>  
