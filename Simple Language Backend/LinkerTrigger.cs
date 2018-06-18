using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LinkerTrigger : MonoBehaviour {

	public GameObject obj = null;

	void OnTriggerStay2D(Collider2D other){
		ProgramObject temp = other.GetComponent<ProgramObject>();
		if (temp != null){
			if (temp.GetType().Name != "EmptyButton"){
				//Debug.Log(temp.name);
				obj = other.gameObject;
			}
			else
				obj = null;
		}
	}
}
