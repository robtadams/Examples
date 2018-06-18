using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Reflection;

public class Linker : MonoBehaviour {

	public GameObject A, B = null;
	Omnibus bus = new Omnibus();

	// Update is called every frame
	void Update(){
		
			// Get the GameObjects LeftTrigger and RightTrigger
			GameObject LTrigger = this.gameObject.transform.Find("LeftTrigger").gameObject;
			GameObject RTrigger = this.gameObject.transform.Find("RightTrigger").gameObject;

			// Get the components of type LinkerTrigger from the LeftTrigger and RightTrigger game objects
			LinkerTrigger L = LTrigger.GetComponent<LinkerTrigger>();
			LinkerTrigger R = RTrigger.GetComponent<LinkerTrigger>();

			// Get the objects that collide with the triggers L and R
			A = L.obj;
			B = R.obj;

			// If there are objects that have collided with L and R ...
			if (A != null && B != null){

				// ... grab the components of type ProgramObject from those GameObjects that collide.
				ProgramObject componentA = A.GetComponent<ProgramObject>();
				ProgramObject componentB = B.GetComponent<ProgramObject>();

				// Then call B.main() passing A.main() as the argument
				componentB.main(componentA.main(bus));
			}
	}
}
