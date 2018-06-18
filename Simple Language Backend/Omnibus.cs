using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Omnibus {

	int i;
	bool b;
	float f;
	string s;
	char c;

	public Omnibus(){
		i = 0;
		b = false;
		f = 0.0f;
		s = "";
		c = ' ';
	}

	/* GETTER AND SETTER FOR INT */
	public int getint(){
		return i;
	}
	public void setint(int input){
		i = input;
		return;
	}

	/* GETTER AND SETTER FOR BOOL */
	public bool getbool(){
		return b;
	}
	public void setbool(bool input){
		b = input;
		return;
	}

	/* GETTER AND SETTER FOR FLOAT */
	public float getfloat(){
		return f;
	}
	public void setfloat(float input){
		f = input;
		return;
	}

	/* GETTER AND SETTER FOR STRING */
	public string getstring(){
		return s;
	}
	public void setstring(string input){
		s = input;
		return;
	}

	/* GETTER AND SETTER FOR CHAR */
	public char getchar(){
		return c;
	}
	public void setchar(char input){
		c = input;
		return;
	}
}
